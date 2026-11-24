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
.bf-hero h1{font-family:var(--su-head);text-transform:uppercase;margin:0 0 24px;font-weight:700;line-height:.9;letter-spacing:-.5px}
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
@media (max-width:900px){
  .bf-hero{padding-top:150px;text-align:center}
  .bf-hero-grid{grid-template-columns:1fr;gap:0}
  .bf-copy{padding-bottom:0}
  .bf-kicker,.bf-price,.bf-ctas{justify-content:center}
  .bf-hero .lead{margin:0 auto 26px}
  .bf-art{height:440px;max-width:420px;width:100%;margin:40px auto -50px}
  .bf-plans{grid-template-columns:1fr}
  .bf-strip .su-wrap{justify-content:center;text-align:center}
}
@media (max-width:640px){
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
'''
i = t.index('</style>')
t = t[:i] + CSS + t[i:]

# ---------- header: announcement bar + CTA ----------
rep('<header class="su-header">\n  <nav class="su-nav" aria-label="Main">',
    '<header class="su-header">\n  <div class="bf-bar"><span class="t">Black Friday · 60% off annual</span><span class="cdw">Ends in <span class="cd" data-cd-text>--</span></span><a href="#pricing">Claim it →</a></div>\n  <nav class="su-nav" aria-label="Main">')
rep('<a class="su-btn su-btn--yellow" href="#pricing">Start now</a>\n      <button class="su-burger"',
    '<a class="su-btn su-btn--yellow" href="#pricing">Get 60% off</a>\n      <button class="su-burger"')

# ---------- hero ----------
HERO = f'''<!-- ===== HERO (Black Friday) ===== -->
<section class="bf-hero" id="top">
  <div class="su-wrap bf-hero-grid">
    <div class="bf-copy">
      <h1><span class="l1">Shape Up's biggest ever sale</span><span class="l2">60% off the whole year</span></h1>
      <p class="lead">The Lifetime Team, <strong>£119.99</strong> <s>£299.88</s> for 12 months of Shape Up.</p>
      <div class="bf-ctas">
        <a class="su-btn bf-btn" href="#pricing">Claim 60% off</a>
        <a class="bf-link" href="#inside">See what's inside</a>
      </div>
    </div>
    <div class="bf-art" aria-hidden="true">
      <img class="gabby" src="images/gabby-cutout-orange.webp" alt="">
    </div>
  </div>
</section>
<div class="su-ticker bf-ticker" aria-hidden="true">
    <div class="su-ticker-band">
      <div class="su-ticker-track">
        {''.join('<span><b>Black Friday</b></span><span class="spark">✦</span><span><b>60% off</b> annual</span><span class="spark">✦</span><span><b>£119.99</b> a year</span><span class="spark">✦</span><span><b>33p</b> a day</span><span class="spark">✦</span><span><b>Ends</b> Cyber Monday</span><span class="spark">✦</span>' for _ in range(2))}
      </div>
    </div>
</div>

'''
cut('<!-- ===== HERO ===== -->', '<!-- ===== WHAT SHAPE UP IS ===== -->', HERO)

# ---------- price mentions elsewhere ----------
rep('<small>From £24.99 a month, cancel anytime</small>', '<small>Black Friday: £119.99 a year, about 33p a day</small>')
rep('<p>All of these, plus every new programme we add, for <b>£24.99</b> a month.</p>',
    '<p>All of these, plus every new programme we add, for <b>£119.99</b> a year this Black Friday.</p>')

# ---------- pricing ----------
PRICING = f'''<!-- ===== PRICING (Black Friday) ===== -->
<svg class="su-wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true" style="margin-bottom:-1px"><path d="M0 70 C 400 -10, 1040 -10, 1440 70 Z" fill="#0d0d0d"/></svg>
<section class="bf-pricing" id="pricing">
  <div class="su-wrap">
    <p class="su-eyebrow">Black Friday prices</p>
    <h2 class="su-h2">60% off.<br><strong>Full year.</strong></h2>
    <p class="lede">Same full app on both plans. When the timer hits zero, prices go back to normal.</p>
    {TIMER}
    <div class="bf-plans">
      <article class="bf-plan bf-plan--main">
        <span class="flag">Main offer · 60% off</span>
        <span class="term">Annual</span>
        <h3>The Lifetime Team</h3>
        <div class="price"><s>£299.88</s><b>£119.99</b><span>a year</span></div>
        <span class="save">That's about 33p a day</span>
        <ul>
          <li>Every Shape Up programme, including Island Body V2 and Strength Is Power</li>
          <li>New content added every month</li>
          <li>Meal plans, barcode scanner and calorie tracking</li>
          <li>Cycle and habit tracking, plus the community</li>
        </ul>
        <a class="su-btn" href="{CHECKOUT_ANNUAL}">Join the Lifetime Team</a>
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
    <p><b>Black Friday</b> · Lifetime Team £119.99 a year</p>
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
    <p>The Lifetime Team is £119.99 for the whole year until midnight on Cyber Monday. After that, it's gone.</p>
    {TIMER}
    <div><a class="su-btn" href="#pricing">Join the Lifetime Team</a></div>
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
  var bar=document.getElementById('bfBuy'),hero=document.querySelector('.bf-hero'),pr=document.getElementById('pricing');
  function bb(){{var past=hero.getBoundingClientRect().bottom<0,r=pr.getBoundingClientRect(),inP=r.top<innerHeight&&r.bottom>0;bar.classList.toggle('show',past&&!inP)}}
  addEventListener('scroll',bb,{{passive:true}});bb();
  // offer reminders (bottom left)
  var T=document.getElementById('bfToast'),ti=0,closed=false;
  function left(){{var ms=Math.max(0,END-Date.now()),s=Math.floor(ms/1000);return Math.floor(s/86400)+'d '+Math.floor(s%86400/3600)+'h '+Math.floor(s%3600/60)+'m left'}}
  var MSG=[
    ['🔥','Lifetime Team is 60% off',function(){{return '£119.99 for the whole year, was £299.88'}}],
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
