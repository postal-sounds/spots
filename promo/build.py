import random, math, pathlib
random.seed(7)
W,H=1080,1350
cols=['#92ADEA','#F0CEFD','#95EA92','#91E7EB']
# map area
mx,my,mw,mh=60,330,960,620
streets=[]
for i in range(14):
    y=random.uniform(0,mh); a=random.uniform(-0.25,0.25)
    streets.append(f'<line x1="0" y1="{y:.0f}" x2="{mw}" y2="{y+a*mw:.0f}" stroke="#2A2A27" stroke-width="{random.choice([2,2,3,6])}"/>')
for i in range(16):
    x=random.uniform(0,mw); a=random.uniform(-0.3,0.3)
    streets.append(f'<line x1="{x:.0f}" y1="0" x2="{x+a*mh:.0f}" y2="{mh}" stroke="#2A2A27" stroke-width="{random.choice([2,2,3,6])}"/>')
streets.append(f'<path d="M -20 {mh*0.7} C {mw*0.3} {mh*0.55}, {mw*0.5} {mh*0.95}, {mw+20} {mh*0.62}" stroke="#1F2A2C" stroke-width="34" fill="none"/>')
dots=[]
centers=[(mw*0.3,mh*0.35),(mw*0.62,mh*0.45),(mw*0.8,mh*0.25),(mw*0.45,mh*0.75)]
for cx,cy in centers:
    for _ in range(14):
        r=abs(random.gauss(0,70)); t=random.uniform(0,6.28)
        x,y=cx+r*math.cos(t),cy+r*math.sin(t)
        if 15<x<mw-15 and 15<y<mh-15:
            dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{random.choice(cols)}" opacity="0.92"/>')
for _ in range(18):
    x,y=random.uniform(20,mw-20),random.uniform(20,mh-20)
    dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{random.choice(cols)}" opacity="0.92"/>')
# "you are here" pin
px,py=mw*0.55,mh*0.58
svg=f'''<svg width="{mw}" height="{mh}" viewBox="0 0 {mw} {mh}">{''.join(streets)}{''.join(dots)}
<circle cx="{px}" cy="{py}" r="46" fill="#BFEF2B" opacity="0.12"/>
<circle cx="{px}" cy="{py}" r="28" fill="#BFEF2B" opacity="0.22"/>
<circle cx="{px}" cy="{py}" r="14" fill="#BFEF2B" stroke="#171717" stroke-width="4"/></svg>'''
legend=''.join(f'<span><i style="background:{c}"></i>{n}</span>' for c,n in zip(cols,['Tiendas Musicales','Historias Musicales','Música en Vivo','Educación &amp; Cultura']))
html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@500;600;700&family=Atkinson+Hyperlegible+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{W}px;height:{H}px;background:#171717;color:#E2E2D8;font-family:'Jost',sans-serif;position:relative;overflow:hidden}}
.logo{{position:absolute;left:30px;top:60px;width:720px;height:144px;background:url(logo-banner.jpg) left center/cover no-repeat;
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 5%,#000 72%,transparent 90%),linear-gradient(transparent,#000 12%,#000 94%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect;}}
.kicker{{position:absolute;left:60px;top:248px;font-family:'Atkinson Hyperlegible Mono',monospace;font-size:22px;letter-spacing:.18em;text-transform:uppercase;color:#9A9A90}}
.map{{position:absolute;left:{mx}px;top:{my}px;width:{mw}px;height:{mh}px;border-radius:28px;overflow:hidden;background:#1E1E1C;box-shadow:0 0 0 1px #2C2C29}}
.card{{position:absolute;left:{mx+px-170}px;bottom:{H-(my+py)+36}px;width:340px;background:#E2E2D8;color:#232320;border-radius:16px;padding:18px 22px;font-family:'Atkinson Hyperlegible Mono',monospace;box-shadow:0 14px 30px rgba(0,0,0,.45)}}
.card:after{{content:'';position:absolute;left:50%;bottom:-12px;margin-left:-12px;border:12px solid transparent;border-bottom:0;border-top-color:#E2E2D8}}
.card b{{display:block;font-size:20px;margin-bottom:6px}}
.card p{{font-size:15px;line-height:1.4}}
.btn{{position:absolute;left:{mx+mw-84}px;top:{my+mh-84}px;width:60px;height:60px;border-radius:16px;background:#BFEF2B;display:flex;align-items:center;justify-content:center}}
.headline{{position:absolute;left:60px;top:1000px;font-weight:600;line-height:1.02}}
.headline .a{{font-size:64px;color:#E2E2D8}}
.headline .b{{font-size:96px;color:#BFEF2B;letter-spacing:-.01em}}
.legend{{position:absolute;left:60px;top:1250px;display:flex;gap:28px;font-family:'Atkinson Hyperlegible Mono',monospace;font-size:17px;color:#B5B5AB}}
.legend i{{display:inline-block;width:14px;height:14px;border-radius:50%;margin-right:9px;vertical-align:-1px}}
</style></head><body>
<div class="logo"></div>
<div class="kicker">Nuevo capítulo · Nov 2026</div>
<div class="map">{svg}</div>
<div class="card"><b>📍 Nuevo spot</b><p>Ahora formo parte del equipo de Postal Sounds, mapeando la música de la ciudad.</p></div>
<div class="btn"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#232320" stroke-width="2"><circle cx="12" cy="12" r="7"/><circle cx="12" cy="12" r="2.5" fill="#232320"/><path d="M12 1v4M12 19v4M1 12h4M19 12h4"/></svg></div>
<div class="headline"><div class="a">Ahora trabajo en</div><div class="b">postalsounds.com</div></div>
<div class="legend">{legend}</div>
</body></html>'''
pathlib.Path(__file__).with_name('anuncio.html').write_text(html)
