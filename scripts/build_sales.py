"""Builds the two programme sales pages for shapeupapp.co.uk from one template.

Usage (from the repo root): python3 scripts/build_sales.py .
Writes island-body-v2.html and strength-is-power.html into the repo root.

Page order: hero, this is for you if, what you get (programme + app),
results (transformations), checkout (plans + FAQ), final call to action.
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
APP_PILLS = [('💪', 'Workout logger'), ('🎥', 'Exercise video demos'), ('📊', 'PRs and history'), ('🥗', 'Meal plans'),
             ('📷', 'Food logger and scanner'), ('❤️', 'Apple and Google Health'), ('🎯', 'Goal setting'),
             ('📸', 'Progress photos'), ('💧', 'Habit tracking'), ('✅', 'Daily tasks'), ('🌸', 'Cycle tracker'),
             ('📋', 'Check ins'), ('🍴', 'Recipes and favourites')]
TRANSFORMATIONS = [f'images/tf-{i:02d}.webp' for i in range(1, 15)]

PAGES = {
    'island-body-v2': dict(
        title='Island Body V2 | Shape Up with Gabby',
        desc="Island Body V2 is Gabby's revamped 8 week lower body focused strength programme, with upper body conditioning. All abilities. £59, or included in the Shape Up membership.",
        name='Island Body V2', h1=('Island', 'Body V2'), theme='island',
        img='images/ib-hero.webp', img_alt='Gabby in a tropical setting', img_pos='50% 35%', img_pos_m='52% 30%',
        checkout='https://join.shapeupwithgabby.co.uk/p/island-body-v2/one-time',
        lead='New · 8 week programme by Gabby',
        sub="My best selling programme, completely revamped. Lower body focused strength training paired with upper body conditioning, so every week builds on the last.",
        facts=[('8', 'weeks'), ('Lower', 'body focus'), ('All', 'abilities')],
        ticker=['8 weeks', 'Lower body focused strength', 'Upper body conditioning', 'Revamped from the best seller', 'All abilities', 'Gym or home'],
        for_you=[
            "You loved the original Island Body, or always wished you'd done it",
            "You want to build your lower body and glutes with proper strength training",
            "You want a plan that tells you exactly what to do, every single session",
            "You want real progress over eight weeks, not just a sweaty workout",
        ],
        for_you_tag="And yes... it's the big, juicy peach one 🍑",
        inside=[
            ('Revamped from the original', 'The best selling Island Body programme, revised and perfected, with fresh exercises throughout.'),
            ('Lower body focused strength', 'Sessions built to grow and strengthen your lower body and glutes, week after week.'),
            ('Upper body conditioning', 'Balanced with upper body work, so you build a strong, athletic shape all over.'),
            ('Clear progressions', 'Every week builds on the last, so you always know you are moving forward.'),
            ('All abilities catered for', 'Brand new to lifting or training for years, the plan works for you.'),
            ('Gym recommended', 'Best in the gym, but you can follow it at home with a range of weights.'),
        ],
        faq_gym=('Do I need a gym?', 'A gym is recommended, but you can follow Island Body V2 at home as long as you have a range of weights to work with.'),
        programme_ticks=['The full 8 week programme', 'Lower body focus with upper body conditioning', 'Follow it in the Shape Up app'],
        other=('strength-is-power', 'Strength Is Power'),
    ),
    'strength-is-power': dict(
        title='Strength Is Power | Shape Up with Gabby',
        desc="Strength Is Power is Gabby's new 8 week full body strength programme, built around the big compound lifts. All abilities, gym or home. £59, or included in the Shape Up membership.",
        name='Strength Is Power', h1=('Strength', 'Is Power'), theme='strength',
        img='images/sip-hero.webp', img_alt='Gabby in the gym with a barbell', img_pos='42% 45%', img_pos_m='42% 40%',
        checkout='https://join.shapeupwithgabby.co.uk/p/strength-is-power/one-time',
        lead='New · 8 week programme by Gabby',
        sub="Eight weeks built to increase your full body strength. Progressive sessions centred on the big compound lifts, with clear weekly targets so you can watch your numbers go up.",
        facts=[('8', 'weeks'), ('Full', 'body strength'), ('Gym', 'or home')],
        ticker=['8 weeks', 'Full body strength', 'Big compound lifts', 'Weekly targets', 'Simple format', 'All abilities', 'Gym or home'],
        for_you=[
            "You want to get properly strong, not just tired",
            "You've always wanted to feel confident with the big lifts",
            "You want a simple plan that's easy to follow and actually works",
            "You want a strong, athletic shape from head to toe",
        ],
        for_you_tag="Simple format. Proven results. 💪",
        inside=[
            ('Built around compound lifts', 'Sessions centred on the big compound movements, building your confidence every time you lift.'),
            ('Clear weekly targets', 'Targets for every week, so you can watch your numbers go up and see your strength grow.'),
            ('Simple format', 'No guesswork and no overcomplicating. Show up, follow the plan, get stronger.'),
            ('360 full body approach', 'Every part of you gets stronger, to build the shape you dream of.'),
            ('All abilities catered for', 'Brand new to lifting or training for years, the plan works for you.'),
            ('Gym or home', 'Follow it in the gym or at home, whatever suits your week.'),
        ],
        faq_gym=('Do I need a gym?', 'No. You can follow Strength Is Power in the gym or at home.'),
        programme_ticks=['The full 8 week programme', 'Built around the big compound lifts', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2'),
    ),
}

CSS = r'''
:root{
  --ink:#111;--body:#3d3d3d;--muted:#6f6f6f;
  --yellow:#FDE08D;--cream:#FFF7DD;--blue:#62BAF5;--blue-soft:#EAF4FE;
  --head:'Oswald','Arial Narrow',Arial,sans-serif;
  --text:'Poppins',system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  box-sizing:border-box;
}
.island{--acc:#E9B44C;--acc-soft:#F7E6BF}
.strength{--acc:#62BAF5;--acc-soft:#DCEEFC}
*,*::before,*::after{box-sizing:inherit}
html{scroll-behavior:smooth}
body{margin:0;color:var(--ink);font-family:var(--text);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;background:#fff;overflow-x:hidden;padding-bottom:env(safe-area-inset-bottom,0px)}
img{max-width:100%;display:block}
a{color:inherit}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:1240px;margin:0 auto;padding:0 28px}
.big{font-family:var(--head);text-transform:uppercase;font-weight:700;line-height:.92;letter-spacing:-.5px;margin:0}
.big em{font-style:normal;color:var(--acc)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;font:600 13px var(--text);letter-spacing:1.3px;text-transform:uppercase;text-decoration:none;padding:18px 34px;background:var(--yellow);color:var(--ink);transition:transform .15s ease,background .15s ease;border:0;cursor:pointer}
.btn:hover{transform:translateY(-2px);background:#ffd45f}
.btn--ink{background:var(--ink);color:#fff}
.btn--ink:hover{background:#000}
.btn--ghost{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.7);padding:16px 30px}
.btn--ghost:hover{background:#fff;color:var(--ink)}
.btn--line{background:transparent;color:var(--ink);border:1.5px solid var(--ink);padding:16px 30px}
.btn--line:hover{background:var(--ink);color:#fff}

/* Top bar */
.top{position:fixed;top:0;left:0;right:0;z-index:40;padding:calc(env(safe-area-inset-top,0px) + 14px) 18px 0;transition:background .25s ease,box-shadow .25s ease}
.top.solid{background:rgba(17,17,17,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);padding-bottom:12px;box-shadow:0 8px 24px rgba(0,0,0,.18)}
.bar{max-width:1240px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 10px}
.bar img{height:22px;width:auto;filter:brightness(0) invert(1)}
.bar .btn{padding:11px 20px;font-size:11.5px}

/* Hero: full-bleed photo, huge type */
.hero{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:flex-end;color:#fff;overflow:hidden;background:#111}
.hero .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos);transform:scale(1.04);animation:zoom 14s ease-out forwards}
@keyframes zoom{to{transform:scale(1)}}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.35) 45%,rgba(0,0,0,0) 70%),linear-gradient(0deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,0) 45%)}
.hero .wrap{position:relative;z-index:2;width:100%;padding-top:130px;padding-bottom:70px}
.hero .lead{font-size:13px;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin:0 0 14px;color:var(--acc)}
.hero h1{font-family:var(--head);text-transform:uppercase;font-weight:700;font-size:clamp(70px,12vw,176px);line-height:.84;letter-spacing:-2px;margin:0 0 22px}
.hero h1 span{display:block}
.hero h1 span:first-child{font-weight:300}
.hero .sub{font-size:17px;max-width:520px;margin:0 0 28px;color:rgba(255,255,255,.88)}
.hero .ctas{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.facts{display:flex;gap:34px;margin:34px 0 0;padding:22px 0 0;border-top:1px solid rgba(255,255,255,.25);max-width:560px;list-style:none}
.facts b{display:block;font-family:var(--head);font-size:30px;line-height:1;text-transform:uppercase}
.facts span{font-size:11px;letter-spacing:1.4px;text-transform:uppercase;color:rgba(255,255,255,.75)}
.hero .phone{position:absolute;z-index:2;right:6%;bottom:9%;width:210px;--r:4deg}

/* Ticker */
.ticker{background:var(--yellow);overflow:hidden;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink)}
.ticker .track{display:flex;width:max-content;gap:40px;padding:16px 0;animation:tick 34s linear infinite;font-family:var(--head);font-weight:700;font-size:22px;text-transform:uppercase;white-space:nowrap;align-items:center}
.ticker .track i{font-style:normal;font-size:16px}
@keyframes tick{to{transform:translateX(-50%)}}

/* For you */
.foryou{padding:110px 0}
.foryou .big{font-size:clamp(46px,7vw,96px);margin-bottom:46px}
.fy{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;border-top:2px solid var(--ink)}
.fy li{display:grid;grid-template-columns:70px 1fr;gap:10px;padding:26px 26px 26px 0;border-bottom:2px solid var(--ink);font-size:clamp(17px,1.7vw,21px);font-weight:500;line-height:1.35;align-items:start}
.fy li:nth-child(odd){border-right:2px solid var(--ink)}
.fy li:nth-child(even){padding-left:26px}
.fy b{font-family:var(--head);font-size:38px;line-height:1;color:var(--acc);-webkit-text-stroke:1px var(--ink)}
.fy-tag{margin:30px 0 0;font-family:var(--head);font-size:clamp(24px,2.6vw,34px);text-transform:uppercase;font-weight:500}

/* What you get */
.get{background:var(--ink);color:#fff;padding:110px 0 30px}
.get .big{font-size:clamp(46px,7vw,96px)}
.get-head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:50px}
.get-head p{max-width:360px;margin:0;color:rgba(255,255,255,.72)}
.prog{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid rgba(255,255,255,.18)}
.prog div{padding:30px 28px 34px 0;border-bottom:1px solid rgba(255,255,255,.18)}
.prog div:not(:nth-child(3n)){border-right:1px solid rgba(255,255,255,.18)}
.prog div:not(:nth-child(3n+1)){padding-left:28px}
.prog h3{font-family:var(--head);font-weight:700;text-transform:uppercase;font-size:24px;line-height:1.05;margin:0 0 10px}
.prog h3::before{content:"✦";display:block;color:var(--acc);font-size:16px;margin-bottom:14px}
.prog p{margin:0;font-size:14px;color:rgba(255,255,255,.72)}

/* Phone */
.phone{position:relative;background:#0b0b0b;border-radius:40px;padding:8px;box-shadow:0 30px 60px rgba(0,0,0,.35),inset 0 0 0 2px #2c2c2c}
.phone .scr{position:relative;border-radius:32px;overflow:hidden;aspect-ratio:380/826;background:#f4f4f4}
.phone .scr img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s ease}
@keyframes bob{0%,100%{transform:translateY(0) rotate(var(--r,0deg))}50%{transform:translateY(-12px) rotate(var(--r,0deg))}}

/* App spotlight (inside dark section) */
.app{padding:100px 0 40px}
.app-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:60px;align-items:center}
.app .big{font-size:clamp(40px,5.4vw,72px);margin-bottom:18px}
.app-intro{color:rgba(255,255,255,.72);margin:0 0 26px;max-width:460px}
.feats{list-style:none;margin:0;padding:0;border-top:1px solid rgba(255,255,255,.18)}
.feats li{border-bottom:1px solid rgba(255,255,255,.18);position:relative}
.feats button{all:unset;box-sizing:border-box;width:100%;cursor:pointer;display:grid;grid-template-columns:42px 1fr 22px;align-items:center;padding:17px 0;font-family:var(--head);font-weight:500;text-transform:uppercase;font-size:22px;color:rgba(255,255,255,.45);transition:color .2s}
.feats button:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.feats .ic{width:30px;height:30px;border-radius:9px;background:rgba(255,255,255,.08);display:grid;place-items:center;font-size:15px;filter:grayscale(1);opacity:.6;transition:all .2s}
.feats .pl{font-family:var(--text);font-weight:400;font-size:20px;transition:transform .2s}
.feats p{margin:0;max-height:0;overflow:hidden;padding-left:42px;font-size:14px;color:rgba(255,255,255,.75);transition:max-height .35s ease,padding .35s ease}
.feats .pbar{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--acc)}
.feats li.on button{color:#fff}
.feats li.on .ic{background:var(--yellow);filter:none;opacity:1}
.feats li.on .pl{transform:rotate(45deg)}
.feats li.on p{max-height:110px;padding-bottom:17px}
.feats li.on .pbar{animation:progbar 4.5s linear forwards}
.feats.paused li.on .pbar{animation:none;width:100%}
@keyframes progbar{to{width:100%}}
.stage{position:relative;height:640px;display:flex;align-items:center;justify-content:center}
.stage::before{content:"";position:absolute;width:470px;height:470px;border-radius:50%;background:var(--acc)}
.stage::after{content:"";position:absolute;width:560px;height:560px;border-radius:50%;border:2px dashed rgba(255,255,255,.22);animation:spin 60s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.stage .phone{width:270px;z-index:2;animation:bob 7s ease-in-out infinite}
.chip{position:absolute;z-index:3;background:#fff;color:var(--ink);border-radius:16px;padding:10px 14px;box-shadow:0 14px 34px rgba(0,0,0,.3);font-size:12px;font-weight:600;line-height:1.25;display:flex;align-items:center;gap:9px;animation:bob 6s ease-in-out infinite}
.chip span{width:30px;height:30px;border-radius:9px;background:var(--acc-soft);display:grid;place-items:center;font-size:15px}
.chip.c1{top:16%;left:2%}
.chip.c2{bottom:18%;right:0;animation-delay:-2.5s}

/* Phone strip */
.strip{padding:30px 0 110px;overflow:hidden}
.phones{display:flex;justify-content:center;align-items:flex-start;gap:22px;margin:0 0 44px}
.phones .phone{flex:0 0 190px;animation:bob 7s ease-in-out infinite}
.phones .phone:nth-child(1){--r:-6deg;margin-top:70px;animation-delay:-1s}
.phones .phone:nth-child(2){--r:-3deg;margin-top:28px;animation-delay:-3s}
.phones .phone:nth-child(3){margin-top:0;animation-delay:-5s}
.phones .phone:nth-child(4){--r:3deg;margin-top:28px;animation-delay:-2s}
.phones .phone:nth-child(5){--r:6deg;margin-top:70px;animation-delay:-4s}
.pills{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;max-width:860px;margin:0 auto;list-style:none;padding:0}
.pills li{display:flex;align-items:center;gap:8px;border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:8px 16px;font-size:13.5px;font-weight:500;color:#fff}
.pills i{font-style:normal}

/* Results */
.results{background:var(--cream);padding:110px 0}
.res-head{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:40px;align-items:end;margin-bottom:50px}
.results .big{font-size:clamp(56px,9vw,132px)}
.res-head p{margin:0;font-size:16px;color:var(--body)}
.beth{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);background:var(--ink);color:#fff;border-radius:28px;overflow:hidden;margin-bottom:22px}
.beth .ph{position:relative;min-height:520px;background:#fff}
.beth .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.lbl{position:absolute;top:14px;z-index:2;font-size:10px;letter-spacing:1.2px;font-weight:700;padding:5px 10px;border-radius:6px;text-transform:uppercase}
.lbl.b{left:14px;background:#fff;color:var(--ink)}
.lbl.a{left:calc(50% + 12px);background:var(--yellow);color:var(--ink)}
.beth .bd{padding:46px 42px;display:flex;flex-direction:column;justify-content:center}
.beth .who{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:var(--yellow);font-weight:700;margin:0 0 18px}
.beth .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid rgba(255,255,255,.2);border-bottom:1px solid rgba(255,255,255,.2);margin:0 0 26px}
.beth .stats div{padding:20px 0}
.beth .stats div+div{padding-left:18px;border-left:1px solid rgba(255,255,255,.2)}
.beth .stats b{display:block;font-family:var(--head);font-size:clamp(40px,4.4vw,60px);line-height:.9;font-weight:700}
.beth .stats span{font-size:11.5px;color:rgba(255,255,255,.7);text-transform:uppercase;letter-spacing:1px}
.beth blockquote{margin:0 0 14px;font-size:18px;font-weight:500;line-height:1.45}
.beth .extra{margin:0;font-size:14px;color:rgba(255,255,255,.72)}
.tf-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.tf{position:relative;margin:0;border-radius:18px;overflow:hidden;aspect-ratio:1/1;background:#eee}
.tf img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease}
.tf:hover img{transform:scale(1.04)}
.tf .lbl{top:10px;font-size:9px;padding:4px 8px}
.tf .lbl.b{left:10px}.tf .lbl.a{left:calc(50% + 8px)}
.tf.more{display:none}
.tf-grid.all .tf.more{display:block}
.res-foot{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:14px;margin-top:40px}
.res-note{text-align:center;font-size:12px;color:var(--muted);margin:18px 0 0}

/* Checkout */
.checkout{padding:110px 0 90px}
.checkout .big{font-size:clamp(50px,7.4vw,104px);text-align:center}
.checkout .intro{max-width:520px;margin:18px auto 46px;text-align:center;color:var(--body)}
.plans{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:18px;max-width:1000px;margin:0 auto;align-items:stretch}
.plan{border:2px solid var(--ink);border-radius:26px;padding:32px 30px;display:flex;flex-direction:column}
.plan .name{font-family:var(--head);font-size:28px;font-weight:700;text-transform:uppercase;line-height:1;margin:0 0 6px}
.plan .what{font-size:13px;color:var(--muted);margin:0 0 20px}
.plan .amount{display:flex;align-items:baseline;gap:6px;margin-bottom:20px}
.plan .amount b{font-family:var(--head);font-size:64px;font-weight:700;line-height:.9}
.plan .amount span{font-size:13px;color:var(--muted)}
.plan ul{list-style:none;padding:0;margin:0 0 26px;display:grid;gap:9px}
.plan li{display:flex;gap:10px;font-size:14px;line-height:1.4}
.plan li::before{content:"✓";flex:0 0 20px;height:20px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:11px;font-weight:700;margin-top:1px}
.plan .btn{margin-top:auto;width:100%}
.plan--mem{background:var(--ink);color:#fff;position:relative}
.plan--mem .what,.plan--mem .amount span{color:rgba(255,255,255,.7)}
.plan--mem li::before{background:var(--yellow);color:var(--ink)}
.plan--mem .badge{position:absolute;top:-14px;left:28px;background:var(--yellow);color:var(--ink);font-family:var(--head);font-weight:700;font-size:14px;letter-spacing:1px;text-transform:uppercase;padding:5px 12px;border-radius:8px;border:2px solid var(--ink)}
.plan--mem .annual{display:block;text-align:center;margin-top:12px;font-size:12.5px;color:rgba(255,255,255,.85);text-underline-offset:3px}
.faq{max-width:820px;margin:90px auto 0}
.faq h3{font-family:var(--head);font-size:clamp(34px,4vw,48px);text-transform:uppercase;margin:0 0 16px;line-height:1}
.faq details{border-bottom:2px solid var(--ink)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;align-items:center;padding:20px 0;font-weight:600;font-size:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:0 0 30px;height:30px;border-radius:50%;border:2px solid var(--ink);display:grid;place-items:center;font-size:18px;line-height:1;transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg);background:var(--ink);color:#fff}
.faq details p{margin:0 0 20px;color:var(--body);font-size:14.5px}

/* Final */
.final{position:relative;overflow:hidden;background:var(--ink);color:#fff;padding:110px 0;text-align:center}
.final .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos);opacity:.32}
.final .wrap{position:relative}
.final .big{font-size:clamp(56px,9vw,132px);margin-bottom:22px}
.final p{max-width:520px;margin:0 auto 28px;color:rgba(255,255,255,.85)}
.final .ctas{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}
.final .other{display:block;margin-top:26px;font-size:13px;color:rgba(255,255,255,.75);text-underline-offset:4px}

footer{background:var(--ink);color:rgba(255,255,255,.6);padding:20px 0 calc(24px + env(safe-area-inset-bottom,0px));font-size:12px;border-top:1px solid rgba(255,255,255,.12)}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.foot nav{display:flex;gap:18px}
.foot a{text-decoration:none;font-weight:600;color:#fff}

/* Mobile sticky buy bar */
.buybar{display:none}

/* Reveal */
.rv{opacity:0;transform:translateY(30px);transition:opacity .7s ease,transform .7s ease}
.rv.in{opacity:1;transform:none}

@media (max-width:980px){
  .hero .phone{display:none}
  .fy{grid-template-columns:1fr}
  .fy li:nth-child(odd){border-right:0}
  .fy li:nth-child(even){padding-left:0}
  .prog{grid-template-columns:1fr 1fr}
  .prog div{padding:26px 22px 28px 0!important;border-right:0!important}
  .prog div:nth-child(odd){border-right:1px solid rgba(255,255,255,.18)!important}
  .prog div:nth-child(even){padding-left:22px!important}
  .get-head,.res-head{display:block}
  .get-head p,.res-head p{margin-top:16px}
  .app-grid{grid-template-columns:1fr;gap:10px}
  .stage{order:-1;height:480px}
  .stage::before{width:320px;height:320px}
  .stage::after{width:380px;height:380px}
  .stage .phone{width:200px}
  .chip.c1{left:0;top:12%}.chip.c2{right:0;bottom:12%}
  .phones{justify-content:flex-start;overflow-x:auto;scroll-snap-type:x mandatory;padding:20px 28px 30px;margin:0 -28px 24px;scrollbar-width:none}
  .phones::-webkit-scrollbar{display:none}
  .phones .phone{flex-basis:170px;scroll-snap-align:center;margin-top:0!important;animation:none;--r:0deg}
  .beth{grid-template-columns:1fr}
  .beth .ph{min-height:0;aspect-ratio:761/738}
  .beth .bd{padding:30px 24px}
  .tf-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
  .plans{grid-template-columns:1fr;max-width:480px}
  .plan--mem{order:-1}
}
@media (max-width:640px){
  body{padding-bottom:calc(84px + env(safe-area-inset-bottom,0px))}
  .wrap{padding:0 20px}
  .bar .btn{display:none}
  .bar{justify-content:center}
  .hero{min-height:92svh}
  .hero::after{background:linear-gradient(0deg,rgba(0,0,0,.85) 0%,rgba(0,0,0,.45) 50%,rgba(0,0,0,.1) 100%)}
  .hero .bg{object-position:var(--pos-m)}
  .hero .wrap{padding-bottom:40px}
  .hero h1{font-size:clamp(54px,15.5vw,90px);letter-spacing:-1px;overflow-wrap:anywhere}
  .hero .sub{font-size:15px}
  .hero .ctas .btn{width:100%}
  .facts{gap:20px}
  .facts b{font-size:24px}
  .ticker .track{font-size:18px;padding:12px 0}
  .foryou,.results,.checkout,.final{padding:72px 0}
  .get{padding:72px 0 10px}
  .fy li{grid-template-columns:52px 1fr;padding:20px 0;font-size:17px}
  .fy b{font-size:30px}
  .prog{grid-template-columns:1fr}
  .prog div:nth-child(n){padding:22px 0!important;border-right:0!important}
  .feats button{font-size:18px;grid-template-columns:38px 1fr 22px}
  .feats p{padding-left:38px}
  .pills{display:grid;grid-template-columns:1fr 1fr;gap:0 14px}
  .pills li{border:0;border-bottom:1px solid rgba(255,255,255,.14);border-radius:0;padding:10px 0;font-size:12.5px}
  .pills i{flex:0 0 30px;height:30px;border-radius:9px;background:rgba(255,255,255,.08);display:grid;place-items:center;font-size:14px}
  .strip{padding-bottom:72px}
  .phones{margin:0 -20px 24px;padding:20px 20px 30px}
  .beth .stats div+div{padding-left:12px}
  .final .ctas .btn{width:100%}
  .buybar{display:flex;position:fixed;left:10px;right:10px;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:50;align-items:center;justify-content:space-between;gap:12px;background:var(--ink);color:#fff;border-radius:20px;padding:10px 10px 10px 18px;box-shadow:0 14px 34px rgba(0,0,0,.35);transform:translateY(140%);transition:transform .25s ease;border:1px solid rgba(255,255,255,.12)}
  .buybar.show{transform:none}
  .buybar b{display:block;font-family:var(--head);font-size:17px;text-transform:uppercase;line-height:1.1}
  .buybar span{font-size:11.5px;color:rgba(255,255,255,.75)}
  .buybar .btn{padding:12px 18px;font-size:11.5px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .hero .bg,.ticker .track,.stage .phone,.chip,.phones .phone,.stage::after,.hero .phone{animation:none}
  .feats li.on .pbar{animation:none;width:100%}
  .rv{opacity:1;transform:none;transition:none}
  .btn,.buybar,.tf img,.phone .scr img{transition:none}
}
'''


def esc(s):
    return html.escape(s, quote=False)


def page(slug, p):
    e = esc
    h1a, h1b = p['h1']
    facts = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in p['facts'])
    tick_items = ''.join(f'<span>{e(x)}</span><i aria-hidden="true">✦</i>' for x in p['ticker'])
    ticker = tick_items * 2
    fy = ''.join(f'<li><b>{i:02d}</b>{e(x)}</li>' for i, x in enumerate(p['for_you'], 1))
    prog = ''.join(f'<div><h3>{e(h)}</h3><p>{e(t)}</p></div>' for h, t in p['inside'])
    feat_items = ''.join(
        f'<li class="{"on" if i == 0 else ""}" data-img="{img}"><button aria-expanded="{"true" if i == 0 else "false"}"><span class="ic" aria-hidden="true">{ic}</span>{e(h)}<span class="pl" aria-hidden="true">+</span></button><p>{e(d)}</p><span class="pbar" aria-hidden="true"></span></li>'
        for i, (ic, h, d, img) in enumerate(APP_FEATS))
    strip_imgs = ['images/app-meals.webp', 'images/app-today.webp', 'images/app-home.webp', 'images/app-log.webp', 'images/app-habits.webp']
    strip = ''.join(f'<div class="phone"><div class="scr"><img src="{s}" alt="" loading="lazy"></div></div>' for s in strip_imgs)
    pills = ''.join(f'<li><i aria-hidden="true">{ic}</i>{e(n)}</li>' for ic, n in APP_PILLS)
    tfs = ''.join(
        f'<figure class="tf rv{" more" if i >= 8 else ""}"><img src="{src}" alt="Shape Up member before and after" loading="lazy"><span class="lbl b">Before</span><span class="lbl a">After</span></figure>'
        for i, src in enumerate(TRANSFORMATIONS))
    pticks = ''.join(f'<li>{e(x)}</li>' for x in p['programme_ticks'])
    other_slug, other_name = p['other']
    faqs = [
        ('Is it suitable for beginners?', 'Yes. It is built for all abilities, so whether you are brand new to lifting or you have been training for years, you can follow it and progress at your own pace.'),
        p['faq_gym'],
        ('How do I access it?', 'Everything lives in the Shape Up app. Once you have checked out, log in to the app and your programme will be there, ready for your first session.'),
        ('Should I get the programme or the membership?', f"If you just want {p['name']}, the programme on its own is £59. If you would like both new programmes plus every other Shape Up programme, meal plans and the community, the membership is £24.99 a month."),
        ('Can I do both new programmes?', 'Absolutely. Island Body V2 and Strength Is Power are both included in the membership, so you can finish one and go straight into the other.'),
    ]
    faq_html = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(faqs))

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

<header class="top" id="top">
  <nav class="bar" aria-label="Main">
    <a href="/programmes"><img src="images/img-01.webp" alt="Shape Up"></a>
    <a class="btn" href="{p['checkout']}">Get it · £59</a>
  </nav>
</header>

<main>
<!-- HERO -->
<section class="hero" style="--pos:{p['img_pos']};--pos-m:{p['img_pos_m']}">
  <img class="bg" src="{p['img']}" alt="{html.escape(p['img_alt'])}">
  <div class="wrap">
    <p class="lead">{e(p['lead'])}</p>
    <h1><span>{e(h1a)}</span><span>{e(h1b)}</span></h1>
    <p class="sub">{e(p['sub'])}</p>
    <div class="ctas">
      <a class="btn" id="heroBuy" href="{p['checkout']}">Get {e(p['name'])} · £59</a>
      <a class="btn btn--ghost" href="#checkout">Or get it in the membership</a>
    </div>
    <ul class="facts">{facts}</ul>
  </div>
  <div class="phone" aria-hidden="true" style="animation:bob 7s ease-in-out infinite"><div class="scr"><img src="images/app-workout.webp" alt=""></div></div>
</section>

<div class="ticker" aria-hidden="true"><div class="track">{ticker}</div></div>

<!-- THIS IS FOR YOU IF -->
<section class="foryou">
  <div class="wrap">
    <h2 class="big rv">This is for you<br><em>if...</em></h2>
    <ul class="fy rv">{fy}</ul>
    <p class="fy-tag rv">{e(p['for_you_tag'])}</p>
  </div>
</section>

<!-- WHAT YOU GET -->
<section class="get">
  <div class="wrap">
    <div class="get-head rv">
      <h2 class="big">What<br>you <em>get</em></h2>
      <p>Eight weeks of training written by Gabby, laid out session by session in the Shape Up app, so you always know exactly what to do next.</p>
    </div>
    <div class="prog rv">{prog}</div>
  </div>

  <div class="app" id="app">
    <div class="wrap app-grid">
      <div class="rv">
        <h2 class="big">Your programme,<br><em>in your pocket</em></h2>
        <p class="app-intro">{e(p['name'])} lives in the Shape Up app, so every session, every set and every bit of progress is right there on your phone.</p>
        <ul class="feats" id="feats">{feat_items}</ul>
      </div>
      <div class="stage" aria-hidden="true">
        <div class="chip c1"><span>📈</span>Log every set</div>
        <div class="phone"><div class="scr"><img id="appScr" src="{APP_FEATS[0][3]}" alt=""></div></div>
        <div class="chip c2"><span>🎥</span>Video demos</div>
      </div>
    </div>
  </div>

  <div class="strip">
    <div class="wrap">
      <div class="phones" aria-hidden="true">{strip}</div>
      <ul class="pills rv">{pills}</ul>
    </div>
  </div>
</section>

<!-- RESULTS -->
<section class="results" id="results">
  <div class="wrap">
    <div class="res-head rv">
      <h2 class="big">Real women.<br><em>Real results.</em></h2>
      <p>Every one of these women trained with Shape Up. Different starting points, different goals, same app and the same community behind them.</p>
    </div>

    <article class="beth rv">
      <div class="ph"><img src="images/tf-beth.webp" alt="Beth's before and after, side view, four weeks apart" loading="lazy"><span class="lbl b">Before</span><span class="lbl a">After</span></div>
      <div class="bd">
        <p class="who">Beth · Shape Up member</p>
        <div class="stats">
          <div><b>4</b><span>weeks</span></div>
          <div><b>1.5kg</b><span>down</span></div>
          <div><b>4.5cm</b><span>off her waist</span></div>
        </div>
        <blockquote>“My mindset again is feeling good and positive about the gym and I've really enjoyed the set of exercises as I feel they've allowed me to push myself.”</blockquote>
        <p class="extra">“This group really have made things much easier to stick to and push through all the challenges that crop up!”</p>
      </div>
    </article>

    <div class="tf-grid" id="tfGrid">{tfs}</div>
    <div class="res-foot">
      <button class="btn btn--line" id="tfMore" type="button">See more results</button>
      <a class="btn btn--ink" href="#checkout">Start your transformation</a>
    </div>
    <p class="res-note">Results from Shape Up members across Gabby's programmes. Everyone's results are different.</p>
  </div>
</section>

<!-- CHECKOUT -->
<section class="checkout" id="checkout">
  <div class="wrap">
    <h2 class="big rv">Get <em>started</em></h2>
    <p class="intro">Buy {e(p['name'])} on its own, or get it with both new programmes and everything else in the Shape Up membership.</p>
    <div class="plans rv">
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
        <a class="btn" href="{MEM_MONTHLY}">Join membership</a>
        <a class="annual" href="{MEM_YEARLY}">Or go annual for £199 a year</a>
      </article>
    </div>

    <div class="faq">
      <h3>Questions</h3>
      {faq_html}
    </div>
  </div>
</section>

<!-- FINAL -->
<section class="final" style="--pos:{p['img_pos']}">
  <img class="bg" src="{p['img']}" alt="" loading="lazy">
  <div class="wrap">
    <h2 class="big">Your 8 weeks<br><em>start now</em></h2>
    <p>Get {e(p['name'])} for £59, or get both new programmes and everything else with the membership.</p>
    <div class="ctas">
      <a class="btn" id="finalBuy" href="{p['checkout']}">Get {e(p['name'])} · £59</a>
      <a class="btn btn--ghost" href="#checkout">See membership</a>
    </div>
    <a class="other" href="/{other_slug}">Also new: {e(other_name)} →</a>
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
  var io=('IntersectionObserver' in window);
  // Solid header once past the hero
  var top=document.getElementById('top'),hero=document.querySelector('.hero');
  if(io)new IntersectionObserver(function(e){{top.classList.toggle('solid',!e[0].isIntersecting);}},{{rootMargin:'-80px 0px 0px 0px'}}).observe(hero);

  // App spotlight: auto-advances, tap to choose
  var list=document.getElementById('feats'),scr=document.getElementById('appScr');
  if(list&&scr){{
    var items=[].slice.call(list.children),cur=0,timer=null,DUR=4500;
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function set(i){{
      cur=(i+items.length)%items.length;
      items.forEach(function(li,k){{
        var on=k===cur;li.classList.toggle('on',on);li.querySelector('button').setAttribute('aria-expanded',on?'true':'false');
        var b=li.querySelector('.pbar');b.style.animation='none';void b.offsetWidth;b.style.animation='';
      }});
      scr.style.opacity=0;
      setTimeout(function(){{scr.src=items[cur].getAttribute('data-img');scr.style.opacity=1;}},reduce?0:220);
    }}
    function play(){{stop();if(reduce)return;timer=setInterval(function(){{set(cur+1);}},DUR);}}
    function stop(){{if(timer)clearInterval(timer);timer=null;}}
    items.forEach(function(li,k){{li.querySelector('button').addEventListener('click',function(){{set(k);list.classList.add('paused');stop();}});}});
    items.forEach(function(li){{var im=new Image();im.src=li.getAttribute('data-img');}});
    if(reduce)list.classList.add('paused');
    if(io)new IntersectionObserver(function(e){{if(e[0].isIntersecting){{if(!list.classList.contains('paused'))play();}}else stop();}},{{threshold:.3}}).observe(list);
    else play();
  }}

  // More results
  var more=document.getElementById('tfMore'),grid=document.getElementById('tfGrid');
  if(more&&grid)more.addEventListener('click',function(){{grid.classList.add('all');grid.querySelectorAll('.rv').forEach(function(el){{el.classList.add('in');}});more.remove();}});

  // Reveal on scroll
  var rv=[].slice.call(document.querySelectorAll('.rv'));
  if(io){{
    var ob=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');ob.unobserve(x.target);}}}});}},{{threshold:.12}});
    rv.forEach(function(el){{ob.observe(el);}});
  }} else rv.forEach(function(el){{el.classList.add('in');}});

  // Mobile buy bar: shows between the hero and final buttons
  var bar=document.getElementById('buyBar'),hb=document.getElementById('heroBuy'),fb=document.getElementById('finalBuy');
  if(io&&bar){{
    var hv=true,fv=false;
    function upd(){{var on=!hv&&!fv;bar.classList.toggle('show',on);bar.setAttribute('aria-hidden',on?'false':'true');bar.querySelector('a').tabIndex=on?0:-1;}}
    new IntersectionObserver(function(e){{hv=e[0].isIntersecting;upd();}}).observe(hb);
    new IntersectionObserver(function(e){{fv=e[0].isIntersecting;upd();}}).observe(fb);
  }}
}})();
</script>
</body>
</html>
'''


for slug, p in PAGES.items():
    out = os.path.join(REPO, slug + '.html')
    open(out, 'w').write(page(slug, p))
    print('wrote', out)
