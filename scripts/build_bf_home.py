"""Build black-friday-sale.html: the homepage (index.html) re-skinned as a Black Friday sales page.

Run from the repo root:  python3 scripts/build_bf_home.py
Edit the OFFER / END / CHECKOUT values below, then rebuild.
"""
import re

END = '2026-12-01T00:00:00Z'          # countdown end: midnight at the end of Cyber Monday (30 Nov, UK time)
CHECKOUT_ANNUAL = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership/yearly'      # TODO: Black Friday £149 link
CHECKOUT_QUARTER = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership/3-month'    # TODO: Black Friday £49.99 link

src = open('index.html').read()
t = src


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
t = re.sub(r'<title>[^<]*</title>', '<title>Black Friday: Half Price Annual Membership | Shape Up with Gabby</title>', t, count=1)
t = re.sub(r'<meta name="description" content="[^"]*">',
           '<meta name="description" content="Black Friday at Shape Up with Gabby: the annual Lifetime Team membership is half price at £149 a year, about 41p a day. Quarterly is £49.99. Ends Cyber Monday.">', t, count=1)
rep('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">')

CSS = '''
/* ===== BLACK FRIDAY LAYER ===== */
:root{--bf-ink:#0d0d0d;--bf-ink2:#1a1a1a}
.bf-bar{display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap;background:var(--bf-ink);color:#fff;margin:-12px -24px 12px;padding:9px 16px;font-size:12px;font-weight:600;letter-spacing:.6px;text-transform:uppercase}
.bf-bar .tag{background:var(--su-yellow);color:var(--bf-ink);border-radius:999px;padding:3px 10px;font-weight:700}
.bf-bar .cd{font-variant-numeric:tabular-nums;color:var(--su-yellow)}
.bf-bar a{color:#fff;text-underline-offset:3px}
.bf-hero{position:relative;overflow:hidden;color:#fff;padding:165px 0 0;
  background:radial-gradient(55% 60% at 78% 40%,rgba(98,186,245,.28) 0%,rgba(98,186,245,0) 70%),radial-gradient(40% 50% at 0% 100%,rgba(253,224,141,.14) 0%,rgba(253,224,141,0) 70%),var(--bf-ink)}
.bf-word{position:absolute;left:50%;top:150px;transform:translateX(-50%);font-family:var(--su-head);font-weight:700;font-size:min(19vw,290px);line-height:.8;letter-spacing:-4px;white-space:nowrap;color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.08);pointer-events:none;user-select:none}
.bf-hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.1fr .9fr;gap:30px;align-items:center}
.bf-tag{display:inline-flex;align-items:stretch;transform:rotate(-2.5deg);margin-bottom:4px;font-family:var(--su-head);text-transform:uppercase;line-height:1;box-shadow:6px 6px 0 var(--su-blue)}
.bf-tag b{background:var(--su-yellow);color:var(--bf-ink);font-size:26px;font-weight:700;padding:8px 12px 6px}
.bf-tag{font-size:15px;font-weight:500;letter-spacing:1px;color:#fff}
.bf-tag>span{display:flex;align-items:center;background:#fff;color:var(--bf-ink);padding:0 12px;font-weight:700}
.bf-hero .su-rating{background:none;box-shadow:none;padding:0;margin:0 0 20px;color:rgba(255,255,255,.85);font-weight:500;font-size:13px}
.bf-hero .su-rating .su-avatars img{border-color:var(--bf-ink)}
.bf-hero h1{font-family:var(--su-head);text-transform:uppercase;margin:16px 0 16px;line-height:.86;letter-spacing:-1px}
.bf-hero h1 .l1{display:block;font-weight:700;font-size:clamp(42px,5vw,72px)}
.bf-hero h1 .l1 em{font-style:normal;color:transparent;-webkit-text-stroke:2px #fff}
.bf-hero h1 .l2{position:relative;display:inline-block;font-weight:700;font-size:clamp(52px,6.6vw,100px);color:var(--su-yellow);padding-bottom:8px;white-space:nowrap}
.bf-scribble{position:absolute;left:-2%;bottom:-8px;width:104%;height:26px;overflow:visible}
.bf-scribble path{fill:none;stroke:var(--su-blue);stroke-width:7;stroke-linecap:round;stroke-dasharray:520;stroke-dashoffset:520;animation:bfdraw 1.4s .5s ease forwards}
@keyframes bfdraw{to{stroke-dashoffset:0}}
.bf-hero .lead{font-size:16px;color:rgba(255,255,255,.86);max-width:500px;margin:0 0 18px}
.bf-hero .lead strong{color:#fff}
.bf-timer{display:inline-flex;align-items:flex-start;gap:8px;font-family:var(--su-head);margin:0 0 20px}
.bf-timer>div{display:flex;flex-direction:column;align-items:center;min-width:66px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:14px;padding:10px 8px 8px}
.bf-timer b{font-size:34px;line-height:1;font-weight:700;color:var(--su-yellow);font-variant-numeric:tabular-nums}
.bf-timer span{font-family:var(--su-text);font-size:9.5px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;opacity:.7;margin-top:5px}
.bf-timer i{font-style:normal;font-size:28px;color:rgba(255,255,255,.4);padding-top:10px}
.bf-timer.ended>div b{color:#fff}
.bf-ctas{display:flex;gap:12px;flex-wrap:wrap}
.bf-btn{background:var(--su-yellow);color:var(--bf-ink);padding:17px 34px;box-shadow:0 12px 30px rgba(253,224,141,.25)}
.bf-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.6)}
.bf-note{margin:14px 0 0;font-size:12.5px;color:rgba(255,255,255,.7)}
.bf-art{position:relative;height:540px}
.bf-art .gabby{position:absolute;left:50%;bottom:0;height:auto;width:100%;max-width:none;transform:translateX(-50%);filter:drop-shadow(0 24px 40px rgba(0,0,0,.5))}
.bf-art .gabby{-webkit-mask-image:linear-gradient(180deg,#000 82%,transparent 100%);mask-image:linear-gradient(180deg,#000 82%,transparent 100%)}
.bf-art .glow{position:absolute;left:50%;top:8%;width:90%;aspect-ratio:1;transform:translateX(-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(253,224,141,.35),rgba(98,186,245,.18) 55%,rgba(98,186,245,0) 100%);filter:blur(10px)}
.bf-art .phone{position:absolute;right:-4%;bottom:40px;width:150px;border-radius:24px;border:5px solid #fff;overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.4);transform:rotate(6deg)}
.bf-art .phone img{display:block;width:100%}
.bf-sticker{position:absolute;z-index:3;border-radius:18px;padding:12px 16px;box-shadow:0 18px 40px rgba(0,0,0,.35);font-size:12px;font-weight:600;line-height:1.2;animation:bfbob 6s ease-in-out infinite}
.bf-sticker b{display:block;font-family:var(--su-head);font-size:30px;line-height:1;text-transform:uppercase}
.bf-sticker s{opacity:.6}
.bf-sticker.s1{left:-2%;top:22%;background:#fff;color:var(--bf-ink);transform:rotate(-5deg)}
.bf-sticker.s2{right:2%;top:6%;background:var(--su-yellow);color:var(--bf-ink);animation-delay:-3s}
@keyframes bfbob{50%{translate:0 -10px}}
.bf-hero{padding-bottom:140px;clip-path:polygon(0 0,100% 0,100% calc(100% - 5.3vw - 40px),0 calc(100% - 40px))}
.su-ticker.bf-ticker{margin-top:-128px;height:110px;margin-bottom:-24px;z-index:5}
.bf-ticker .su-ticker-band{background:var(--su-yellow)}
.bf-ticker .su-ticker-track span,.bf-ticker .su-ticker-track b,.bf-ticker .su-ticker-track .spark{color:var(--bf-ink)}
.bf-art{margin-bottom:-70px}

.bf-pricing{background:var(--bf-ink);color:#fff;padding:90px 0 100px;text-align:center}
.bf-pricing .su-eyebrow{color:var(--su-yellow)}
.bf-pricing .su-h2 strong{color:var(--su-yellow)}
.bf-pricing .lede{max-width:560px;margin:0 auto 22px;color:rgba(255,255,255,.8)}
.bf-plans{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;max-width:920px;margin:30px auto 0;text-align:left;align-items:stretch}
.bf-plan{position:relative;background:var(--bf-ink2);border:1px solid rgba(255,255,255,.14);border-radius:24px;padding:30px 28px;display:flex;flex-direction:column}
.bf-plan--main{background:var(--su-yellow);color:var(--bf-ink);border-color:var(--su-yellow);box-shadow:0 0 0 6px rgba(253,224,141,.15),0 30px 60px rgba(0,0,0,.4)}
.bf-plan .flag{position:absolute;top:-14px;left:24px;background:var(--bf-ink);color:var(--su-yellow);border:2px solid var(--su-yellow);border-radius:999px;padding:5px 14px;font-size:10.5px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase}
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
.bf-strip .bf-timer{margin:0}
.bf-strip .bf-timer>div{min-width:56px;padding:7px 6px 6px}
.bf-strip .bf-timer b{font-size:24px}

.bf-final{text-align:center}
.bf-final .su-h2{color:#fff}
.bf-final p{max-width:560px;margin:0 auto 22px;color:#fff}
.bf-final .bf-timer>div{background:rgba(13,13,13,.25);border-color:rgba(255,255,255,.35)}
.bf-final .bf-timer b{color:#fff}
.bf-final .su-btn{background:var(--bf-ink);color:#fff}

.bf-toast{position:fixed;left:18px;bottom:18px;z-index:70;display:flex;align-items:center;gap:12px;max-width:340px;background:#fff;color:var(--bf-ink);border-radius:14px;padding:12px 36px 12px 12px;box-shadow:0 14px 40px rgba(0,0,0,.25);border-left:5px solid var(--su-yellow);transform:translateY(160%);opacity:0;transition:transform .45s ease,opacity .45s ease;font-size:13px;line-height:1.35}
.bf-toast.show{transform:none;opacity:1}
.bf-toast .ic{flex:none;width:38px;height:38px;border-radius:10px;background:var(--bf-ink);color:var(--su-yellow);display:grid;place-items:center;font-size:18px}
.bf-toast b{display:block;font-size:13.5px}
.bf-toast small{display:block;color:#666;font-size:11.5px;margin-top:2px;font-variant-numeric:tabular-nums}
.bf-toast button{position:absolute;top:6px;right:8px;border:0;background:none;font-size:16px;line-height:1;color:#999;cursor:pointer;padding:4px}
.bf-buybar{display:none}
@media (max-width:900px){
  .bf-hero{padding-top:150px;text-align:center}
  .bf-hero-grid{grid-template-columns:1fr}
  .bf-hero .lead{margin:0 auto 20px}
  .bf-ctas{justify-content:center}
  .bf-art{height:380px;max-width:420px;width:100%;margin:10px auto 0}
  .bf-art .phone{width:110px;right:2%;bottom:30px}
  .bf-sticker b{font-size:24px}
  .bf-word{top:120px;font-size:30vw}
  .bf-plans{grid-template-columns:1fr}
  .bf-strip .su-wrap{justify-content:center;text-align:center}
}
@media (max-width:640px){
  .bf-bar{margin:-10px -12px 10px;font-size:10.5px;gap:8px;padding:8px 10px}
  .bf-bar a{display:none}
  .bf-hero{padding-top:140px}
  .bf-hero h1 .l2{font-size:clamp(46px,14vw,64px)}
  .bf-hero h1 .l1{font-size:clamp(36px,11vw,50px)}
  .bf-timer{gap:4px}
  .bf-timer>div{min-width:56px;padding:8px 4px 6px}
  .bf-timer b{font-size:26px}
  .bf-timer i{font-size:20px;padding-top:8px}
  .bf-ctas .su-btn{width:100%}
  .bf-art{height:380px;margin-bottom:-50px}
  .bf-art .phone{display:none}
  .bf-sticker{padding:9px 12px;font-size:11px}
  .bf-sticker b{font-size:20px}
  .bf-sticker.s1{left:0;top:30%}
  .bf-plan{padding:28px 20px}
  .bf-plan .price b{font-size:54px}
  .bf-toast{left:10px;right:10px;max-width:none;bottom:84px}
  .bf-buybar{display:flex;position:fixed;left:10px;right:10px;bottom:10px;z-index:60;align-items:center;justify-content:space-between;gap:10px;background:var(--bf-ink);color:#fff;border-radius:18px;padding:10px 10px 10px 16px;box-shadow:0 12px 30px rgba(0,0,0,.35);transform:translateY(140%);transition:transform .3s ease}
  .bf-buybar.show{transform:none}
  .bf-buybar b{display:block;font-size:13px}
  .bf-buybar span{font-size:11px;color:var(--su-yellow);font-variant-numeric:tabular-nums}
  .bf-buybar .su-btn{width:auto;display:inline-flex;padding:12px 16px;background:var(--su-yellow);color:var(--bf-ink);font-size:11.5px}
}
@media (prefers-reduced-motion:reduce){.bf-toast{transition:none}.bf-sticker{animation:none}.bf-scribble path{animation:none;stroke-dashoffset:0}}
'''
i = t.index('</style>')
t = t[:i] + CSS + t[i:]

# ---------- header: announcement bar + CTA ----------
rep('<header class="su-header">\n  <nav class="su-nav" aria-label="Main">',
    '<header class="su-header">\n  <div class="bf-bar"><span class="tag">Black Friday</span><span>Annual membership half price · £149</span><span>Ends in <span class="cd" data-cd-text>--</span></span><a href="#pricing">Claim it</a></div>\n  <nav class="su-nav" aria-label="Main">')
rep('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>\n      <button class="su-burger"',
    '<a class="su-btn su-btn--yellow" href="#pricing">Get 50% off</a>\n      <button class="su-burger"')

# ---------- hero ----------
HERO = f'''<!-- ===== HERO (Black Friday) ===== -->
<section class="bf-hero" id="top">
  <div class="bf-word" aria-hidden="true">BLACK FRIDAY</div>
  <div class="su-wrap bf-hero-grid">
    <div class="bf-copy">
      <div><span class="bf-tag"><b>50% off</b><span>Black Friday sale</span></span></div>
      <h1><span class="l1"><em>Black</em> Friday</span><span class="l2">Half price</span></h1>
      <p class="lead">Join the <strong>Lifetime Team</strong> for <strong>£149 for the whole year</strong>. That's about 41p a day for every programme, every meal plan and 12,400 women training alongside you.</p>
      {TIMER}
      <div class="bf-ctas">
        <a class="su-btn bf-btn" href="#pricing">Claim half price</a>
        <a class="su-btn su-btn--outline bf-ghost" href="#inside">See what's inside <span aria-hidden="true">↓</span></a>
      </div>
      <p class="bf-note">Black Friday prices end at midnight on Cyber Monday.</p>
    </div>
    <div class="bf-art" aria-hidden="true">
      <div class="glow"></div>
      <img class="gabby" src="images/gabby-cutout-peach.webp" alt="">
      <div class="phone"><img src="images/img-12.webp" alt=""></div>
      <div class="bf-sticker s1"><b>£149</b><s>£299.88</s> a year</div>
      <div class="bf-sticker s2"><b>41p</b>a day</div>
    </div>
  </div>
</section>
<div class="su-ticker bf-ticker" aria-hidden="true">
    <div class="su-ticker-band">
      <div class="su-ticker-track">
        {''.join('<span><b>Black Friday</b></span><span class="spark">✦</span><span><b>50% off</b> annual</span><span class="spark">✦</span><span><b>£149</b> a year</span><span class="spark">✦</span><span><b>41p</b> a day</span><span class="spark">✦</span><span><b>Ends</b> Cyber Monday</span><span class="spark">✦</span>' for _ in range(2))}
      </div>
    </div>
</div>

'''
cut('<!-- ===== HERO ===== -->', '<!-- ===== WHAT SHAPE UP IS ===== -->', HERO)

# ---------- price mentions elsewhere ----------
rep('<small>From £24.99 a month, cancel anytime</small>', '<small>Black Friday: £149 a year, about 41p a day</small>')
rep('<p>All of these, plus every new programme we add, for <b>£24.99</b> a month.</p>',
    '<p>All of these, plus every new programme we add, for <b>£149</b> a year this Black Friday.</p>')

# ---------- pricing ----------
PRICING = f'''<!-- ===== PRICING (Black Friday) ===== -->
<svg class="su-wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true" style="margin-bottom:-1px"><path d="M0 70 C 400 -10, 1040 -10, 1440 70 Z" fill="#0d0d0d"/></svg>
<section class="bf-pricing" id="pricing">
  <div class="su-wrap">
    <p class="su-eyebrow">Black Friday prices</p>
    <h2 class="su-h2">Half price.<br><strong>Full year.</strong></h2>
    <p class="lede">Same full app on both plans. When the timer hits zero, prices go back to normal.</p>
    {TIMER}
    <div class="bf-plans">
      <article class="bf-plan bf-plan--main">
        <span class="flag">Main offer · 50% off</span>
        <span class="term">Annual</span>
        <h3>The Lifetime Team</h3>
        <div class="price"><s>£299.88</s><b>£149</b><span>a year</span></div>
        <span class="save">That's about 41p a day</span>
        <ul>
          <li>Every Shape Up programme, including Island Body V2 and Strength Is Power</li>
          <li>New content added every month</li>
          <li>Meal plans, barcode scanner and calorie tracking</li>
          <li>Cycle and habit tracking, plus the community</li>
        </ul>
        <a class="su-btn" href="{CHECKOUT_ANNUAL}">Join the Lifetime Team</a>
        <small>Half the price of 12 months at £24.99</small>
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
    <ul class="su-ticks">
      <li>iOS &amp; Android</li><li>Gym and home plans</li><li>All abilities</li>
    </ul>
  </div>
</section>

'''
s = t.index('<!-- ===== PRICING ===== -->')
e = t.index('<!-- ===== PROGRAMMES', s)
t = t[:s] + PRICING + t[e:]

# ---------- mid-page strip before results ----------
STRIP = f'''<div class="bf-strip">
  <div class="su-wrap">
    <p><b>Black Friday</b> · Lifetime Team £149 a year</p>
    {TIMER}
    <a class="su-btn bf-btn" href="#pricing">Claim half price</a>
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
t = t[:a] + '<a class="su-btn su-btn--yellow" href="#pricing">Claim half price</a>' + t[a + len('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>'):]
t, n = re.subn(r'\n\s*<details><summary><span class="n">\d\d</span>Membership or a one off programme[^\n]*</details>', '', t)
assert n == 1, n

# ---------- FAQ ----------
rep('<small>From £24.99 a month, cancel anytime.</small>', '<small>Lifetime Team £149 a year · Quarterly £49.99 · ends Cyber Monday</small>')
rep('What exactly do I get for £24.99 a month?', 'What exactly do I get with the membership?')
faq_side = t.index('<div class="su-faq-side">')
a = t.index('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>', faq_side)
t = t[:a] + '<a class="su-btn su-btn--yellow" href="#pricing">Claim the offer</a>' + t[a + len('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>'):]
NEW_FAQ = ('<details open><summary><span class="n">01</span>How long is the Black Friday offer on?<span class="t">+</span></summary><p>Until midnight at the end of Cyber Monday, 30 November. When the timer hits zero, prices go back to normal.</p></details>\n'
           '      <details><summary><span class="n">02</span>What is the Lifetime Team?<span class="t">+</span></summary><p>It\'s the annual membership: a full year of Shape Up for £149, half the price of paying £24.99 a month for 12 months. That works out at about 41p a day.</p></details>\n      ')
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
    <h2 class="su-h2">Don't miss<strong>half price</strong></h2>
    <p>The Lifetime Team is £149 for the whole year until midnight on Cyber Monday. After that, it's gone.</p>
    {TIMER}
    <div><a class="su-btn" href="#pricing">Join the Lifetime Team</a></div>
  </div>
</section>

'''
cut('<section class="su-lead">', '<!-- ===== FOOTER ===== -->', FINAL)

# ---------- mobile buy bar + countdown script ----------
BAR = '''<div class="bf-toast" id="bfToast" role="status" aria-live="polite"><span class="ic" aria-hidden="true"></span><div><b></b><small></small></div><button type="button" aria-label="Close">×</button></div>
<div class="bf-buybar" id="bfBuy"><div><b>Lifetime Team · £149/yr</b><span>Ends in <span data-cd-text>--</span></span></div><a class="su-btn" href="#pricing">50% off</a></div>
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
  var bar=document.getElementById('bfBuy'),hero=document.querySelector('.bf-hero'),pr=document.getElementById('pricing');
  function bb(){{var past=hero.getBoundingClientRect().bottom<0,r=pr.getBoundingClientRect(),inP=r.top<innerHeight&&r.bottom>0;bar.classList.toggle('show',past&&!inP)}}
  addEventListener('scroll',bb,{{passive:true}});bb();
  // offer reminders (bottom left)
  var T=document.getElementById('bfToast'),ti=0,closed=false;
  function left(){{var ms=Math.max(0,END-Date.now()),s=Math.floor(ms/1000);return Math.floor(s/86400)+'d '+Math.floor(s%86400/3600)+'h '+Math.floor(s%3600/60)+'m left'}}
  var MSG=[
    ['🔥','Lifetime Team is half price',function(){{return '£149 for the whole year, was £299.88'}}],
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
print('wrote black-friday-sale.html', len(t))
