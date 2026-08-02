#!/usr/bin/env python3
"""
generate_stats.py
Pulls GitHub contribution calendar via GraphQL and regenerates
metrics-panel.svg (glass-card style, matches the rest of the README).

Requires env var: GH_TOKEN (a GitHub token with read:user scope)
Requires env var: GH_USERNAME (defaults to SonamNarula if unset)
"""

import os
import sys
import json
import datetime
import urllib.request

GH_TOKEN = os.environ.get("GH_TOKEN")
GH_USERNAME = os.environ.get("GH_USERNAME", "SonamNarula")

if not GH_TOKEN:
    print("ERROR: GH_TOKEN environment variable not set.", file=sys.stderr)
    sys.exit(1)

BG, BAR, BORDER = "#0d0e14", "#0a0a0f", "#2a2d42"
RED, YELLOW, GREEN, BLUE, PURPLE = "#f7768e", "#e0af68", "#9ece6a", "#7aa2f7", "#bb9af7"
FG, MUTED = "#e8eaf6", "#7982a9"
FONT = "'JetBrains Mono','Fira Code',ui-monospace,monospace"

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""


def fetch_calendar(username, token):
    body = json.dumps({"query": QUERY, "variables": {"login": username}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": username,
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    if "errors" in data:
        print("GraphQL errors:", data["errors"], file=sys.stderr)
        sys.exit(1)
    return data["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def flatten_days(calendar):
    days = []
    for week in calendar["weeks"]:
        for day in week["contributionDays"]:
            days.append((day["date"], day["contributionCount"]))
    days.sort(key=lambda x: x[0])
    return days


def compute_streaks(days):
    """
    Correct streak logic:
    - If today has 0 contributions, don't zero the streak immediately —
      the day may not be "over" yet (timezone / Action run time).
      Walk backwards from the most recent day that HAS a contribution.
    - If the last active day is more than 1 day ago, streak is genuinely 0.
    - Longest streak = max run of consecutive contributing days in history.
    """
    if not days:
        return 0, 0

    today_str = datetime.date.today().isoformat()
    days = [d for d in days if d[0] <= today_str]

    last_active_idx = None
    for i in range(len(days) - 1, -1, -1):
        if days[i][1] > 0:
            last_active_idx = i
            break

    current_streak = 0
    if last_active_idx is not None:
        last_active_date = datetime.date.fromisoformat(days[last_active_idx][0])
        today = datetime.date.today()
        gap = (today - last_active_date).days

        if gap <= 1:
            i = last_active_idx
            while i >= 0 and days[i][1] > 0:
                current_streak += 1
                i -= 1
        else:
            current_streak = 0

    longest_streak = 0
    run = 0
    for _, count in days:
        if count > 0:
            run += 1
            longest_streak = max(longest_streak, run)
        else:
            run = 0

    return current_streak, longest_streak


def glass_chrome(cid, w, h, title):
    return f'''  <defs>
    <clipPath id="clip_{cid}"><rect width="{w}" height="{h}" rx="20"/></clipPath>
    <linearGradient id="edge_{cid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.55"/>
      <stop offset="50%" stop-color="{PURPLE}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{GREEN}" stop-opacity="0.45"/>
    </linearGradient>
    <linearGradient id="glass_{cid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.07"/>
      <stop offset="18%" stop-color="#ffffff" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="orb1_{cid}" cx="15%" cy="0%" r="60%">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="{BLUE}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orb2_{cid}" cx="100%" cy="100%" r="70%">
      <stop offset="0%" stop-color="{PURPLE}" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="{PURPLE}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .m{{fill:{MUTED};font-family:{FONT};font-size:12.5px;}}
    .title{{fill:{MUTED};font-family:{FONT};font-size:12.5px;letter-spacing:.4px;}}
    .prompt{{fill:{GREEN};font-family:{FONT};font-size:13px;}}
    .dot-live{{animation:pulse 2.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center;}}
    @keyframes pulse{{0%,100%{{opacity:1;transform:scale(1);}}50%{{opacity:.4;transform:scale(.82);}}}}
    .sheen{{animation:sheen 6s ease-in-out infinite;}}
    @keyframes sheen{{0%,100%{{opacity:.5;}}50%{{opacity:1;}}}}
  </style>
  <g clip-path="url(#clip_{cid})">
    <rect width="{w}" height="{h}" fill="{BG}"/>
    <rect width="{w}" height="{h}" fill="url(#orb1_{cid})"/>
    <rect width="{w}" height="{h}" fill="url(#orb2_{cid})"/>
    <rect width="{w}" height="{h}" fill="url(#glass_{cid})"/>
    <rect width="{w}" height="42" fill="{BAR}" opacity="0.75"/>
    <rect x="0" y="41" width="{w}" height="1.6" fill="url(#edge_{cid})" class="sheen"/>
    <circle cx="23" cy="21" r="6" fill="{RED}"/><circle cx="43" cy="21" r="6" fill="{YELLOW}"/>
    <circle cx="63" cy="21" r="6" fill="{GREEN}" class="dot-live"/>
    <text x="{w/2}" y="26" text-anchor="middle" class="title">{title}</text>
'''


def render_metrics_svg(total, current, longest, updated_date):
    W, H = 900, 200
    metrics = [
        ("Total Contributions", f"{total:,}", BLUE),
        ("Current Streak (days)", str(current), GREEN),
        ("Longest Streak (days)", str(longest), PURPLE),
    ]
    body = '    <text x="28" y="70" class="prompt">~ % stats --year --live</text>\n'
    seg_w = (W - 56) / 3
    for i, (label, val, color) in enumerate(metrics):
        cx = 28 + seg_w * i + seg_w / 2
        if i > 0:
            body += f'    <line x1="{28+seg_w*i:.0f}" y1="90" x2="{28+seg_w*i:.0f}" y2="160" stroke="{BORDER}" stroke-width="1"/>\n'
        body += f'    <text x="{cx:.0f}" y="130" text-anchor="middle" fill="{color}" font-family="{FONT}" font-size="34" font-weight="700">{val}</text>\n'
        body += f'    <text x="{cx:.0f}" y="152" text-anchor="middle" class="m" font-size="12">{label}</text>\n'
    body += f'    <line x1="28" y1="168" x2="{W-28}" y2="168" stroke="{BORDER}" stroke-width="1"/>\n'
    body += f'    <text x="28" y="188" class="m" font-size="11">last updated <tspan fill="{BLUE}">{updated_date}</tspan> &#183; auto-refreshed daily via GitHub Actions</text>\n'

    svg = f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += glass_chrome("metrics", W, H, "sonam@github — metrics")
    svg += body
    svg += f'''  </g>
  <rect x="0.75" y="0.75" width="{W-1.5}" height="{H-1.5}" rx="19.5" fill="none" stroke="url(#edge_metrics)" stroke-width="1.4" opacity="0.7"/>
</svg>
'''
    return svg


def main():
    calendar = fetch_calendar(GH_USERNAME, GH_TOKEN)
    total = calendar["totalContributions"]
    days = flatten_days(calendar)
    current, longest = compute_streaks(days)
    updated_date = datetime.date.today().isoformat()

    svg = render_metrics_svg(total, current, longest, updated_date)
    with open("metrics-panel.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Total: {total} | Current streak: {current} | Longest streak: {longest}")


if __name__ == "__main__":
    main()
