"""Builds the two programme sales pages for shapeupapp.co.uk from one template.

Usage: python3 build_sales.py /path/to/shapeupwaitlist
Writes island-body-v2.html and strength-is-power.html into the repo root.
"""
import sys, os, html

REPO = sys.argv[1]

GA = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KNYFB4VHQ3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-KNYFB4VHQ3');
</script>
'''

MEM_MONTHLY = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership/monthly'
MEM_YEARLY = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership/yearly'
INSTAGRAM = 'https://www.instagram.com/gabbydawnallen/?hl=en'

APP_FEATS = [
    ('🏋️‍♀️', 'Workout tracker', 'Your programme laid out week by week, with every exercise, set and rep ready to go.', 'images/app-workout.webp'),
    ('🎥', 'Demos and logging', 'Watch a demo for every exercise, then log your weights and reps as you train.', 'images/app-log.webp'),
    ('🏠', 'Your home screen', "Today's workout, meals and progress, all on one screen.", 'images/app-home.webp'),
    ('🗓️', 'Tasks and cycle tracking', 'Tick off your daily tasks and train with your cycle, not against it.', 'images/app-today.webp'),
    ('🥗', 'Meal plans', 'Recipes with calories and macros worked out, so food is sorted too.', 'images/app-meals.webp'),
    ('💧', 'Habit building', 'Pick the habits you want to work on and the app keeps you on track.', 'images/app-habits.webp'),
]
APP_PILLS = [('💪','Workout logger'),('🎥','Exercise video demos'),('📊','PRs and history'),('🥗','Meal plans'),('📷','Food logger and scanner'),('❤️','Apple and Google Health'),('🎯','Goal setting'),('📸','Progress photos'),('💧','Habit tracking'),('✅','Daily tasks'),('🌸','Cycle tracker'),('📋','Check ins'),('🍴','Recipes and favourites')]

PAGES = {
    'island-body-v2': dict(
        title='Island Body V2 | Shape Up with Gabby',
        desc="Island Body V2 is Gabby's revamped 8 week lower body focused strength programme, with upper body conditioning. All abilities. £59, or included in the Shape Up membership.",
        name='Island Body V2',
        h1=('Island Body', 'V2'),
        theme='island',
        img='images/ib-hero.webp', img_alt='Gabby in a tropical setting', img_pos='50% 30%', img_pos_m='50% 25%',
        checkout='https://join.shapeupwithgabby.co.uk/p/island-body-v2/one-time',
        kicker='8 weeks · strength · hypertrophy',
        sub="My best selling programme, completely revamped. Eight weeks of lower body focused strength training paired with upper body conditioning, with a revised and perfected format so every week builds on the last.",
        chips=['8 weeks', 'Lower body focus', 'All abilities'],
        for_you_h=('This is for you', 'if...'),
        for_you=[
            "You loved the original Island Body, or always wished you'd done it",
            "You want to build your lower body and glutes with proper strength training",
            "You want a plan that tells you exactly what to do, every single session",
            "You want to see real progress over eight weeks, not just get sweaty",
        ],
        for_you_tag="And yes... it's the big, juicy peach one 🍑",
        inside=[
            ('Revamped from the original', 'The best selling Island Body programme, revised and perfected, with fresh exercises throughout.'),
            ('Lower body focused strength', 'Sessions built to grow and strengthen your lower body and glutes, week after week.'),
            ('Upper body conditioning', 'Balanced with upper body work, so you build a strong, athletic shape all over.'),
            ('Clear progressions', 'Every week builds on the last, so you always know you are moving forward.'),
            ('All abilities catered for', "Brand new to lifting or training for years, the plan works for you."),
            ('Gym recommended', 'Best in the gym, but you can follow it at home as long as you have a range of weights.'),
        ],
        note=("Island Body has always been the programme you lot message me about the most. So for V2 I went back through every single session, kept what you loved, rebuilt what I knew could be better and added fresh exercises throughout. If you loved the original, you're going to LOVE this one."),
        faq_gym=('Do I need a gym?', 'A gym is recommended, but you can follow Island Body V2 at home as long as you have a range of weights to work with.'),
        programme_ticks=['The full 8 week programme', 'Lower body focus with upper body conditioning', 'Follow it in the Shape Up app'],
        other=('strength-is-power', 'Strength Is Power', '8 weeks of full body strength, built around the big compound lifts.', 'images/img-46.webp', '50% 30%'),
    ),
    'strength-is-power': dict(
        title='Strength Is Power | Shape Up with Gabby',
        desc="Strength Is Power is Gabby's new 8 week full body strength programme, built around the big compound lifts. All abilities, gym or home. £59, or included in the Shape Up membership.",
        name='Strength Is Power',
        h1=('Strength', 'Is Power'),
        theme='strength',
        img='images/sip-hero.webp', img_alt='Gabby in the gym with a barbell', img_pos='41% 50%', img_pos_m='41% 40%',
        checkout='https://join.shapeupwithgabby.co.uk/p/strength-is-power/one-time',
        kicker='8 weeks · strength focus',
        sub="Eight weeks built to increase your full body strength. Progressive sessions centred on the big compound lifts, with clear weekly targets so you can watch your numbers go up and lift heavier with confidence.",
        chips=['8 weeks', 'Full body strength', 'Gym or home'],
        for_you_h=('This is for you', 'if...'),
        for_you=[
            "You want to get properly strong, not just tired",
            "You've always wanted to feel confident with the big lifts",
            "You like a simple plan that's easy to follow and actually works",
            "You want to build a strong, athletic shape from head to toe",
        ],
        for_you_tag="Simple format. Proven results. 💪",
        inside=[
            ('Built around compound lifts', 'Sessions centred on the big compound movements, building your confidence every time you lift.'),
            ('Clear weekly targets', 'Targets for every week, so you can watch your numbers go up and see your strength grow.'),
            ('Simple format', 'No guesswork and no overcomplicating. Show up, follow the plan, get stronger.'),
            ('360 full body approach', 'Every part of you gets stronger, to build the shape you dream of.'),
            ('All abilities catered for', "Brand new to lifting or training for years, the plan works for you."),
            ('Gym or home', 'Follow it in the gym or at home, whatever suits your week.'),
        ],
        note=("Getting strong changed everything for me. Not just how I look, but how I feel walking into a room. I built Strength Is Power to give you that same feeling, with a simple plan that makes lifting heavier feel achievable from your very first session."),
        faq_gym=('Do I need a gym?', 'No. You can follow Strength Is Power in the gym or at home.'),
        programme_ticks=['The full 8 week programme', 'Built around the big compound lifts', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2', 'My best selling programme, revamped: lower body focused strength with upper body conditioning.', 'images/img-45.webp', '50% 0%'),
    ),
}

CSS = r'''
:root{
  --ink:#121212;--body:#3d3d3d;--muted:#6f6f6f;
  --yellow:#FDE08D;--cream:#FFF7DD;--blue:#62BAF5;--blue-soft:#EAF4FE;
  --head:'Oswald','Arial Narrow',Arial,sans-serif;
  --text:'Poppins',system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  box-sizing:border-box;
}
.island{--acc:#B07A1F;--acc-soft:#F7E6BF;--hero-a:#FFF3D6;--hero-b:#FBE3B0;--band:#1E2A22;--band-acc:#F2C76B}
.strength{--acc:#2F8FD1;--acc-soft:#DCEEFC;--hero-a:#F3F6F9;--hero-b:#E2EAF1;--band:#121212;--band-acc:#62BAF5}
*,*::before,*::after{box-sizing:inherit}
html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);font-family:var(--text);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;background:#fff;overflow-x:hidden;padding-bottom:env(safe-area-inset-bottom,0px)}
img{max-width:100%;display:block}
a{color:inherit}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.h2{font-family:var(--head);text-transform:uppercase;font-weight:300;font-size:clamp(34px,4.6vw,54px);line-height:1;margin:0;letter-spacing:-.4px}
.h2 strong{font-weight:700;display:block}
.eyebrow{font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--acc);margin:0 0 12px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;font:600 13px var(--text);letter-spacing:1.2px;text-transform:uppercase;text-decoration:none;padding:17px 32px;background:var(--ink);color:#fff;transition:transform .15s ease,background .15s ease;border:0;cursor:pointer}
.btn:hover{transform:translateY(-1px);background:#000}
.btn--yellow{background:var(--yellow);color:var(--ink)}
.btn--yellow:hover{background:#ffd56a}
.btn--line{background:transparent;color:var(--ink);border:1.5px solid var(--ink);padding:15px 28px}
.btn--line:hover{background:var(--ink);color:#fff}

/* Top bar */
.top{position:sticky;top:0;z-index:40;padding:calc(env(safe-area-inset-top,0px) + 10px) 16px 0}
.bar{max-width:1180px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;background:rgba(255,255,255,.88);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-radius:999px;padding:8px 8px 8px 22px;box-shadow:0 6px 24px rgba(0,0,0,.07)}
.bar img{height:22px;width:auto}
.bar .btn{padding:11px 20px;font-size:11.5px}

/* Hero */
.hero{background:radial-gradient(60% 70% at 80% 30%,var(--hero-b) 0%,rgba(255,255,255,0) 70%),linear-gradient(180deg,var(--hero-a) 0%,#fff 100%);margin-top:-62px;padding:110px 0 70px}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:48px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:7px 14px 7px 10px;font-size:12px;font-weight:600;box-shadow:0 4px 14px rgba(0,0,0,.06)}
.pill i{width:9px;height:9px;border-radius:50%;background:#E8463B}
.hero h1{font-family:var(--head);text-transform:uppercase;font-weight:300;font-size:clamp(54px,7.4vw,104px);line-height:.9;letter-spacing:-1.5px;margin:20px 0 6px}
.hero h1 strong{display:block;font-weight:700;color:var(--ink)}
.kicker{font-size:12px;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;color:var(--acc);margin:14px 0 14px}
.hero .sub{font-size:16px;color:var(--body);max-width:500px;margin:0 0 22px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px;padding:0;list-style:none}
.chips li{background:#fff;border:1.5px solid var(--acc-soft);border-radius:999px;padding:7px 14px;font-size:12.5px;font-weight:600}
.cta-row{display:flex;flex-wrap:wrap;align-items:center;gap:14px 20px}
.cta-row .alt{font-size:13px;font-weight:600;text-decoration:underline;text-underline-offset:4px;color:var(--ink)}
.price-line{font-size:12px;color:var(--muted);margin-top:14px}
.hero-art{position:relative}
.hero-art .frame{position:relative;border-radius:30px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 30px 60px rgba(0,0,0,.18);background:#ddd}
.hero-art .frame img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos)}
.float{position:absolute;z-index:2;background:#fff;border-radius:18px;padding:12px 16px;box-shadow:0 14px 34px rgba(0,0,0,.14);font-size:12px;font-weight:600;line-height:1.25}
.float b{display:block;font-family:var(--head);font-size:26px;line-height:1;font-weight:700}
.float.f1{left:-22px;top:12%}
.float.f2{right:-18px;bottom:10%;background:var(--yellow)}

/* For you */
.foryou{padding:90px 0}
.foryou-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:56px;align-items:start}
.list{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.list li{display:grid;grid-template-columns:34px 1fr;gap:14px;align-items:center;background:var(--cream);border-radius:16px;padding:14px 18px;font-weight:500;font-size:15px;line-height:1.45}
.list li::before{content:"✓";width:34px;height:34px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:14px;font-weight:700}
.tagline{margin-top:20px;font-family:var(--head);font-size:24px;font-weight:500;text-transform:uppercase;line-height:1.15}

/* Inside */
.inside{background:var(--band);color:#fff;padding:90px 0;border-radius:36px;margin:0 12px}
.inside .eyebrow{color:var(--band-acc)}
.inside-head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:40px}
.inside-head p{max-width:330px;margin:0;color:rgba(255,255,255,.75);font-size:14px}
.feat-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;counter-reset:f}
.feat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:22px;padding:26px 22px;counter-increment:f;position:relative}
.feat::before{content:counter(f,decimal-leading-zero);font-family:var(--head);font-weight:700;font-size:15px;color:var(--band-acc);display:block;margin-bottom:22px}
.feat h3{font-family:var(--head);font-weight:500;text-transform:uppercase;font-size:21px;line-height:1.1;margin:0 0 8px}
.feat p{margin:0;font-size:13.5px;color:rgba(255,255,255,.75);line-height:1.55}

/* Note from Gabby */
.note{padding:90px 0}
.note-card{display:grid;grid-template-columns:minmax(0,.75fr) minmax(0,1.25fr);gap:0;background:var(--cream);border-radius:28px;overflow:hidden}
.note-card .ph{position:relative;min-height:340px;background:#111}
.note-card .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 20%}
.note-card .bd{padding:46px 44px;display:flex;flex-direction:column;justify-content:center}
.note-card blockquote{margin:0 0 18px;font-size:clamp(17px,1.8vw,21px);font-weight:500;line-height:1.5}
.note-card cite{font-style:normal;font-family:var(--head);font-size:22px;text-transform:uppercase;font-weight:700}
.note-card cite span{display:block;font-family:var(--text);font-size:12px;font-weight:500;text-transform:none;color:var(--muted);margin-top:2px}

/* How it works */
.how{padding:0 0 90px}
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:36px;counter-reset:s;list-style:none;padding:0}
.steps li{border:1.5px solid #ececec;border-radius:22px;padding:24px 22px;counter-increment:s}
.steps li::before{content:counter(s);display:grid;place-items:center;width:42px;height:42px;border-radius:12px;background:var(--yellow);font-family:var(--head);font-weight:700;font-size:20px;margin-bottom:16px}
.steps b{display:block;font-size:16px;margin-bottom:4px}
.steps span{font-size:13.5px;color:var(--body)}

/* Pricing */
.pricing{background:linear-gradient(180deg,#fff 0%,var(--cream) 18%,var(--cream) 100%);padding:90px 0}
.pricing .h2,.pricing .intro{text-align:center}
.pricing .eyebrow{text-align:center}
.pricing .intro{max-width:520px;margin:14px auto 40px;color:var(--body)}
.plans{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:18px;max-width:980px;margin:0 auto;align-items:stretch}
.plan{background:#fff;border-radius:26px;padding:30px 28px;display:flex;flex-direction:column;border:1.5px solid #eee}
.plan .name{font-family:var(--head);font-size:24px;font-weight:700;text-transform:uppercase;line-height:1.1;margin:0 0 4px}
.plan .what{font-size:13px;color:var(--muted);margin:0 0 18px}
.plan .amount{display:flex;align-items:baseline;gap:6px;margin-bottom:18px}
.plan .amount b{font-family:var(--head);font-size:54px;font-weight:700;line-height:1}
.plan .amount span{font-size:13px;color:var(--muted)}
.plan ul{list-style:none;padding:0;margin:0 0 24px;display:grid;gap:8px}
.plan li{display:flex;gap:10px;font-size:14px;line-height:1.4}
.plan li::before{content:"✓";flex:0 0 20px;height:20px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:11px;font-weight:700;margin-top:1px}
.plan .btn{margin-top:auto;width:100%}
.plan--mem{background:var(--ink);color:#fff;border-color:var(--ink);position:relative;box-shadow:0 24px 50px rgba(0,0,0,.2)}
.plan--mem .what,.plan--mem .amount span{color:rgba(255,255,255,.7)}
.plan--mem li::before{background:var(--yellow);color:var(--ink)}
.plan--mem .badge{position:absolute;top:-13px;left:28px;background:var(--yellow);color:var(--ink);font-family:var(--head);font-weight:700;font-size:13px;letter-spacing:1px;text-transform:uppercase;padding:5px 12px;border-radius:8px}
.plan--mem .annual{display:block;text-align:center;margin-top:12px;font-size:12.5px;color:rgba(255,255,255,.85);text-underline-offset:3px}
.plan--mem .annual:hover{color:#fff}

/* FAQ */
.faq{padding:90px 0}
.faq-grid{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:56px}
.faq details{border-bottom:1px solid #e6e6e6}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;align-items:center;padding:20px 0;font-weight:600;font-size:15.5px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:0 0 28px;height:28px;border-radius:50%;border:1.5px solid var(--ink);display:grid;place-items:center;font-weight:400;font-size:18px;line-height:1;transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg);background:var(--ink);color:#fff}
.faq details p{margin:0 0 20px;color:var(--body);font-size:14.5px;max-width:600px}

/* Also new */
.also{padding:0 0 90px}
.also-card{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);background:var(--blue-soft);border-radius:28px;overflow:hidden;text-decoration:none;transition:transform .15s ease}
.also-card:hover{transform:translateY(-2px)}
.also-card .ph{position:relative;min-height:260px}
.also-card .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.also-card .bd{padding:36px 36px;display:flex;flex-direction:column;justify-content:center}
.also-card h3{font-family:var(--head);font-size:34px;font-weight:700;text-transform:uppercase;line-height:1;margin:0 0 10px}
.also-card p{margin:0 0 18px;color:var(--body);font-size:14.5px;max-width:420px}
.also-card .go{font-weight:600;font-size:13px;letter-spacing:1px;text-transform:uppercase}

/* Final CTA */
.final{background:var(--yellow);padding:70px 0;text-align:center}
.final .h2{margin-bottom:14px}
.final p{max-width:480px;margin:0 auto 26px;font-size:15px}
.final .cta-row{justify-content:center}

footer{padding:26px 0 calc(26px + env(safe-area-inset-bottom,0px));font-size:12px;color:var(--muted)}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.foot nav{display:flex;gap:18px}
.foot a{text-decoration:none;font-weight:600;color:var(--ink)}

/* Mobile sticky buy bar */
.buybar{display:none}

@media (max-width:900px){
  .hero{padding:96px 0 50px}
  .hero-grid{grid-template-columns:1fr;gap:30px}
  .hero-art{order:-1;max-width:520px;width:100%;margin:0 auto}
  .hero-art .frame{aspect-ratio:4/3}
  .hero-art .frame img{object-position:var(--pos-m)}
  .float.f1{left:10px;top:auto;bottom:-18px}
  .float.f2{right:10px;bottom:-18px}
  .hero .copy{text-align:center}
  .hero .sub{margin:0 auto 20px;font-size:15px}
  .chips,.cta-row{justify-content:center}
  .foryou-grid,.faq-grid{grid-template-columns:1fr;gap:28px}
  .feat-grid{grid-template-columns:1fr 1fr}
  .inside-head{flex-direction:column;align-items:flex-start;gap:14px}
  .note-card,.also-card{grid-template-columns:1fr}
  .note-card .ph{min-height:0;aspect-ratio:16/10}
  .also-card .ph{min-height:0;aspect-ratio:16/9}
  .note-card .bd,.also-card .bd{padding:28px 24px}
  .plans{grid-template-columns:1fr;max-width:480px}
  .plan--mem{order:-1}
  .steps{grid-template-columns:1fr}
}
@media (max-width:640px){
  body{padding-bottom:calc(84px + env(safe-area-inset-bottom,0px))}
  .bar .btn{display:none}
  .bar{justify-content:center;padding:10px 18px}
  .hero h1{font-size:clamp(52px,16vw,74px)}
  .cta-row .btn{width:100%}
  .foryou,.note,.faq,.pricing{padding:64px 0}
  .inside{padding:64px 0;margin:0 8px;border-radius:26px}
  .feat-grid{grid-template-columns:1fr}
  .how,.also{padding-bottom:64px}
  .list li{font-size:14px;padding:12px 14px;grid-template-columns:30px 1fr}
  .list li::before{width:30px;height:30px}
  .buybar{display:flex;position:fixed;left:10px;right:10px;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:50;align-items:center;justify-content:space-between;gap:12px;background:var(--ink);color:#fff;border-radius:20px;padding:10px 10px 10px 18px;box-shadow:0 14px 34px rgba(0,0,0,.3);transform:translateY(140%);transition:transform .25s ease}
  .buybar.show{transform:none}
  .buybar b{display:block;font-family:var(--head);font-size:17px;text-transform:uppercase;line-height:1.1}
  .buybar span{font-size:11.5px;color:rgba(255,255,255,.75)}
  .buybar .btn{padding:12px 18px;font-size:11.5px;background:var(--yellow);color:var(--ink)}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn,.also-card,.buybar{transition:none}.btn:hover,.also-card:hover{transform:none}}

/* Phone mockup */
.phone{position:relative;background:#111;border-radius:40px;padding:8px;box-shadow:0 30px 60px rgba(0,0,0,.28),inset 0 0 0 2px #2a2a2a}
.phone .scr{position:relative;border-radius:32px;overflow:hidden;aspect-ratio:380/826;background:#f4f4f4}
.phone .scr img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s ease}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes bobr{0%,100%{transform:translateY(0) rotate(var(--r,0deg))}50%{transform:translateY(-12px) rotate(var(--r,0deg))}}
.float,.hero-phone{animation:bob 6s ease-in-out infinite}
.float.f2{animation-delay:-2s}
.hero-phone{position:absolute;z-index:3;left:-46px;bottom:-34px;width:150px;animation-delay:-3s}
.float.f1{left:auto;right:-18px;top:9%}

/* App spotlight */
.app{padding:96px 0 40px;overflow:hidden}
.app-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center}
.app-intro{color:var(--body);margin:16px 0 26px;max-width:460px}
.feats{list-style:none;margin:0;padding:0;border-top:1px solid #e8e8e8}
.feats li{border-bottom:1px solid #e8e8e8;position:relative}
.feats button{all:unset;box-sizing:border-box;width:100%;cursor:pointer;display:grid;grid-template-columns:40px 1fr 22px;align-items:center;padding:16px 0;font-family:var(--head);font-weight:500;text-transform:uppercase;font-size:21px;color:#8a8f96;transition:color .2s}
.feats button:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.feats .ic{width:30px;height:30px;border-radius:9px;background:#f1f1f1;display:grid;place-items:center;font-size:15px;filter:grayscale(1);opacity:.6;transition:all .2s}
.feats .pl{font-family:var(--text);font-weight:400;font-size:20px;transition:transform .2s}
.feats p{margin:0;max-height:0;overflow:hidden;padding-left:40px;font-size:14px;color:var(--body);transition:max-height .35s ease,padding .35s ease}
.feats .prog{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--ink)}
.feats li.on button{color:var(--ink)}
.feats li.on .ic{background:var(--yellow);filter:none;opacity:1}
.feats li.on .pl{transform:rotate(45deg)}
.feats li.on p{max-height:110px;padding-bottom:16px}
.feats li.on .prog{animation:prog var(--dur,4.5s) linear forwards}
.feats.paused li.on .prog{animation:none;width:100%}
@keyframes prog{to{width:100%}}
.stage{position:relative;height:640px;display:flex;align-items:center;justify-content:center}
.stage::before{content:"";position:absolute;width:470px;height:470px;border-radius:50%;background:var(--yellow)}
.stage::after{content:"";position:absolute;width:560px;height:560px;border-radius:50%;border:2px dashed rgba(0,0,0,.12);animation:spin 60s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.stage .phone{width:270px;z-index:2;animation:bob 7s ease-in-out infinite}
.chip{position:absolute;z-index:3;background:#fff;border-radius:16px;padding:10px 14px;box-shadow:0 14px 34px rgba(0,0,0,.14);font-size:12px;font-weight:600;line-height:1.25;display:flex;align-items:center;gap:9px;animation:bob 6s ease-in-out infinite}
.chip span{width:30px;height:30px;border-radius:9px;background:var(--acc-soft);display:grid;place-items:center;font-size:15px}
.chip.c1{top:16%;left:2%}
.chip.c2{bottom:18%;right:0;animation-delay:-2.5s}
.chip.c3{top:8%;right:6%;animation-delay:-4s}

/* Phone strip */
.strip{padding:30px 0 96px;overflow:hidden}
.phones{display:flex;justify-content:center;align-items:flex-start;gap:22px;margin:0 0 40px}
.phones .phone{flex:0 0 190px;animation:bobr 7s ease-in-out infinite}
.phones .phone:nth-child(1){--r:-6deg;margin-top:70px;animation-delay:-1s}
.phones .phone:nth-child(2){--r:-3deg;margin-top:28px;animation-delay:-3s}
.phones .phone:nth-child(3){margin-top:0;animation-delay:-5s}
.phones .phone:nth-child(4){--r:3deg;margin-top:28px;animation-delay:-2s}
.phones .phone:nth-child(5){--r:6deg;margin-top:70px;animation-delay:-4s}
.pills{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;max-width:820px;margin:0 auto;list-style:none;padding:0}
.pills li{display:flex;align-items:center;gap:8px;border:1.5px solid var(--acc-soft);background:#fff;border-radius:999px;padding:8px 16px;font-size:13.5px;font-weight:500}
.pills li:nth-child(odd){background:var(--cream)}
.pills i{font-style:normal}
.strip-h{text-align:center;margin-bottom:36px}
.strip-h .eyebrow{text-align:center}

/* Reveal on scroll */
.rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
.rv.in{opacity:1;transform:none}

@media (max-width:900px){
  .hero-phone{width:104px;left:12px;bottom:-26px}
  .float.f1{right:auto;left:auto;right:12px;top:12px;bottom:auto}
  .float.f2{right:12px;bottom:-18px}
  .app{padding:70px 0 20px}
  .app-grid{grid-template-columns:1fr;gap:10px}
  .stage{order:-1;height:470px}
  .stage::before{width:320px;height:320px}
  .stage::after{width:380px;height:380px}
  .stage .phone{width:200px}
  .chip.c1{left:0;top:12%}.chip.c2{right:0;bottom:12%}.chip.c3{display:none}
  .feats button{font-size:18px;grid-template-columns:38px 1fr 22px}
  .feats p{padding-left:38px}
  .phones{justify-content:flex-start;overflow-x:auto;scroll-snap-type:x mandatory;padding:20px 24px 30px;margin:0 -24px 24px;scrollbar-width:none}
  .phones::-webkit-scrollbar{display:none}
  .phones .phone{flex-basis:170px;scroll-snap-align:center;margin-top:0!important;animation:none}
  .pills{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
  .pills li,.pills li:nth-child(odd){background:none;border:0;border-bottom:1px solid #eee;border-radius:0;padding:10px 0;font-size:12.5px}
  .pills i{flex:0 0 30px;height:30px;border-radius:9px;background:var(--acc-soft);display:grid;place-items:center;font-size:14px}
}
@media (prefers-reduced-motion:reduce){
  .float,.hero-phone,.stage .phone,.chip,.phones .phone,.stage::after{animation:none}
  .feats li.on .prog{animation:none;width:100%}
  .rv{opacity:1;transform:none;transition:none}
  .phone .scr img{transition:none}
}
'''

def esc(s):
    return html.escape(s, quote=False)

def page(slug, p):
    e = esc
    chips = ''.join(f'<li>{e(c)}</li>' for c in p['chips'])
    foryou = ''.join(f'<li>{e(x)}</li>' for x in p['for_you'])
    feats = ''.join(f'<article class="feat"><h3>{e(h)}</h3><p>{e(t)}</p></article>' for h, t in p['inside'])
    pticks = ''.join(f'<li>{e(x)}</li>' for x in p['programme_ticks'])
    other_slug, other_name, other_desc, other_img, other_pos = p['other']
    faqs = [
        ('Is it suitable for beginners?', 'Yes. It is built for all abilities, so whether you are brand new to lifting or you have been training for years, you can follow it and progress at your own pace.'),
        p['faq_gym'],
        ('How do I access it?', 'Everything lives in the Shape Up app. Once you have checked out, log in to the app and your programme will be there, ready for your first session.'),
        ('Should I get the programme or the membership?', f"If you just want {p['name']}, the programme on its own is £59. If you would like both new programmes plus every other Shape Up programme, meal plans and the community, the membership is £24.99 a month."),
        ('Can I do both new programmes?', 'Absolutely. Island Body V2 and Strength Is Power are both included in the membership, so you can finish one and go straight into the other.'),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(faqs))
    h1a, h1b = p['h1']
    feat_items = ''.join(
        f'<li class="{"on" if i == 0 else ""}" data-img="{img}"><button aria-expanded="{"true" if i == 0 else "false"}"><span class="ic" aria-hidden="true">{ic}</span>{e(h)}<span class="pl" aria-hidden="true">+</span></button><p>{e(d)}</p><span class="prog" aria-hidden="true"></span></li>'
        for i, (ic, h, d, img) in enumerate(APP_FEATS))
    first_img = APP_FEATS[0][3]
    strip_imgs = ['images/app-meals.webp','images/app-today.webp','images/app-home.webp','images/app-log.webp','images/app-habits.webp']
    strip_phones = ''.join(f'<div class="phone"><div class="scr"><img src="{s}" alt="" loading="lazy"></div></div>' for s in strip_imgs)
    pills = ''.join(f'<li><i aria-hidden="true">{ic}</i>{e(n)}</li>' for ic, n in APP_PILLS)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
{GA}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{html.escape(p['desc'])}">
<meta name="rating" content="general">
<title>{e(p['title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@300;500;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body class="{p['theme']}">

<header class="top">
  <nav class="bar" aria-label="Main">
    <a href="/programmes"><img src="images/img-01.webp" alt="Shape Up"></a>
    <a class="btn" href="{p['checkout']}">Get it · £59</a>
  </nav>
</header>

<main>
<section class="hero">
  <div class="wrap hero-grid">
    <div class="copy">
      <span class="pill"><i aria-hidden="true"></i>New programme · out now</span>
      <h1>{e(h1a)}<strong>{e(h1b)}</strong></h1>
      <p class="kicker">{e(p['kicker'])}</p>
      <p class="sub">{e(p['sub'])}</p>
      <ul class="chips">{chips}</ul>
      <div class="cta-row">
        <a class="btn" id="heroBuy" href="{p['checkout']}">Get {e(p['name'])} · £59</a>
        <a class="alt" href="#pricing">Or get it in the membership</a>
      </div>
    </div>
    <div class="hero-art">
      <div class="frame" style="--pos:{p['img_pos']};--pos-m:{p['img_pos_m']}"><img src="{p['img']}" alt="{html.escape(p['img_alt'])}"></div>
      <div class="phone hero-phone" aria-hidden="true"><div class="scr"><img src="images/app-workout.webp" alt=""></div></div>
      <div class="float f1"><b>8</b>week programme</div>
      <div class="float f2"><b>£59</b>one time</div>
    </div>
  </div>
</section>

<section class="foryou">
  <div class="wrap foryou-grid rv">
    <div>
      <p class="eyebrow">Who it's for</p>
      <h2 class="h2">{e(p['for_you_h'][0])}<strong>{e(p['for_you_h'][1])}</strong></h2>
      <p class="tagline">{e(p['for_you_tag'])}</p>
    </div>
    <ul class="list">{foryou}</ul>
  </div>
</section>

<section class="inside">
  <div class="wrap">
    <div class="inside-head">
      <div>
        <p class="eyebrow">What's inside</p>
        <h2 class="h2">Everything you get<strong>in {e(p['name'])}</strong></h2>
      </div>
      <p>Eight weeks of training written by Gabby, laid out session by session so you always know exactly what to do next.</p>
    </div>
    <div class="feat-grid rv">{feats}</div>
  </div>
</section>

<section class="app" id="app">
  <div class="wrap app-grid">
    <div class="rv">
      <p class="eyebrow">Inside the Shape Up app</p>
      <h2 class="h2">Your programme,<strong>in your pocket</strong></h2>
      <p class="app-intro">{e(p['name'])} lives in the Shape Up app, so every session, every set and every bit of progress is right there on your phone.</p>
      <ul class="feats" id="feats">{feat_items}</ul>
    </div>
    <div class="stage" aria-hidden="true">
      <div class="chip c1"><span>📈</span>Log every set</div>
      <div class="phone"><div class="scr"><img id="appScr" src="{first_img}" alt=""></div></div>
      <div class="chip c2"><span>🎥</span>Video demos</div>
      <div class="chip c3"><span>🔥</span>8 weeks</div>
    </div>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <div class="strip-h rv">
      <p class="eyebrow">Everything in one place</p>
      <h2 class="h2">Built to keep you<strong>on track</strong></h2>
    </div>
    <div class="phones" aria-hidden="true">{strip_phones}</div>
    <ul class="pills rv">{pills}</ul>
  </div>
</section>

<section class="note">
  <div class="wrap">
    <div class="note-card">
      <div class="ph"><img src="images/img-19.webp" alt="Gabby"></div>
      <div class="bd">
        <p class="eyebrow">A note from Gabby</p>
        <blockquote>“{e(p['note'])}”</blockquote>
        <cite>Gabby xxx<span>Founder of Shape Up</span></cite>
      </div>
    </div>
  </div>
</section>

<section class="how">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h2 class="h2">Start in<strong>three steps</strong></h2>
    <ol class="steps rv">
      <li><b>Get the programme</b><span>Check out in a couple of minutes, or join the membership to get it included.</span></li>
      <li><b>Open the Shape Up app</b><span>Log in and your programme is waiting for you, laid out week by week.</span></li>
      <li><b>Start week one</b><span>Follow each session, hit your targets and watch your progress build over eight weeks.</span></li>
    </ol>
  </div>
</section>

<section class="pricing" id="pricing">
  <div class="wrap">
    <p class="eyebrow">Choose how you train</p>
    <h2 class="h2">Get started<strong>today</strong></h2>
    <p class="intro">Buy {e(p['name'])} on its own, or get it with both new programmes and everything else in the Shape Up membership.</p>
    <div class="plans">
      <article class="plan">
        <p class="name">{e(p['name'])}</p>
        <p class="what">The programme on its own</p>
        <div class="amount"><b>£59</b><span>one time</span></div>
        <ul>{pticks}</ul>
        <a class="btn btn--line" href="{p['checkout']}">Get {e(p['name'])}</a>
      </article>
      <article class="plan plan--mem">
        <span class="badge">Best value</span>
        <p class="name">Shape Up Membership</p>
        <p class="what">Every programme, plus the full app</p>
        <div class="amount"><b>£24.99</b><span>a month</span></div>
        <ul>
          <li>{e(p['name'])} included</li>
          <li>{e(other_name)} included too</li>
          <li>Every other Shape Up programme</li>
          <li>New content added every month</li>
          <li>Meal plans and barcode food scanner</li>
          <li>Cycle and habit tracking, plus the Shape Up community</li>
        </ul>
        <a class="btn btn--yellow" href="{MEM_MONTHLY}">Join membership</a>
        <a class="annual" href="{MEM_YEARLY}">Or go annual for £199 a year</a>
      </article>
    </div>
  </div>
</section>

<section class="faq">
  <div class="wrap faq-grid">
    <div>
      <p class="eyebrow">FAQ</p>
      <h2 class="h2">Got<strong>questions?</strong></h2>
    </div>
    <div>{faq_html}</div>
  </div>
</section>

<section class="also">
  <div class="wrap">
    <a class="also-card" href="/{other_slug}">
      <div class="ph"><img src="{other_img}" alt="{html.escape(other_name)}" style="object-position:{other_pos}"></div>
      <div class="bd">
        <p class="eyebrow">Also new</p>
        <h3>{e(other_name)}</h3>
        <p>{e(other_desc)}</p>
        <span class="go">See {e(other_name)} →</span>
      </div>
    </a>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <h2 class="h2">Ready to<strong>start?</strong></h2>
    <p>Get {e(p['name'])} for £59, or get both new programmes and everything else with the membership.</p>
    <div class="cta-row">
      <a class="btn" href="{p['checkout']}">Get {e(p['name'])} · £59</a>
      <a class="btn btn--line" href="#pricing">See membership</a>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap foot">
    <span>© 2026 Shape Up with Gabby</span>
    <nav><a href="/programmes">All new programmes</a><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></nav>
  </div>
</footer>

<div class="buybar" id="buyBar" aria-hidden="true">
  <div><b>{e(p['name'])}</b><span>£59 one time</span></div>
  <a class="btn" href="{p['checkout']}" tabindex="-1">Get it</a>
</div>

<script>
(function(){{
  // App spotlight: auto-advances, tap to choose
  var list=document.getElementById('feats'),scr=document.getElementById('appScr');
  if(list&&scr){{
    var items=[].slice.call(list.children),cur=0,timer=null,DUR=4500;
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function set(i){{
      cur=(i+items.length)%items.length;
      items.forEach(function(li,k){{
        var on=k===cur;li.classList.toggle('on',on);li.querySelector('button').setAttribute('aria-expanded',on?'true':'false');
        var b=li.querySelector('.prog');b.style.animation='none';void b.offsetWidth;b.style.animation='';
      }});
      scr.style.opacity=0;
      setTimeout(function(){{scr.src=items[cur].getAttribute('data-img');scr.style.opacity=1;}},reduce?0:220);
    }}
    function play(){{stop();if(reduce)return;list.classList.remove('paused');timer=setInterval(function(){{set(cur+1);}},DUR);}}
    function stop(){{if(timer)clearInterval(timer);timer=null;}}
    items.forEach(function(li,k){{li.querySelector('button').addEventListener('click',function(){{set(k);list.classList.add('paused');stop();}});}});
    items.forEach(function(li){{var im=new Image();im.src=li.getAttribute('data-img');}});
    if('IntersectionObserver' in window){{
      new IntersectionObserver(function(e){{if(e[0].isIntersecting){{if(!list.classList.contains('paused'))play();}}else stop();}},{{threshold:.3}}).observe(list);
    }} else play();
    if(reduce)list.classList.add('paused');
  }}
  // Reveal on scroll
  var rv=[].slice.call(document.querySelectorAll('.rv'));
  if('IntersectionObserver' in window){{
    var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target);}}}});}},{{threshold:.15}});
    rv.forEach(function(el){{io.observe(el);}});
  }} else rv.forEach(function(el){{el.classList.add('in');}});
}})();
(function(){{
  var bar=document.getElementById('buyBar'),hero=document.getElementById('heroBuy'),fin=document.querySelector('.final');
  if(!('IntersectionObserver' in window)||!bar)return;
  var heroVis=true,finVis=false;
  function upd(){{var on=!heroVis&&!finVis;bar.classList.toggle('show',on);bar.setAttribute('aria-hidden',on?'false':'true');bar.querySelector('a').tabIndex=on?0:-1;}}
  new IntersectionObserver(function(e){{heroVis=e[0].isIntersecting;upd();}}).observe(hero);
  new IntersectionObserver(function(e){{finVis=e[0].isIntersecting;upd();}}).observe(fin);
}})();
</script>
</body>
</html>
'''

for slug, p in PAGES.items():
    out = os.path.join(REPO, slug + '.html')
    open(out, 'w').write(page(slug, p))
    print('wrote', out)
