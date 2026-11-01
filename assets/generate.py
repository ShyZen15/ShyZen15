"""Generates every SVG used in the profile README.

Edit the data below and run:  python3 assets/generate.py
"""
from html import escape
from pathlib import Path
import textwrap

OUT = Path(__file__).parent

MONO = "'JetBrains Mono','Fira Code','SFMono-Regular',Consolas,'DejaVu Sans Mono',Menlo,monospace"
SANS = "'Inter','Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"

BG = "#0b0d14"
PANEL = "#11131d"
LINE = "#232838"
TEXT = "#e2e8f0"
MUTED = "#6b7280"
CYAN = "#7dd3fc"
VIOLET = "#c084fc"
PINK = "#f472b6"
AMBER = "#fbbf24"
GREEN = "#86efac"


def t(s):
    return escape(s, quote=False)


# --------------------------------------------------------------------------- header

LOGO = r"""
              _
      *     /  )    .
   .       |  (         *
            \__)
       /\         .
      /  \   /\
     / /\ \_/  \    /\
    / /  \  \   \__/  \
   /_/    \__\  ~   ~  \
  ~~~~~~~~~~~~~~~~~~~~~~~~
  waterloo <-> dehradun
""".strip("\n").split("\n")

INFO = [
    ("name", "Shiven Sharma"),
    ("home", "Waterloo, ON  /  Dehradun, IN"),
    ("role", "ai/ml  -  backend  -  hardware"),
    ("os", "linux  /  hyprland"),
    ("shell", "fish + starship"),
    ("editor", "neovim (astronvim)"),
    ("langs", "python  typescript  c++  lua  sql"),
    ("stack", "fastapi  supabase  postgres  react"),
    ("radio", "lora  meshtastic  esp32  arduino"),
    ("uptime", "shipping code since 2020"),
    ("now", "building quantum-larpers (shh)"),
]


def header():
    W, H = 1000, 480
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Shiven Sharma (ShyZen15): a fastfetch-style terminal introduction">')
    o.append(f"""<defs>
</defs>
<style>
  .m{{font-family:{MONO};font-size:13px;}}
  .s{{font-family:{SANS};}}
  .in{{opacity:0;animation:in .35s ease-out forwards;}}
  @keyframes in{{from{{opacity:0;transform:translateX(-6px)}}to{{opacity:1;transform:none}}}}
  .tw{{animation:tw 3s ease-in-out infinite;}}
  @keyframes tw{{0%,100%{{opacity:.15}}50%{{opacity:.9}}}}
  .ch{{fill-opacity:0;animation:ch .01s linear forwards;}}
  @keyframes ch{{to{{fill-opacity:1}}}}
  .cur{{animation:blink 1s steps(1) infinite;}}
  @keyframes blink{{50%{{fill-opacity:0}}}}
  .enso{{stroke-dasharray:100;stroke-dashoffset:100;animation:draw 2.2s cubic-bezier(.6,.1,.2,1) .3s forwards;}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  @media (prefers-reduced-motion: reduce){{.in,.enso,.ch{{animation:none;opacity:1;fill-opacity:1;stroke-dashoffset:0}}.tw,.cur{{animation:none}}}}
</style>""")
    o.append(f'<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>')

    # stars
    import random
    rnd = random.Random(15)
    for i in range(46):
        x, y = rnd.uniform(10, W - 10), rnd.uniform(44, H - 10)
        r = rnd.choice([0.7, 0.9, 1.1, 1.4])
        o.append(f'<circle class="tw" cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" style="animation-delay:{rnd.uniform(0,3):.2f}s"/>')

    # waybar
    o.append(f'<g class="m" font-size="12">')
    o.append(f'<rect x="16" y="10" width="{W-32}" height="26" rx="13" fill="{PANEL}" stroke="{LINE}"/>')
    for i, n in enumerate("12345"):
        active = n == "2"
        x = 30 + i * 26
        if active:
            o.append(f'<rect x="{x-2}" y="15" width="22" height="16" rx="8" fill="{VIOLET}"/>')
        o.append(f'<text x="{x+9}" y="27" text-anchor="middle" fill="{BG if active else MUTED}" font-weight="{700 if active else 400}">{n}</text>')
    o.append(f'<text x="{W/2}" y="27" text-anchor="middle" xml:space="preserve" fill="{TEXT}">03:14 AM  <tspan fill="{MUTED}">-</tspan>  <tspan fill="{CYAN}">night shift</tspan></text>')
    o.append(f'<text x="{W-30}" y="27" text-anchor="end" xml:space="preserve" fill="{MUTED}">cpu <tspan fill="{GREEN}">12%</tspan>   lofi <tspan fill="{PINK}">on</tspan>   caffeine <tspan fill="{AMBER}">98%</tspan></text>')
    o.append('</g>')

    # terminal window
    tx, ty, tw_, th = 24, 52, 640, 408
    o.append(f'<rect x="{tx}" y="{ty}" width="{tw_}" height="{th}" rx="14" fill="{PANEL}" stroke="#2e3446" stroke-width="1.5"/>')
    o.append(f'<g class="m">')
    py = ty + 34
    prompt = f'<tspan fill="{CYAN}" font-weight="700">shiven</tspan><tspan fill="{MUTED}"> in </tspan><tspan fill="{VIOLET}" font-weight="700">~/dev</tspan><tspan fill="{GREEN}"> ❯ </tspan>'
    typed = "".join(f'<tspan class="ch" fill="{TEXT}" style="animation-delay:{0.4 + i*0.09:.2f}s">{c}</tspan>' for i, c in enumerate("fastfetch"))
    o.append(f'<text x="{tx+20}" y="{py}" xml:space="preserve">{prompt}{typed}</text>')

    base_delay = 1.45
    ly = py + 30
    for i, line in enumerate(LOGO):
        color = AMBER if "_" in line and i < 4 else (CYAN if "~" in line or "dehradun" in line else VIOLET)
        if i in (0, 1, 2, 3):
            color = AMBER
        o.append(f'<text class="in" x="{tx+18}" y="{ly + i*20}" fill="{color}" xml:space="preserve" style="animation-delay:{base_delay + i*0.04:.2f}s">{t(line)}</text>')

    ix = tx + 248
    o.append(f'<text class="in" x="{ix}" y="{ly}" style="animation-delay:{base_delay:.2f}s"><tspan fill="{CYAN}" font-weight="700">shiven</tspan><tspan fill="{TEXT}">@</tspan><tspan fill="{VIOLET}" font-weight="700">shyzen15</tspan></text>')
    o.append(f'<text class="in" x="{ix}" y="{ly+16}" fill="{MUTED}" style="animation-delay:{base_delay:.2f}s">{"-"*15}</text>')
    for i, (k, v) in enumerate(INFO):
        y = ly + 36 + i * 21
        d = base_delay + 0.12 + i * 0.09
        o.append(f'<text class="in" x="{ix}" y="{y}" xml:space="preserve" style="animation-delay:{d:.2f}s"><tspan fill="{CYAN}" font-weight="700">{k:<8}</tspan><tspan fill="{TEXT}">{t(v)}</tspan></text>')

    # colour blocks
    cy = ly + 36 + len(INFO) * 21
    d = base_delay + 0.15 + len(INFO) * 0.09
    for i, c in enumerate(["#1f2335", "#f87171", GREEN, AMBER, CYAN, VIOLET, PINK, TEXT]):
        o.append(f'<rect class="in" x="{ix + i*24}" y="{cy-6}" width="20" height="12" rx="3" fill="{c}" style="animation-delay:{d:.2f}s"/>')

    # final prompt + cursor
    fy = ty + th - 22
    d2 = d + 0.3
    o.append(f'<text class="in" x="{tx+20}" y="{fy}" xml:space="preserve" style="animation-delay:{d2:.2f}s">{prompt}<tspan class="cur" fill="{TEXT}">\u2588</tspan></text>')
    o.append('</g>')

    # right panel: enso + name
    cx, cyy, r = 832, 226, 96
    import math
    a0, a1 = math.radians(-115), math.radians(215)
    p = lambda a, rr: (cx + rr * math.cos(a), cyy + rr * math.sin(a))
    x0, y0 = p(a0, r); x1, y1 = p(a1, r)
    o.append(f'<path class="enso" pathLength="100" d="M{x0:.1f} {y0:.1f} A{r} {r} 0 1 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{TEXT}" stroke-width="13" stroke-linecap="round" opacity=".92"/>')
    x0, y0 = p(a0 + .12, r + 6); x1, y1 = p(a1 - .25, r + 6)
    o.append(f'<path class="enso" pathLength="100" d="M{x0:.1f} {y0:.1f} A{r+6} {r+6} 0 1 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{TEXT}" stroke-width="3" stroke-linecap="round" opacity=".35" style="animation-delay:.45s"/>')
    o.append(f'<text class="s in" x="{cx}" y="{cyy+6}" text-anchor="middle" font-size="34" font-weight="800" fill="{TEXT}" letter-spacing="1" style="animation-delay:1.6s">Shy<tspan fill="{VIOLET}">Zen</tspan></text>')
    o.append(f'<text class="m in" x="{cx}" y="{cyy+30}" text-anchor="middle" font-size="12" fill="{MUTED}" letter-spacing="6" style="animation-delay:1.8s">SHIVEN</text>')
    o.append(f'<text class="m in" x="{cx}" y="{cyy+150}" text-anchor="middle" font-size="11" fill="{MUTED}" style="animation-delay:2.1s">ML  /  BACKENDS  /  RADIOS  /  RICE</text>')
    o.append('</svg>')
    return "\n".join(o)


# --------------------------------------------------------------------------- mesh divider

def mesh():
    W, H = 1000, 64
    import random
    rnd = random.Random(7)
    nodes = []
    n = 13
    for i in range(n):
        x = 30 + i * (W - 60) / (n - 1)
        y = 32 + (14 if i % 2 else -14) + rnd.uniform(-4, 4)
        nodes.append((x, y))
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="divider: a radio mesh passing packets">']
    o.append('<style>.p{animation:p 2.4s ease-in-out infinite}@keyframes p{0%,100%{opacity:.35}50%{opacity:1}}@media (prefers-reduced-motion: reduce){.p{animation:none}}</style>')
    edges = [(i, i + 1) for i in range(n - 1)] + [(i, i + 2) for i in range(0, n - 2, 3)]
    for a, b in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        o.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#8b949e" stroke-opacity=".35" stroke-width="1.2"/>')
    route = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in nodes)
    colors = [CYAN, VIOLET, PINK, AMBER]
    for i, (x, y) in enumerate(nodes):
        c = colors[i % 4]
        o.append(f'<circle class="p" cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{c}" style="animation-delay:{i*0.18:.2f}s"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="none" stroke="{c}" stroke-opacity=".25"/>')
    for k, (c, dur, begin) in enumerate([(CYAN, 6, 0), (PINK, 6, -3)]):
        o.append(f'<circle r="3" fill="{c}"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{route}"/></circle>')
    o.append('</svg>')
    return "\n".join(o)


# --------------------------------------------------------------------------- project cards

PROJECTS = [
    dict(slug="medmesh", path="~/hackathons/medmesh", tag="HACK THE VALLEY 11", title="MedMesh", accent=PINK, motif="radio",
         desc="Offline emergency network on a LoRa radio mesh. When cell towers go down, an SOS still hops node to node to a command centre that triages it, dispatches help and flags who has gone silent.",
         chips=["ESP32", "Meshtastic", "React Native", "FastAPI", "LightGBM"]),
    dict(slug="trustify", path="~/hackathons/trustify", tag="PIVOTHACKS 2026", title="Trustify", accent=GREEN, motif="shield",
         desc="A real-time \"is this legit?\" engine for students living alone for the first time. It checks rentals, job offers and YouTube claims against official data and returns a blunt risk verdict.",
         chips=["FastAPI", "Snowflake", "Chrome ext", "Vercel"]),
    dict(slug="peerproject", path="~/nonprofit/peer-project", tag="PEERPROJECT.IN", title="The Peer Project", accent=CYAN, motif="peers",
         desc="Free, student-run mentorship with r/CBSE, r/ICSE and r/JEE that pairs high schoolers with grads who walked the same path. I built the backend: auth, mentor matching, APIs.",
         chips=["FastAPI", "Supabase", "pgvector", "JWT", "LLMs"]),
    dict(slug="signlang", path="~/ml/sign-language-model", tag="COMPUTER VISION", title="Sign Language Model", accent=AMBER, motif="vision",
         desc="Reads the sign-language alphabet from a webcam with YOLO, spell-corrects the letters into words and speaks them aloud, streaming results over sockets to a Django dashboard.",
         chips=["YOLOv8/11", "OpenCV", "Django", "sockets", "TTS"]),
    dict(slug="adonis", path="~/py/adonis-transfer", tag="PYTHON  /  NETWORKING", title="Adonis Transfer", accent=VIOLET, motif="transfer",
         desc="Encrypted file transfer with a Tkinter GUI, raw socket streaming and PostgreSQL-backed accounts. The project that started my sockets obsession.",
         chips=["Python", "sockets", "PyCryptodome", "PostgreSQL"]),
    dict(slug="dotfiles", path="~/.config", tag="THE RICE", title="dotfiles-better-v2", accent=CYAN, motif="tiles",
         desc="My daily-driver Linux setup: Hyprland tiling, Waybar, rofi, fish and starship, pywal colours, Spicetify and an AstroNvim config. Pretty, and fast.",
         chips=["Hyprland", "Waybar", "fish", "Neovim", "pywal"]),
]


def motif(kind, x, y, c):
    if kind == "radio":
        rings = "".join(
            f'<circle cx="{x}" cy="{y}" r="6" fill="none" stroke="{c}" stroke-width="2">'
            f'<animate attributeName="r" values="6;34" dur="2.4s" begin="{i*0.8}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values=".9;0" dur="2.4s" begin="{i*0.8}s" repeatCount="indefinite"/></circle>'
            for i in range(3))
        return rings + f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>'
    if kind == "shield":
        return (f'<path d="M{x} {y-28} l24 9 v15 c0 16 -11 26 -24 31 c-13 -5 -24 -15 -24 -31 v-15 z" fill="{c}" fill-opacity=".12" stroke="{c}" stroke-width="2"/>'
                f'<path d="M{x-10} {y} l7 7 l14 -15" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="40" stroke-dashoffset="40">'
                f'<animate attributeName="stroke-dashoffset" values="40;0;0;40" keyTimes="0;.3;.85;1" dur="3s" repeatCount="indefinite"/></path>')
    if kind == "peers":
        return (f'<line x1="{x-22}" y1="{y+10}" x2="{x+22}" y2="{y-10}" stroke="{c}" stroke-opacity=".5" stroke-width="2" stroke-dasharray="3 4"/>'
                f'<circle cx="{x-22}" cy="{y+10}" r="9" fill="{c}" fill-opacity=".18" stroke="{c}" stroke-width="2"/>'
                f'<circle cx="{x+22}" cy="{y-10}" r="9" fill="{c}" fill-opacity=".18" stroke="{c}" stroke-width="2"/>'
                f'<circle r="3" fill="{c}"><animateMotion dur="2s" repeatCount="indefinite" path="M{x-22} {y+10} L{x+22} {y-10} L{x-22} {y+10}"/></circle>')
    if kind == "vision":
        s = 26
        br = "".join(f'<path d="M{x+dx*s} {y+dy*s-dy*10} V{y+dy*s} H{x+dx*s-dx*10}" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>'
                     for dx in (-1, 1) for dy in (-1, 1))
        return br + (f'<line x1="{x-20}" x2="{x+20}" y1="{y-20}" y2="{y-20}" stroke="{c}" stroke-opacity=".8" stroke-width="2">'
                     f'<animate attributeName="y1" values="{y-20};{y+20};{y-20}" dur="2.6s" repeatCount="indefinite"/>'
                     f'<animate attributeName="y2" values="{y-20};{y+20};{y-20}" dur="2.6s" repeatCount="indefinite"/></line>')
    if kind == "transfer":
        return (f'<path d="M{x-26} {y-8} H{x+22} m-8 -7 l8 7 l-8 7" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<path d="M{x+26} {y+12} H{x-22} m8 -7 l-8 7 l8 7" fill="none" stroke="{c}" stroke-opacity=".5" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
                f'<rect width="6" height="6" rx="1" fill="{c}" y="{y-11}"><animate attributeName="x" values="{x-26};{x+16}" dur="1.4s" repeatCount="indefinite"/></rect>')
    if kind == "tiles":
        rects = [(x - 28, y - 22, 26, 44), (x + 2, y - 22, 26, 20), (x + 2, y + 2, 26, 20)]
        out = ""
        for i, (rx, ry, w, h) in enumerate(rects):
            out += (f'<rect x="{rx}" y="{ry}" width="{w}" height="{h}" rx="4" fill="{c}" fill-opacity=".1" stroke="{c}" stroke-width="2" stroke-opacity=".35">'
                    f'<animate attributeName="stroke-opacity" values=".35;1;.35;.35" keyTimes="0;.15;.33;1" dur="3s" begin="{i}s" repeatCount="indefinite"/></rect>')
        return out
    return ""


def card(p):
    W, H = 480, 236
    c = p["accent"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(p["title"])}: {escape(p["desc"])}">']
    o.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>')
    o.append(f'<rect x="1" y="22" width="3" height="44" rx="1.5" fill="{c}"/>')
    o.append(f'<text x="22" y="34" font-family="{MONO}" font-size="12" fill="{MUTED}">{t(p["path"])}</text>')
    o.append(f'<text x="22" y="66" font-family="{SANS}" font-size="25" font-weight="800" fill="{TEXT}">{t(p["title"])}</text>')
    tag = p["tag"]
    tw = len(tag) * 6.9 + 18
    o.append(f'<rect x="22" y="78" width="{tw:.0f}" height="20" rx="10" fill="{c}" fill-opacity=".14" stroke="{c}" stroke-opacity=".5"/>')
    o.append(f'<text x="{22 + tw/2:.0f}" y="92" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" fill="{c}" letter-spacing=".5">{t(tag)}</text>')
    o.append(motif(p["motif"], W - 64, 62, c))
    for i, line in enumerate(textwrap.wrap(p["desc"], 64)[:4]):
        o.append(f'<text x="22" y="{124 + i*19}" font-family="{SANS}" font-size="13.5" fill="#cbd5e1">{t(line)}</text>')
    x = 22
    for chip in p["chips"]:
        w = len(chip) * 7.4 + 18
        o.append(f'<rect x="{x:.0f}" y="{H-36}" width="{w:.0f}" height="22" rx="6" fill="#1a1e2b" stroke="{LINE}"/>')
        o.append(f'<text x="{x + w/2:.0f}" y="{H-21}" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{TEXT}">{t(chip)}</text>')
        x += w + 8
    o.append('</svg>')
    return "\n".join(o)


# --------------------------------------------------------------------------- footer

def footer():
    W, H = 1000, 150
    prompt = f'<tspan fill="{CYAN}" font-weight="700">shiven</tspan><tspan fill="{MUTED}"> in </tspan><tspan fill="{VIOLET}" font-weight="700">~</tspan><tspan fill="{GREEN}"> ❯ </tspan>'
    lines = [
        (0.2, f'{prompt}<tspan fill="{TEXT}">sleep 8h</tspan>'),
        (0.9, f'<tspan fill="{AMBER}">fish:</tspan><tspan fill="{TEXT}"> sleep postponed until the build passes. try again at 4am.</tspan>'),
        (1.6, f'{prompt}<tspan fill="{TEXT}">git commit -m </tspan><tspan fill="{GREEN}">"it works. do not touch it."</tspan>'),
        (2.3, f'<tspan fill="{MUTED}">[main 15c0ffe] thanks for stopping by. star something, say hi.</tspan>'),
    ]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer: a late-night terminal sign-off">']
    o.append(f'<style>.in{{opacity:0;animation:in .3s ease-out forwards}}@keyframes in{{to{{opacity:1}}}}.cur{{animation:b 1s steps(1) infinite}}@keyframes b{{50%{{fill-opacity:0}}}}@media (prefers-reduced-motion: reduce){{.in{{animation:none;opacity:1}}.cur{{animation:none}}}}</style>')
    o.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>')
    o.append(f'<g font-family="{MONO}" font-size="13">')
    for i, (d, s) in enumerate(lines):
        o.append(f'<text class="in" x="24" y="{34 + i*24}" xml:space="preserve" style="animation-delay:{d}s">{s}</text>')
    o.append(f'<text class="in" x="24" y="{34 + 4*24}" xml:space="preserve" style="animation-delay:2.9s">{prompt}<tspan class="cur" fill="{TEXT}">\u2588</tspan></text>')
    o.append('</g></svg>')
    return "\n".join(o)


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header())
    (OUT / "mesh.svg").write_text(mesh())
    (OUT / "footer.svg").write_text(footer())
    for p in PROJECTS:
        (OUT / f"card-{p['slug']}.svg").write_text(card(p))
    print("wrote", sorted(f.name for f in OUT.glob("*.svg")))
