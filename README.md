<div align="center">

<img src="assets/header.svg" width="100%" alt="shiven@shyzen15: a fastfetch-style intro. AI/ML, backends, radios and a well-riced Hyprland setup, from Dehradun." />

</div>

<br/>

<p align="center">
  <b>Hey, I'm Shiven</b>, a quiet builder from the Himalayan foothills.<br/>
  I like software that keeps working when everything else stops:<br/>
  <i>SOS messages hopping over radio when the towers are down, models that read hands, backends that pair strangers who can help each other.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/based_in-Dehradun,_IN-c084fc?style=flat-square&labelColor=11131d" alt="based in Dehradun, India"/>
  <img src="https://img.shields.io/badge/focus-AI%2FML_%C2%B7_backend_%C2%B7_hardware-7dd3fc?style=flat-square&labelColor=11131d" alt="focus: AI/ML, backend, hardware"/>
  <img src="https://img.shields.io/badge/runs_on-Hyprland_%2B_Neovim-f472b6?style=flat-square&labelColor=11131d" alt="runs on Hyprland and Neovim"/>
  <img src="https://img.shields.io/badge/peak_hours-02%3A00--05%3A00-fbbf24?style=flat-square&labelColor=11131d" alt="peak hours 2am to 5am"/>
</p>

<img src="assets/mesh.svg" width="100%" alt="" />

## `❯ cat now.md`

```diff
+ building   quantum-larpers. it's brand new and it's a secret (for now)
+ shipping   the peer project backend v2: graphql, smarter AI mentor matching, docker
+ hacking    whatever the next hackathon throws at me (last two: Hack the Valley 11, PivotHacks 2026)
- sleeping   pending...
```

<img src="assets/mesh.svg" width="100%" alt="" />

## `❯ ls ~/projects --sort=love`

<p align="center">
  <a href="https://github.com/Ashmitbharti/MEDMESH-HTV"><img src="assets/card-medmesh.svg" width="49%" alt="MedMesh: an offline emergency network on a LoRa radio mesh, built at Hack the Valley 11" /></a>
  <a href="https://github.com/Erenius-Valoraen/CrowdSolution"><img src="assets/card-trustify.svg" width="49%" alt="Trustify: a real-time fact-checking and risk-rating engine for students, built at PivotHacks 2026" /></a>
  <a href="https://github.com/ShyZen15/The-Peer-Project-Backend"><img src="assets/card-peerproject.svg" width="49%" alt="The Peer Project: a free, student-run mentorship platform. I built the backend." /></a>
  <a href="https://github.com/ShyZen15/Sign-Language-Model"><img src="assets/card-signlang.svg" width="49%" alt="Sign Language Model: YOLO-based sign-alphabet recognition with speech output" /></a>
  <a href="https://github.com/ShyZen15/Adonis-Transfer"><img src="assets/card-adonis.svg" width="49%" alt="Adonis Transfer: encrypted socket file transfer with a Tkinter GUI" /></a>
  <a href="https://github.com/ShyZen15/dotfiles-better-v2"><img src="assets/card-dotfiles.svg" width="49%" alt="dotfiles-better-v2: my Hyprland, Waybar, fish and AstroNvim rice" /></a>
</p>

<details>
<summary><b>🔌 &nbsp;open the hardware drawer</b> &nbsp;<sub>(things with wires, sensors and questionable soldering)</sub></summary>
<br/>

| build | what it does |
|---|---|
| **MedMesh node** | Heltec WiFi LoRa 32 V3 boards running Meshtastic, plus an ESP32 SOS button you have to hold for 3 seconds (let go early and it cancels) |
| **EMF Detector** | An Arduino device that detects electromagnetic fields, with custom ML on top to make sense of the readings |
| **Driver Safety Device** | Hardware sensors and an ML model that watch a driver's alertness and step in before it becomes a crash |
| **Caristification** | An AI chatbot that suggests cars to fit your lifestyle and previews modifications before you make them |
| **Video Meeting App** | An accessible video-call platform designed for people of determination |

</details>

<img src="assets/mesh.svg" width="100%" alt="" />

## `❯ cat stack.toml`

<table>
<tr>
<td width="160"><code>[languages]</code></td>
<td><img src="https://skillicons.dev/icons?i=py,ts,js,cpp,lua,postgres&perline=12" alt="Python, TypeScript, JavaScript, C++, Lua, SQL"/></td>
</tr>
<tr>
<td><code>[backend]</code></td>
<td><img src="https://skillicons.dev/icons?i=fastapi,django,supabase,postgres,vercel,docker&perline=12" alt="FastAPI, Django, Supabase, PostgreSQL, Vercel, Docker"/></td>
</tr>
<tr>
<td><code>[frontend]</code></td>
<td><img src="https://skillicons.dev/icons?i=react,tailwind,vite,html,css&perline=12" alt="React and React Native, Tailwind, Vite, HTML, CSS"/></td>
</tr>
<tr>
<td><code>[ml.vision]</code></td>
<td><img src="https://skillicons.dev/icons?i=sklearn,opencv,pytorch&perline=12" alt="scikit-learn, OpenCV, PyTorch (YOLO via Ultralytics)"/> &nbsp;<sub>+ LightGBM · XGBoost · YOLOv8/11 · pgvector · Hugging Face</sub></td>
</tr>
<tr>
<td><code>[hardware]</code></td>
<td><img src="https://skillicons.dev/icons?i=arduino,raspberrypi&perline=12" alt="Arduino, Raspberry Pi"/> &nbsp;<sub>+ ESP32 · LoRa · Meshtastic · sensors that occasionally catch fire</sub></td>
</tr>
<tr>
<td><code>[daily.driver]</code></td>
<td><img src="https://skillicons.dev/icons?i=linux,neovim,git,github&perline=12" alt="Linux, Neovim, Git, GitHub"/> &nbsp;<sub>+ Hyprland · Waybar · fish · starship · pywal</sub></td>
</tr>
</table>

<img src="assets/mesh.svg" width="100%" alt="" />

## `❯ man shiven`

```text
SHIVEN(1)                       User Commands                       SHIVEN(1)

NAME
       shiven - turns caffeine, hackathon deadlines and LoRa packets into
                working software

SYNOPSIS
       shiven [--build] [--rice] [--ship-at-4am] <idea>

DESCRIPTION
       Writes Python first, asks questions later. Connects hardware to models
       to people. Will rewrite your dotfiles if left unattended.

OPTIONS
       --sockets      falls back to raw sockets whenever a library feels too
                      easy (see: adonis-transfer)
       --mesh         keeps messages moving when the network is down
       --mentor       matches students with people who walked the same path

BUGS
       Thinks "one more feature" before every deadline. Has never once been
       right about that.

SEE ALSO
       peerproject.in(1), devpost.com/software/medmesh(1)
```

<img src="assets/mesh.svg" width="100%" alt="" />

## `❯ ping shiven`

<p align="center">
  <a href="https://github.com/ShyZen15"><img src="https://img.shields.io/badge/GitHub-ShyZen15-c084fc?style=for-the-badge&logo=github&logoColor=white&labelColor=11131d" alt="GitHub: ShyZen15"/></a>
  <a href="https://peerproject.in"><img src="https://img.shields.io/badge/The_Peer_Project-peerproject.in-7dd3fc?style=for-the-badge&logo=googlechrome&logoColor=white&labelColor=11131d" alt="The Peer Project website"/></a>
  <a href="https://devpost.com/software/medmesh"><img src="https://img.shields.io/badge/Devpost-MedMesh-f472b6?style=for-the-badge&logo=devpost&logoColor=white&labelColor=11131d" alt="MedMesh on Devpost"/></a>
  <!-- add yours:
  <a href="https://linkedin.com/in/YOUR-HANDLE"><img src="https://img.shields.io/badge/LinkedIn-say_hi-fbbf24?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=11131d" alt="LinkedIn"/></a>
  -->
</p>

<p align="center"><sub>open to hackathon teams, open-source collabs, and anything involving radios, models, or both.</sub></p>

<br/>

<div align="center">
<img src="assets/footer.svg" width="100%" alt="shiven ❯ sleep 8h. fish: sleep postponed until the build passes. Thanks for stopping by." />
</div>

<!-- every SVG in /assets is generated: edit assets/generate.py, then run `python3 assets/generate.py` -->
