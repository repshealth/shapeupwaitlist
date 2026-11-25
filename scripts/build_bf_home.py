"""Build the Black Friday homepage from the standard homepage (homepage-standard.html).

Writes index.html (the live homepage during the sale) and black-friday-sale.html (same page).
After the sale, restore the normal homepage with:  cp homepage-standard.html index.html

Run from the repo root:  python3 scripts/build_bf_home.py
Edit the OFFER / END / CHECKOUT values below, then rebuild.
"""
import re

END = '2026-12-01T00:00:00Z'          # countdown end: midnight at the end of Cyber Monday (30 Nov, UK time)
CHECKOUT_ANNUAL = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership-2/yearly'
CHECKOUT_QUARTER = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership-2/3-month'

src = open('homepage-standard.html').read()
t = src
t = t.replace('<meta name="robots" content="noindex">\n', '')  # the standard copy is noindex; the live homepage must not be


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (a[:80], t.count(a))
    t = t.replace(a, b)


def cut(start, end_marker, new):
    """Replace from `start` up to (not including) `end_marker`."""
    global t
    s = t.index(start)
    e = t.index(end_marker, s)
    t = t[:s] + new + t[e:]


TIMER = '''<div class="bf-timer" data-cd role="timer" aria-label="Time left on the Black Friday offer">
  <div><b class="d">00</b><span>Days</span></div><i>:</i>
  <div><b class="h">00</b><span>Hours</span></div><i>:</i>
  <div><b class="m">00</b><span>Mins</span></div><i>:</i>
  <div><b class="s">00</b><span>Secs</span></div>
</div>'''

# ---------- head ----------
t = re.sub(r'<title>[^<]*</title>', '<title>Black Friday: 60% Off Annual Membership | Shape Up with Gabby</title>', t, count=1)
t = re.sub(r'<meta name="description" content="[^"]*">',
           '<meta name="description" content="Black Friday at Shape Up with Gabby: the annual Lifetime Team membership is 60% off at £119.99 a year, about 33p a day. Quarterly is £49.99. Ends Cyber Monday.">', t, count=1)

CSS = '''
/* ===== BLACK FRIDAY LAYER ===== */
:root{--bf-ink:#0d0d0d;--bf-ink2:#1a1a1a}
.bf-bar{display:flex;align-items:center;justify-content:center;gap:28px;flex-wrap:wrap;background:var(--su-yellow);color:var(--bf-ink);margin:-12px -24px 12px;padding:11px 16px;font-family:var(--su-head);font-size:16px;font-weight:600;letter-spacing:1px;text-transform:uppercase}
.bf-bar .cd{font-variant-numeric:tabular-nums;font-weight:700}
.bf-bar a{color:var(--bf-ink);text-decoration:none;font-weight:700}
.bf-hero{position:relative;overflow:hidden;color:#fff;padding:190px 0 140px;background:radial-gradient(42% 60% at 74% 48%,rgba(253,224,141,.10) 0%,rgba(253,224,141,0) 70%),var(--bf-ink);clip-path:polygon(0 0,100% 0,100% calc(100% - 5.3vw - 40px),0 calc(100% - 40px))}
.su-ticker.bf-ticker{margin-top:-128px;height:110px;margin-bottom:-24px;z-index:5}
.bf-ticker .su-ticker-band{background:var(--su-yellow)}
.bf-ticker .su-ticker-track span,.bf-ticker .su-ticker-track b,.bf-ticker .su-ticker-track .spark{color:var(--bf-ink)}

/* Hero: clean editorial layout */
.bf-hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:end}
.bf-copy{padding-bottom:120px}
.bf-kicker{display:flex;align-items:center;gap:10px;margin:0 0 26px;font-size:12px;font-weight:600;letter-spacing:2.2px;text-transform:uppercase;color:rgba(255,255,255,.75)}
.bf-kicker b{color:var(--su-yellow);font-weight:700}
.bf-kicker span{color:rgba(255,255,255,.3);font-weight:400}
.bf-hero .lead s{color:rgba(255,255,255,.4);margin-left:4px}
.bf-hero .lead strong{color:#fff}
.bf-hero h1{font-family:var(--su-head);text-transform:uppercase;margin:0 0 36px;font-weight:700;line-height:.9;letter-spacing:-.5px}
.bf-hero h1 .l1{display:block;font-size:clamp(56px,6vw,92px);color:var(--su-yellow);max-width:9.5em}
.bf-hero h1 .l2{display:block;font-size:clamp(30px,3.4vw,50px);font-weight:400;color:#fff;letter-spacing:0;margin-top:6px}
.bf-hero .lead{font-size:17px;line-height:1.6;color:rgba(255,255,255,.72);max-width:460px;margin:0 0 36px}
.bf-price{display:flex;align-items:flex-end;gap:16px;margin:0 0 30px}
.bf-price b{font-family:var(--su-head);font-size:64px;line-height:.85;font-weight:700;color:#fff}
.bf-price div{display:flex;flex-direction:column;gap:4px;font-size:13px;color:rgba(255,255,255,.65)}
.bf-price s{font-size:15px;color:rgba(255,255,255,.45)}
.bf-timer{display:inline-flex;align-items:flex-start;gap:18px;font-family:var(--su-head);margin:0 0 34px}
.bf-timer>div{display:flex;flex-direction:column;align-items:flex-start;min-width:48px}
.bf-timer b{font-size:34px;line-height:1;font-weight:500;color:#fff;font-variant-numeric:tabular-nums}
.bf-timer span{font-family:var(--su-text);font-size:10px;font-weight:600;letter-spacing:1.6px;text-transform:uppercase;color:rgba(255,255,255,.45);margin-top:6px}
.bf-timer i{font-style:normal;font-size:26px;line-height:1.1;color:rgba(255,255,255,.25)}
.bf-timer.ended b{color:rgba(255,255,255,.5)}
.bf-ctas{display:flex;align-items:center;gap:26px;flex-wrap:wrap}
.bf-btn{background:var(--su-yellow);color:var(--bf-ink);padding:18px 38px}
.bf-link{color:#fff;font-size:13px;font-weight:600;letter-spacing:1px;text-transform:uppercase;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.4);padding-bottom:3px}
.bf-link:hover{border-color:var(--su-yellow)}
.bf-art{position:relative;height:660px;margin-bottom:-60px}
.bf-art .gabby{position:absolute;left:50%;bottom:0;height:100%;width:auto;max-width:none;transform:translateX(-50%);-webkit-mask-image:linear-gradient(180deg,#000 84%,transparent 100%);mask-image:linear-gradient(180deg,#000 84%,transparent 100%)}
.bf-strip .bf-timer{margin:0;gap:14px}
.bf-strip .bf-timer b{font-size:26px}
.bf-pricing .bf-timer{justify-content:center}
.bf-pricing .bf-timer>div,.bf-final .bf-timer>div{align-items:center}
.bf-final .bf-timer span{color:rgba(255,255,255,.8)}
.bf-final .bf-timer i{color:rgba(255,255,255,.5)}

.bf-pricing{background:var(--bf-ink);color:#fff;padding:90px 0 100px;text-align:center}
.bf-pricing .su-eyebrow{color:var(--su-yellow)}
.bf-pricing .su-h2 strong{color:var(--su-yellow)}
.bf-excl{display:inline-block;margin:0 0 18px;background:var(--su-yellow);color:var(--bf-ink);font-family:var(--su-head);font-size:20px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:8px 18px;border-radius:6px}
.bf-big{font-family:var(--su-head);text-transform:uppercase;font-weight:700;line-height:.88;letter-spacing:-1px;margin:0 0 22px;font-size:clamp(64px,9vw,140px);color:#fff}
.bf-big strong{color:var(--su-yellow);font-weight:700}
@media (max-width:640px){.bf-excl{font-size:16px}.bf-big{font-size:clamp(52px,16vw,76px)}}
.bf-pricing .lede{max-width:560px;margin:0 auto 22px;color:rgba(255,255,255,.8)}
.bf-plans{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;max-width:920px;margin:30px auto 0;text-align:left;align-items:stretch}
.bf-plan{position:relative;background:var(--bf-ink2);border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:30px 28px;display:flex;flex-direction:column}
.bf-plan--main{background:var(--su-yellow);color:var(--bf-ink);border-color:var(--su-yellow);box-shadow:0 0 0 6px rgba(253,224,141,.15),0 30px 60px rgba(0,0,0,.4)}
.bf-plan .flag{position:absolute;top:-14px;left:50%;transform:translateX(-50%);white-space:nowrap;background:var(--bf-ink);color:var(--su-yellow);border:2px solid var(--su-yellow);border-radius:999px;padding:5px 14px;font-size:10.5px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase}
.bf-plan .term{font-size:11px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;opacity:.75}
.bf-plan h3{font-family:var(--su-head);text-transform:uppercase;font-size:30px;line-height:1;margin:6px 0 14px}
.bf-plan .price{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.bf-plan .price b{font-family:var(--su-head);font-size:64px;line-height:.9}
.bf-plan .price s{font-size:20px;font-weight:600;opacity:.55}
.bf-plan .price span{font-size:13px;font-weight:600}
.bf-plan .save{display:inline-block;align-self:flex-start;margin:12px 0 16px;border-radius:999px;padding:6px 12px;font-size:11.5px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;background:var(--bf-ink);color:var(--su-yellow)}
.bf-plan:not(.bf-plan--main) .save{background:rgba(253,224,141,.15);color:var(--su-yellow)}
.bf-plan ul{list-style:none;margin:0 0 22px;padding:0;display:grid;gap:9px;font-size:14px}
.bf-plan li{display:flex;gap:10px;align-items:flex-start}
.bf-plan li::before{content:"";flex:none;width:18px;height:18px;margin-top:2px;border-radius:50%;background:var(--bf-ink) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%23FDE08D' stroke-width='3'/%3E%3C/svg%3E") center/12px no-repeat}
.bf-plan:not(.bf-plan--main) li::before{background-color:rgba(255,255,255,.12)}
.bf-plan .su-btn{margin-top:auto;width:100%}
.bf-plan--main .su-btn{background:var(--bf-ink);color:#fff}
.bf-plan:not(.bf-plan--main) .su-btn{background:#fff;color:var(--bf-ink)}
.bf-plan small{display:block;text-align:center;margin-top:10px;font-size:11.5px;opacity:.7}
.bf-pricing .su-ticks{justify-content:center;color:rgba(255,255,255,.8);margin-top:26px}

.bf-strip{background:var(--bf-ink);color:#fff;padding:26px 0}
.bf-strip .su-wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap}
.bf-strip p{margin:0;font-family:var(--su-head);text-transform:uppercase;font-size:clamp(20px,2vw,26px);line-height:1.05}
@media (min-width:901px){.bf-strip .su-wrap{flex-wrap:nowrap}.bf-strip .su-btn{flex:none}}
.bf-strip p b{color:var(--su-yellow)}

.bf-final{text-align:center}
.bf-final .su-h2{color:#fff}
.bf-final p{max-width:560px;margin:0 auto 22px;color:#fff}
.bf-final .su-btn{background:var(--bf-ink);color:#fff}

.bf-toast{position:fixed;left:18px;bottom:18px;z-index:70;display:flex;align-items:center;gap:12px;max-width:340px;background:#fff;color:var(--bf-ink);border-radius:14px;padding:12px 36px 12px 12px;box-shadow:0 14px 40px rgba(0,0,0,.25);border-left:5px solid var(--su-yellow);transform:translateY(160%);opacity:0;transition:transform .45s ease,opacity .45s ease;font-size:13px;line-height:1.35}
.bf-toast.show{transform:none;opacity:1}
.bf-toast .ic{flex:none;width:38px;height:38px;border-radius:10px;background:var(--bf-ink);color:var(--su-yellow);display:grid;place-items:center;font-size:18px}
.bf-toast b{display:block;font-size:13.5px}
.bf-toast small{display:block;color:#666;font-size:11.5px;margin-top:2px;font-variant-numeric:tabular-nums}
.bf-toast button{position:absolute;top:6px;right:8px;border:0;background:none;font-size:16px;line-height:1;color:#999;cursor:pointer;padding:4px}
.bf-buybar{display:none}
@media (max-width:1100px){
  .bf-hero{padding-top:160px;text-align:center}
  .bf-hero-grid{grid-template-columns:1fr;gap:0}
  .bf-copy{padding-bottom:0;max-width:680px;margin:0 auto;width:100%}
  .bf-hero h1 .l1{max-width:none}
  .bf-hero h1{text-align:center}
  .bf-kicker,.bf-price,.bf-ctas{justify-content:center}
  .bf-hero .lead{margin:0 auto 30px}
  .bf-art{height:560px;max-width:480px;width:100%;margin:50px auto -50px}
}
@media (max-width:900px){
  .bf-hero{padding-top:150px}
  .bf-art{height:480px;max-width:420px;margin:40px auto -50px}
  .bf-plans{grid-template-columns:1fr 1fr;gap:16px}
  .bf-plan{padding:28px 22px}
  .bf-plan .price b{font-size:50px}
  .bf-strip .su-wrap{justify-content:center;text-align:center}
}
@media (max-width:640px){
  .bf-plans{grid-template-columns:1fr}
  .bf-hero{padding-top:140px}
  .bf-hero h1 .l1{font-size:clamp(42px,12.5vw,60px);max-width:none}
  .bf-kicker{flex-wrap:wrap;justify-content:center;gap:6px 10px;font-size:11px;letter-spacing:1.6px}
  .bf-hero h1 .l2{font-size:clamp(24px,7.4vw,34px)}
  .bf-price b{font-size:54px}
  .bf-timer{gap:12px}
  .bf-timer b{font-size:28px}
  .bf-timer i{font-size:22px}
  .bf-ctas{flex-direction:column;gap:18px}
  .bf-ctas .su-btn{width:100%}
  .bf-art{height:400px}
  .bf-bar{margin:-10px -12px 10px;font-size:13px;gap:4px 12px;padding:8px 10px}
  .bf-bar a{display:none}
  .bf-plan{padding:28px 20px}
  .bf-plan .price b{font-size:54px}
  .bf-toast{left:10px;right:10px;max-width:none;bottom:84px}
  .bf-buybar{display:flex;position:fixed;left:10px;right:10px;bottom:10px;z-index:60;align-items:center;justify-content:space-between;gap:10px;background:var(--bf-ink);color:#fff;border-radius:18px;padding:10px 10px 10px 16px;box-shadow:0 12px 30px rgba(0,0,0,.35);transform:translateY(140%);transition:transform .3s ease}
  .bf-buybar.show{transform:none}
  .bf-buybar b{display:block;font-size:13px}
  .bf-buybar span{font-size:11px;color:var(--su-yellow);font-variant-numeric:tabular-nums}
  .bf-buybar .su-btn{width:auto;display:inline-flex;padding:12px 16px;background:var(--su-yellow);color:var(--bf-ink);font-size:11.5px}
}
@media (prefers-reduced-motion:reduce){.bf-toast{transition:none}}

/* ===== BRAND (light) THEME: overrides the dark Black Friday styles ===== */
@keyframes bfPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.04)}}
@keyframes bfDot{0%{box-shadow:0 0 0 0 rgba(98,186,245,.7)}70%{box-shadow:0 0 0 10px rgba(98,186,245,0)}100%{box-shadow:0 0 0 0 rgba(98,186,245,0)}}
@keyframes bfShine{0%{transform:translateX(-120%) skewX(-20deg)}60%,100%{transform:translateX(320%) skewX(-20deg)}}
@keyframes bfSpinBorder{to{--bf-a:360deg}}
@keyframes bfWiggle{0%,92%,100%{transform:rotate(-8deg) scale(1)}95%{transform:rotate(4deg) scale(1.08)}}
@keyframes bfFloat{0%,100%{translate:0 0}50%{translate:0 -8px}}
@property --bf-a{syntax:'<angle>';inherits:false;initial-value:0deg}

.bf-pill{display:inline-flex;align-items:center;gap:10px;background:var(--su-ink);color:#fff;border-radius:999px;padding:9px 18px 9px 14px;font-size:12px;font-weight:600;letter-spacing:1px;text-transform:uppercase;text-decoration:none;margin-top:8px}
.bf-pill b{color:var(--su-yellow);font-weight:700}
.bf-pill .dot{width:9px;height:9px;border-radius:50%;background:var(--su-blue);animation:bfDot 1.8s infinite}
.bf-lhero h1 .bf-hl{position:relative;display:inline-block;z-index:0}
.bf-lhero h1 .bf-hl::after{content:"";position:absolute;left:-4px;right:-4px;bottom:4px;height:38%;background:var(--su-yellow);z-index:-1;border-radius:4px}
.bf-shine{position:relative;overflow:hidden}
.bf-shine::after{content:"";position:absolute;top:0;bottom:0;left:0;width:40%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.55),transparent);animation:bfShine 3.2s ease-in-out infinite}
.bf-burst{position:absolute;z-index:4;right:4%;bottom:90px;width:118px;height:118px;border-radius:50%;background:var(--su-ink);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:var(--su-head);text-transform:uppercase;font-size:14px;line-height:1;letter-spacing:1px;box-shadow:0 0 0 6px var(--su-yellow),0 18px 40px rgba(0,0,0,.2);animation:bfWiggle 4s ease-in-out infinite}
.bf-burst b{font-size:40px;color:var(--su-yellow);font-weight:700}


.bf-pricing{background:linear-gradient(180deg,#fff 0%,var(--su-cream) 18%,var(--su-cream) 82%,#fff 100%);color:var(--su-ink);padding:90px 0 100px}
.bf-excl{background:var(--su-ink);color:var(--su-yellow);animation:bfPulse 2.4s ease-in-out infinite}
.bf-big{color:var(--su-ink)}
.bf-big strong{color:var(--su-blue)}
.bf-pricing .lede{color:var(--su-body)}
.bf-pricing .bf-timer b{color:var(--su-ink)}
.bf-pricing .bf-timer span{color:var(--su-muted)}
.bf-pricing .bf-timer i{color:rgba(0,0,0,.2)}
.bf-pricing .bf-timer>div{background:#fff;border:1px solid rgba(0,0,0,.08);border-radius:14px;padding:10px 12px 8px;min-width:64px;box-shadow:0 6px 16px rgba(0,0,0,.05)}

.bf-plans{align-items:center}
.bf-plan{background:#fff;color:var(--su-ink);border:1px solid rgba(0,0,0,.1);box-shadow:0 10px 30px rgba(0,0,0,.06)}
.bf-plan:not(.bf-plan--main) .save{background:var(--su-blue-soft);color:var(--su-ink)}
.bf-plan:not(.bf-plan--main) li::before{background-color:var(--su-blue)}
.bf-plan:not(.bf-plan--main) .su-btn{background:var(--su-ink);color:#fff}
.bf-plan small{color:var(--su-muted);opacity:1}

/* the hero card: animated border, ribbon, gentle lift */
.bf-plan--main{border:4px solid transparent;padding:38px 30px 30px;transform:scale(1.03);
  background:linear-gradient(var(--su-yellow),var(--su-yellow)) padding-box,conic-gradient(from var(--bf-a),var(--su-blue),var(--su-ink),var(--su-yellow),var(--su-blue),var(--su-ink),var(--su-blue)) border-box;
  animation:bfSpinBorder 4s linear infinite,bfFloat 5s ease-in-out infinite;
  box-shadow:0 30px 60px rgba(98,186,245,.28),0 10px 24px rgba(0,0,0,.08)}
.bf-plan--main .flag{background:var(--su-blue);color:#fff;border-color:#fff}
.bf-plan--main .price b{animation:bfPulse 2.4s ease-in-out infinite;display:inline-block;transform-origin:left bottom}
.bf-plan--main .save{background:var(--su-ink);color:var(--su-yellow)}
.bf-ribbon{position:absolute;top:20px;right:-38px;transform:rotate(38deg);background:var(--su-ink);color:var(--su-yellow);font-family:var(--su-head);font-size:12px;letter-spacing:1.5px;text-transform:uppercase;padding:5px 40px;overflow:hidden}
.bf-plan--main{overflow:visible}
.bf-plan--main .bf-ribbon-wrap{position:absolute;inset:0;overflow:hidden;border-radius:24px;pointer-events:none}

.bf-strip{background:var(--su-blue);color:#fff}
.bf-strip p b{color:var(--su-ink)}
.bf-strip .bf-timer b{color:#fff}
.bf-strip .bf-timer span{color:rgba(255,255,255,.8)}
.bf-strip .bf-timer i{color:rgba(255,255,255,.5)}
.bf-strip .bf-btn{background:var(--su-yellow);color:var(--su-ink)}
.bf-final .su-btn{background:var(--su-ink);color:#fff}
.bf-buybar{background:var(--su-ink)}

@media (max-width:900px){
  .bf-plan--main{transform:none}
  .bf-burst{width:92px;height:92px;bottom:60px;right:0}
  .bf-burst b{font-size:30px}
}
@media (max-width:640px){
  .bf-burst{width:80px;height:80px;font-size:11px;bottom:40px}
  .bf-burst b{font-size:26px}
  .bf-pill{font-size:10.5px;padding:8px 14px 8px 12px}
  .bf-pricing .bf-timer>div{min-width:54px;padding:8px 6px}
}
@media (prefers-reduced-motion:reduce){.bf-plan--main,.bf-plan--main .price b,.bf-excl,.bf-burst,.bf-shine::after,.bf-pill .dot{animation:none}}
'''
i = t.index('</style>')
t = t[:i] + CSS + t[i:]

# ---------- header: announcement bar + CTA ----------
rep('<header class="su-header">\n  <nav class="su-nav" aria-label="Main">',
    '<header class="su-header">\n  <div class="bf-bar"><span class="t">Black Friday · Up to 60% off</span><span class="cdw">Ends in <span class="cd" data-cd-text>--</span></span><a href="#pricing">Claim it →</a></div>\n  <nav class="su-nav" aria-label="Main">')
rep('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>\n      <button class="su-burger"',
    '<a class="su-btn su-btn--yellow" href="#pricing">Get 60% off</a>\n      <button class="su-burger"')

# ---------- hero ----------
HERO = f'''<!-- ===== HERO (Black Friday, brand colours) ===== -->
<section class="su-hero bf-lhero" id="top">
  <div class="su-wrap su-hero-grid">
    <div>
      <a class="bf-pill" href="#pricing"><span class="dot" aria-hidden="true"></span><b>Black Friday</b> Up to 60% off</a>
      <h1>Shape Up's biggest<br><span class="bf-hl">ever sale.</span></h1>
      <p class="lead">Up to 60% off memberships. Training, nutrition and 12,400 women training alongside you, in one app.</p>
      <div class="su-hero-ctas">
        <a class="su-btn su-btn--blue bf-shine" href="{CHECKOUT_ANNUAL}">Claim 60% off</a>
        <a class="su-btn su-btn--outline" href="#inside">See what's inside <span aria-hidden="true">↓</span></a>
      </div>
      <div class="su-hero-note">Black Friday prices end Cyber Monday</div>
    </div>
    <div class="su-hero-art">
      <img class="su-hero-gabby" src="images/img-10.webp" alt="Gabby, founder of Shape Up">
      <div class="su-phone su-hero-phone2"><img src="images/img-11.webp" alt="Shape Up meal plan screen"></div>
      <div class="su-phone su-hero-phone1"><img src="images/img-12.webp" alt="Shape Up workout tracker screen"></div>
      <div class="bf-burst" aria-hidden="true"><b>60%</b>off</div>
    </div>
  </div>
  <div class="su-ticker" aria-hidden="true">
    <div class="su-ticker-band">
      <div class="su-ticker-track">
        {''.join('<span><b>Black Friday</b></span><span class="spark">✦</span><span><b>Up to 60%</b> off</span><span class="spark">✦</span><span><b>£119.99</b> a year</span><span class="spark">✦</span><span><b>33p</b> a day</span><span class="spark">✦</span><span><b>Ends</b> Cyber Monday</span><span class="spark">✦</span>' for _ in range(2))}
      </div>
    </div>
  </div>
</section>

'''
cut('<!-- ===== HERO ===== -->', '<!-- ===== WHAT SHAPE UP IS ===== -->', HERO)

rep('<p class="su-eyebrow">What Shape Up is</p>\n', '')
rep('<h2 class="su-h2">Every programme<strong>included</strong></h2>', '<h2 class="su-h2">Every programme &amp; challenge<strong>included</strong></h2>')
rep('<h2 class="su-h2">Everything you need,<strong>right there in your pocket.</strong></h2>', '<h2 class="su-h2">Everything you need<strong>to transform your body.</strong></h2>')
rep('      <div class="note">Level 3 PT &amp; nutrition coach, coaching women for 6 years</div>\n', '')
# remove the "Your health and fitness best friend" section (review comment)
_s = t.index('<!-- ===== WHAT SHAPE UP IS ===== -->')
_e = t.index('<!-- ===== FEATURES ===== -->', _s)
t = t[:_s] + t[_e:]
# app feature pills (review comments)
t = t.replace('<i aria-hidden="true">🥗</i>Meal Plan System</span>', '<i aria-hidden="true">🥗</i>Custom Meal Plans &amp; Recipes</span>')
t = t.replace('<i aria-hidden="true">📋</i>Check-In System</span>', '<i aria-hidden="true">📋</i>Progress Reviews</span>')
t, _n = re.subn(r'<span class="su-pill"><i aria-hidden="true">[^<]*</i>Injury System</span>', '', t)
assert _n >= 1, _n
rep('      <p class="su-intro">This is the first full programme built inside the new app, and honestly that\'s the bit I\'m most excited about.</p>\n', '')

# remove the "Everything. One price." section (review comment); the app section takes over the #inside anchor
_s = t.index('<!-- ===== FEATURES ===== -->')  # includes the wave above the section
_e = t.index('<!-- ===== INSIDE THE APP ===== -->', _s)
t = t[:_s] + t[_e:]
rep('<!-- ===== INSIDE THE APP ===== -->\n<section class="su-app">', '<!-- ===== INSIDE THE APP ===== -->\n<section class="su-app" id="inside">')
_s = t.index("  // What's inside: desktop accordion + mobile tabs/swipe share one state")
_e = t.index("  var tf=document.getElementById('suTfTrack')", _s)
t = t[:_s] + t[_e:]

# remove the "Inside the app" section (review); links that pointed at it now go to the programmes
_s = t.index('<!-- ===== INSIDE THE APP ===== -->')
_e = t.index('<!-- ===== PRICING', _s)
t = t[:_s] + t[_e:]
t = t.replace('<li><a href="#inside">What\'s Inside</a></li>', '<li><a href="#programmes">What\'s Inside</a></li>')
t = t.replace('<a href="#inside">What\'s Inside</a>', '<a href="#programmes">What\'s Inside</a>')
t = t.replace('href="#inside">See what\'s inside', 'href="#programmes">See what\'s inside')
t = t.replace('<li><a href="#inside">What\'s inside</a></li><li><a href="#inside">Inside the app</a></li>', '<li><a href="#programmes">What\'s inside</a></li>')
assert 'href="#inside"' not in t, re.findall(r'.{60}href="#inside".{40}', t)

# ---------- price mentions elsewhere ----------
rep('<p>All of these, plus every new programme we add, for <b>£24.99</b> a month.</p>',
    '<p>All of these, plus every new programme we add, for <b>£119.99</b> a year this Black Friday.</p>')

# ---------- pricing ----------
PRICING = f'''<!-- ===== PRICING (Black Friday) ===== -->
<section class="bf-pricing" id="pricing">
  <div class="su-wrap">
    <p class="bf-excl">Exclusive offer</p>
    <h2 class="bf-big">Up to<br><strong>60% off</strong></h2>
    <p class="lede">When the timer hits zero, prices go back to normal.</p>
    {TIMER}
    <div class="bf-plans">
      <article class="bf-plan bf-plan--main">
        <span class="bf-ribbon-wrap" aria-hidden="true"><span class="bf-ribbon">Black Friday</span></span>
        <span class="flag">Best value</span>
        <h3>Annual Membership</h3>
        <div class="price"><s>£299.88</s><b>£119.99</b><span>a year</span></div>
        <span class="save">60% off · about 33p a day</span>
        <ul>
          <li>Every Shape Up programme, including Island Body V2 and Strength Is Power</li>
          <li>Custom workouts from Gabby &amp; the Shape Up team</li>
          <li>Meal plans, barcode scanner and calorie tracking</li>
          <li>Cycle and habit tracking, plus the community</li>
          <li>Access to all of Gabby's new programmes &amp; challenges</li>
        </ul>
        <a class="su-btn bf-shine" href="{CHECKOUT_ANNUAL}">Get 60% off</a>
        <small>60% less than 12 months at £24.99</small>
      </article>
      <article class="bf-plan">
        <span class="term">Quarterly</span>
        <h3>3 months</h3>
        <div class="price"><s>£64.99</s><b>£49.99</b><span>every 3 months</span></div>
        <span class="save">Save £15 every quarter</span>
        <ul>
          <li>The full Shape Up app, same as annual</li>
          <li>Every programme and meal plan</li>
          <li>About 55p a day</li>
        </ul>
        <a class="su-btn" href="{CHECKOUT_QUARTER}">Get quarterly</a>
        <small>Billed £49.99 every 3 months</small>
      </article>
    </div>
  </div>
</section>

'''
s = t.index('<!-- ===== PRICING ===== -->')
e = t.index('<!-- ===== PROGRAMMES', s)
t = t[:s] + PRICING + t[e:]

# ---------- mid-page strip before results ----------
STRIP = f'''<div class="bf-strip">
  <div class="su-wrap">
    <p><b>Black Friday</b> · 60% off</p>
    {TIMER}
    <a class="su-btn bf-btn" href="#pricing">Claim 60% off</a>
  </div>
</div>

'''
rep('<!-- ===== RESULTS ===== -->', STRIP + '<!-- ===== RESULTS ===== -->')

# ---------- remove one-off programme exits ----------
t, n = re.subn(r'\n\s*<span class="su-pcard-more">See programme →</span>\n\s*<a class="su-pcard-link"[^>]*></a>', '', t)
assert n == 7, n
rep('    <div class="su-oneoff-btn"><a class="su-btn su-btn--outline" href="one-off-programmes.html">Buy a one off programme</a></div>\n', '')
cs = t.index('<div class="su-compare">')
a = t.index('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>', cs)
t = t[:a] + '<a class="su-btn su-btn--yellow" href="#pricing">Claim 60% off</a>' + t[a + len('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>'):]
t, n = re.subn(r'\n\s*<details><summary><span class="n">\d\d</span>Membership or a one off programme[^\n]*</details>', '', t)
assert n == 1, n

# ---------- FAQ ----------
rep('<small>From £24.99 a month, cancel anytime.</small>', '<small>Lifetime Team £119.99 a year · Quarterly £49.99 · ends Cyber Monday</small>')
rep('What exactly do I get for £24.99 a month?', 'What exactly do I get with the membership?')
faq_side = t.index('<div class="su-faq-side">')
a = t.index('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>', faq_side)
t = t[:a] + '<a class="su-btn su-btn--yellow" href="#pricing">Claim the offer</a>' + t[a + len('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>'):]
NEW_FAQ = ('<details open><summary><span class="n">01</span>How long is the Black Friday offer on?<span class="t">+</span></summary><p>Until midnight at the end of Cyber Monday, 30 November. When the timer hits zero, prices go back to normal.</p></details>\n'
           '      <details><summary><span class="n">02</span>What is the Lifetime Team?<span class="t">+</span></summary><p>It\'s the annual membership: a full year of Shape Up for £119.99, 60% less than paying £24.99 a month for 12 months. That works out at about 33p a day.</p></details>\n      ')
first = t.index('<details open><summary><span class="n">01</span>')
t = t[:first] + NEW_FAQ + t[first:].replace('<details open><summary>', '<details><summary>', 1)
fs = t.index('<section class="su-faq"'); fe = t.index('</section>', fs)
seg = t[fs:fe]; k = [0]
def num(m):
    k[0] += 1; return f'<span class="n">{k[0]:02d}</span>'
seg = re.sub(r'<span class="n">\d\d</span>', num, seg)
t = t[:fs] + seg + t[fe:]

# ---------- final CTA replaces the lead magnet ----------
FINAL = f'''<section class="su-lead bf-final">
  <div class="su-wrap">
    <p class="su-eyebrow">Black Friday ends soon</p>
    <h2 class="su-h2">Don't miss<strong>60% off</strong></h2>
    <p>£119.99 for the whole year until midnight on Cyber Monday. After that, it's gone.</p>
    {TIMER}
    <div><a class="su-btn" href="#pricing">Join now</a></div>
  </div>
</section>

'''
cut('<section class="su-lead">', '<!-- ===== FOOTER ===== -->', FINAL)

# ---------- mobile buy bar + countdown script ----------
BAR = '''<div class="bf-toast" id="bfToast" role="status" aria-live="polite"><span class="ic" aria-hidden="true"></span><div><b></b><small></small></div><button type="button" aria-label="Close">×</button></div>
<div class="bf-buybar" id="bfBuy"><div><b>Lifetime Team · £119.99/yr</b><span>Ends in <span data-cd-text>--</span></span></div><a class="su-btn" href="#pricing">60% off</a></div>
'''
SCRIPT = f'''<script>
(function(){{
  var END=new Date('{END}').getTime();
  function pad(n){{return (n<10?'0':'')+n}}
  function tick(){{
    var ms=Math.max(0,END-Date.now()),s=Math.floor(ms/1000),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),x=s%60;
    document.querySelectorAll('[data-cd]').forEach(function(el){{
      el.querySelector('.d').textContent=pad(d);el.querySelector('.h').textContent=pad(h);el.querySelector('.m').textContent=pad(m);el.querySelector('.s').textContent=pad(x);
      el.classList.toggle('ended',ms===0)}});
    document.querySelectorAll('[data-cd-text]').forEach(function(el){{el.textContent=ms?(d+'d '+pad(h)+'h '+pad(m)+'m '+pad(x)+'s'):'Offer ended'}});
    if(!ms)clearInterval(iv);
  }}
  var iv=setInterval(tick,1000);tick();
  var bar=document.getElementById('bfBuy'),hero=document.getElementById('top'),pr=document.getElementById('pricing');
  function bb(){{var past=hero.getBoundingClientRect().bottom<0,r=pr.getBoundingClientRect(),inP=r.top<innerHeight&&r.bottom>0;bar.classList.toggle('show',past&&!inP)}}
  addEventListener('scroll',bb,{{passive:true}});bb();
  // offer reminders (bottom left)
  var T=document.getElementById('bfToast'),ti=0,closed=false;
  function left(){{var ms=Math.max(0,END-Date.now()),s=Math.floor(ms/1000);return Math.floor(s/86400)+'d '+Math.floor(s%86400/3600)+'h '+Math.floor(s%3600/60)+'m left'}}
  var MSG=[
    ['🔥','Keep the price for life',function(){{return 'Annual is £119.99 a year, was £299.88'}}],
    ['💪','Quarterly is £15 off',function(){{return '£49.99 every 3 months, was £64.99'}}],
    ['⏰','Black Friday prices end Cyber Monday',left]
  ];
  function show(){{
    if(closed)return; var r=pr.getBoundingClientRect(); if(r.top<innerHeight&&r.bottom>0){{setTimeout(show,3000);return}}
    var m=MSG[ti++%MSG.length];T.querySelector('.ic').textContent=m[0];T.querySelector('b').textContent=m[1];T.querySelector('small').textContent=m[2]();
    T.classList.add('show');setTimeout(function(){{T.classList.remove('show');setTimeout(show,3500)}},6500);
  }}
  T.querySelector('button').addEventListener('click',function(){{closed=true;T.classList.remove('show')}});
  setTimeout(show,800);
}})();
</script>
'''
i = t.rindex('</body>')
t = t[:i] + BAR + SCRIPT + t[i:]

assert '£24.99 a month.</p>' not in t.split('<section class="su-faq"')[0]
open('black-friday-sale.html', 'w').write(t)
open('index.html', 'w').write(t)
print('wrote index.html and black-friday-sale.html', len(t))
