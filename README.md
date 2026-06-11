<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0d0e1a,25:131425,60:0d0e1a,100:0d0e1a&height=310&section=header&text=Sonam%20Narula&fontSize=82&fontColor=7aa2f7&animation=fadeIn&fontAlignY=43&desc=Ships%20real%20code%20%C2%B7%20Grinds%20DSA%20daily%20%C2%B7%20Trains%20like%20it%27s%20a%20sport%20%C2%B7%20Final%20Year%20CSE&descColor=bb9af7&descSize=17&descAlignY=64&stroke=7aa2f7&strokeWidth=1" />

<br/>

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=16&pause=2000&color=7AA2F7&center=true&vCenter=true&width=780&lines=CodeFusion+%E2%80%94+Real-Time+Collaborative+Editor+%7C+Built+From+Scratch+%E2%9A%A1;Trackify+%E2%80%94+Productivity+Suite+%7C+Live+%26+Used+Daily+%F0%9F%9A%80;NeuroNews+%E2%80%94+Live+News+Aggregator+%7C+React+%2B+REST+API;UI+Clones+%E2%80%94+Pixel-Perfect+Frontend+Craft+%7C+Built+to+Understand;1000%2B+DSA+Problems+Solved+%C2%B7+Still+Grinding+%F0%9F%94%A5;Final+Year+CSE+%40+JECRC%2C+Jaipur+%C2%B7+CRT+Full+Focus+Mode)](https://github.com/SonamNarula)

<br/>

<img src="https://komarev.com/ghpvc/?username=SonamNarula&style=for-the-badge&color=7aa2f7&label=PROFILE+VIEWS&labelColor=131425" />

<br/><br/>

I train every day.
I build real things.
I grind DSA like it is pre-season.

</div>

<div align="center">

<img src="https://img.shields.io/badge/DSA-1000%2B-7aa2f7?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/LeetCode-488%2B-FFA116?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/Streak-200%2B%20Days-bb9af7?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/Projects-4-7dcfff?style=for-the-badge&labelColor=131425" />

</div>

<br/>

---

## $ whoami

*Final year CS student who treats coding like a sport.*
*I train every day. I build real things. I grind DSA like it is pre-season.*
*The projects, the commits, the numbers — they do not lie.*

```yaml
name    : Sonam Narula
degree  : B.Tech CSE  —  JECRC University, Jaipur  [2023–27]
year    : Final Year

currently:
  - CRT  (Campus Recruitment Training)  — full focus mode
  - DSA  — 1000+ done, still going every single morning
  - System Design  — patterns, tradeoffs, first principles
  - Data Analytics — adding another weapon to the arsenal

shipped:
  CodeFusion : "real-time collaborative code editor  [Socket.io + Monaco · Live]"
  Trackify   : "student productivity suite            [Vite + React · Live]"

building:
  NeuroNews  : "live news aggregator                  [React + REST API]"
  UI Clones  : "pixel-perfect frontend reproductions  [HTML · CSS · JS]"

dsa:
  total    : 1000+
  leetcode : 488
  language : C++
  platforms: [LeetCode, GFG, Codolio]

mindset  : "show up every day, whether it counts or not — it always counts"
contact  : sonamnarula2108@gmail.com
```

---
## Focus areas 
<div align="center">

<img src="https://img.shields.io/badge/Full_Stack-Development-7aa2f7?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/Competitive-Programming-bb9af7?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/Data-Analytics-7dcfff?style=for-the-badge&labelColor=131425" />
<img src="https://img.shields.io/badge/System-Design-e0af68?style=for-the-badge&labelColor=131425" />

</div>

---

## $ ls ~/arsenal

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=c,cpp,java,py,js,ts,html,css,bash,markdown" />

<br/><br/>

**Frontend**

<img src="https://skillicons.dev/icons?i=react,redux,tailwind,vite,nextjs,bootstrap,sass,materialui,styledcomponents" />

<br/><br/>

**Backend & Database**

<img src="https://skillicons.dev/icons?i=nodejs,express,mongodb,mysql,firebase,prisma,graphql,redis" />

<br/><br/>

**Tools & DevOps**

<img src="https://skillicons.dev/icons?i=git,github,vscode,docker,postman,vercel,netlify,linux,figma,canva,notion,npm" />

<br/><br/>

**AI & Others**

<img src="https://skillicons.dev/icons?i=openai,tensorflow,pytorch" />

</div>

---

## $ ls ~/projects

> Four builds. Not for the resume. For the craft.

---

### ⚡ CodeFusion — Real-Time Collaborative Code Editor

> *"Google Docs for code. Full-stack. Zero shortcuts."*

The hardest problem I have taken on. Multiple developers. One shared Monaco editor. Every keystroke emits a Socket.io event, travels through a Node server, and renders on every connected client in milliseconds — with no polling, no page reload, no compromise. The editor itself runs on Monaco — the same engine behind VS Code — living inside the browser.

I did not pick an easy project. I picked the right one.

```
  STACK   React 18 · Node.js · Express · Socket.io · Monaco Editor · Tailwind CSS
  ARCH    Client / Server separated · Room-based WebSocket namespacing · In-memory Map
  STATUS  🟢 Live & Deployed  —  Vercel (frontend) · Railway (backend)
```

**How it works under the hood:**

```
  CLIENT A  (Monaco)          SERVER  (Node + Express)         CLIENT B  (Monaco)
       │                              │                               │
       ├──── room:join ──────────────►│                               │
       │                              ├────── user:joined ───────────►│
       │                              │                               │
       ├──── code:change ────────────►│                               │
       │     { roomId, code }         ├────── code:change ───────────►│  ← instant render
       │                              │                               │
       ├──── typing:start ───────────►│                               │
       │     { roomId, username }     ├────── typing:start ──────────►│  ← "X is typing…"
       │                              │                               │
       ├──── room:leave ─────────────►│                               │
       │                              ├────── user:left ─────────────►│
```

**The technical details:**

| Feature | What is actually happening |
|:--------|:--------------------------|
| ⚡ Sub-ms code sync | `code:change` on every keystroke — server broadcasts instantly to all room clients |
| 🏠 Room system | Unique room IDs · `Map<roomId, {users, code}>` fully server-managed |
| ⌨️ Live typing indicators | `typing:start` + `typing:stop` events · "X is typing…" shown across all clients |
| 🌐 Multi-language support | JS · Python · C++ · Java · Go · TypeScript — Monaco language mode API |
| ▶️ In-browser execution | Run code → output panel rendered, zero page reload |
| 🌙 Theme persistence | Dark / Light toggle · choice stored to localStorage |
| 📱 Fully responsive | Desktop · tablet · mobile — all handled |

[![Live Demo](https://img.shields.io/badge/Live_Demo-CodeFusion-7aa2f7?style=for-the-badge&logo=vercel&logoColor=white&labelColor=131425)](https://codefusion-collaborative-editor.vercel.app/)
&nbsp;
[![Source Code](https://img.shields.io/badge/Source%20Code-GitHub-bb9af7?style=for-the-badge&logo=github&logoColor=white&labelColor=131425)](https://github.com/SonamNarula/CodeFusion-a-collaborative-real-time-code-editor)

---

### 💜 Trackify — Student Productivity Suite

> *"Built for students who actually show up every day. Like me."*

My college minor project — ideated, designed, built solo, and deployed live. Not a tutorial follow-along. A real product, built around a real problem: I needed one place to track my DSA solves, log study hours, manage deadlines, and see whether my grind was actually adding up. Nothing clean existed. So I built it.

```
  STACK   React · JavaScript · Vite · CSS
  STATUS  🟢 Live @ trackify.wasmer.app
```

**What it does:**
- 📊 DSA solve tracker with daily streaks — the chain must not break
- ⏱️ Study session logging with cumulative hour tracking — the hours add up
- ✅ Task manager with deadline management — nothing slips
- 📈 Visual progress dashboard — your consistency, staring back at you
- 🎓 Sole developer — from idea to production

[![Live Demo](https://img.shields.io/badge/Live%20Demo-trackify.wasmer.app-7aa2f7?style=for-the-badge&labelColor=131425)](https://trackify.wasmer.app)
[![Source Code](https://img.shields.io/badge/Source%20Code-GitHub-bb9af7?style=for-the-badge&logo=github&logoColor=white&labelColor=131425)](https://github.com/SonamNarula/Trackify-college-minor-project)

---

### 📰 NeuroNews — Live News Aggregator

> *"News without the noise. Clean, filtered, and always current."*

A React news aggregator pulling live data from the NewsAPI. Built because most news apps are a mess — cluttered, overwhelming, and algorithmically poisoned. NeuroNews is the opposite: pick your category, scroll through clean articles, stay current. The codebase is complete; deployment is being finalised.

```
  STACK   React · NewsAPI · CSS
  STATUS  🟡 Code complete · Deployment in progress
```

**What it does:**
- 📡 Live articles via REST API — refreshed and always up to date
- 🗂️ Category filtering — Technology, Business, Sports, Health, Science, and more
- ♾️ Infinite scroll — no interruptions, just content
- 📱 Fully responsive — desktop through mobile
- 🧹 Distraction-free interface — content first, nothing else competing

[![Source Code](https://img.shields.io/badge/Source%20Code-GitHub-7aa2f7?style=for-the-badge&logo=github&logoColor=white&labelColor=131425)](https://github.com/SonamNarula/Neuro-News)

---

### 🎨 UI Clones — Frontend Precision & Craft

> *"You do not truly understand a UI until you can rebuild it exactly."*

Deliberate practice. Not copying for the sake of it — deconstructing how real product UIs are actually built, then rebuilding them with full accuracy: layout grids, spacing systems, transitions, hover states, and responsiveness across every breakpoint. This work sharpened the fundamentals that every project since has been built on.

```
  STACK   HTML · CSS · JavaScript
  STATUS  🟢 Ongoing — new clones added regularly
```

**What this represents:**
- 🖼️ Pixel-accurate reproductions of real product UIs
- 📐 Deep focus on layout grids, spacing logic, visual rhythm
- 📱 Every clone responsive — mobile to widescreen
- 🔎 Micro-detail obsession: hover states, transitions, typography, shadows
- 🧱 The foundation every other project is built on

[![View Work](https://img.shields.io/badge/View%20Work-GitHub-7aa2f7?style=for-the-badge&logo=github&logoColor=white&labelColor=131425)](https://github.com/SonamNarula)

---

## $ cat engineering.log

- 1000+ DSA problems solved
- 488+ LeetCode problems
- 200+ day coding streak
- Built and deployed multiple full-stack applications
- Active across GitHub, LeetCode, GFG, and Codolio

---

## $ cat github-stats.json

<div align="center">

<img src="https://github-readme-stats-sigma-five.vercel.app/api?username=SonamNarula&show_icons=true&hide_border=true&bg_color=0d0e1a&title_color=7aa2f7&icon_color=bb9af7&text_color=7aa2f7&border_radius=10&count_private=true&include_all_commits=true&rank_icon=percentile" height="165" />
&nbsp;
<img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=SonamNarula&layout=compact&hide_border=true&bg_color=0d0e1a&title_color=7aa2f7&text_color=7aa2f7&border_radius=10&langs_count=6" height="165" />
<img src="https://streak-stats.demolab.com?user=SonamNarula&theme=dark&hide_border=true&background=0d0e1a&ring=7aa2f7&fire=e0af68&currStreakLabel=7aa2f7&sideLabels=bb9af7&currStreakNum=7aa2f7&sideNums=7aa2f7&dates=565f89&border_radius=10" height="165" />

<br/><br/>

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=SonamNarula&bg_color=0d0e1a&color=7aa2f7&line=bb9af7&point=7dcfff&area=true&area_color=1a1b2e&hide_border=true&radius=6)](https://github.com/SonamNarula)

![Metrics](https://raw.githubusercontent.com/SonamNarula/SonamNarula/main/github-metrics.svg)

</div>

---

## $ grep -r "dsa" ~/grind

<div align="center">

<img src="https://leetcard.jacoblin.cool/sonamnarula2005?theme=dark&border=0&radius=8&ext=heatmap" />

<br/>

[![LeetCode](https://img.shields.io/badge/LeetCode-488%20Solved-FFA116?style=for-the-badge&logo=leetcode&logoColor=white&labelColor=131425)](https://leetcode.com/u/sonamnarula2005/)
&nbsp;
[![DSA Total](https://img.shields.io/badge/Total-1000%2B%20Problems-7aa2f7?style=for-the-badge&labelColor=131425)](https://codolio.com/profile/0PG2lf5S)

<br/>

[![GFG](https://img.shields.io/badge/GeeksForGeeks-Daily%20Solver-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white&labelColor=131425)](https://www.geeksforgeeks.org/profile/sonammnapaqc)
&nbsp;
[![Codolio](https://img.shields.io/badge/Codolio-Full%20Portfolio-bb9af7?style=for-the-badge&labelColor=131425)](https://codolio.com/profile/0PG2lf5S)

</div>

---

## $ ping sonam

<div align="center">

<a href="https://www.linkedin.com/in/sonam-narula-402a60285/">
  <img src="https://skillicons.dev/icons?i=linkedin" />
</a>
&nbsp;
<a href="https://github.com/SonamNarula">
  <img src="https://skillicons.dev/icons?i=github" />
</a>
&nbsp;
<a href="mailto:sonamnarula2108@gmail.com">
  <img src="https://skillicons.dev/icons?i=gmail" />
</a>
&nbsp;
<a href="https://codolio.com/profile/0PG2lf5S">
  <img src="https://skillicons.dev/icons?i=stackoverflow" />
</a>

</div>

---


## Contribution Arcade

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/krishrathi1/krishrathi1/output/pacman-contribution-graph-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/krishrathi1/krishrathi1/output/pacman-contribution-graph.svg">
  <img alt="Pacman contribution graph" src="https://raw.githubusercontent.com/krishrathi1/krishrathi1/output/pacman-contribution-graph.svg">
</picture>

---

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0d0e1a,50:131425,100:0d0e1a&height=100&section=footer" />

---

<br />

