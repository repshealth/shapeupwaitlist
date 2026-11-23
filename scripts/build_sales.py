"""Builds the two programme sales pages for shapeupapp.co.uk from one template.

Usage (from the repo root): python3 scripts/build_sales.py .
Writes one sales page per programme (see PAGES) into the repo root.

Design follows the Shape Up homepage (cream/yellow/blue, Oswald light+bold headings,
blue-bordered phone mockups, tilted blue banner, wave dividers, yellow footer).
Page order: hero, this is for you if, what you get (programme + app),
results (transformations), checkout (plans), FAQ, final call to action.
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
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1394121145302064');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1394121145302064&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
'''

MEM_MONTHLY = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership/monthly'
MEM_YEARLY = 'https://join.shapeupwithgabby.co.uk/p/shape-up-membership-7-day-free-trial/yearly'
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
# Same set as the homepage carousel: one front view per member, no repeats
TRANSFORMATIONS = [f'images/{n}.webp' for n in ['img-26', 'img-27', 'tf-s01', 'img-28', 'img-31', 'tf-s02', 'img-34', 'img-35', 'tf-s03', 'img-37', 'tf-n01', 'tf-s04', 'tf-n02', 'tf-n03', 'tf-s05', 'tf-n04', 'tf-n05', 'tf-s06', 'tf-n06', 'tf-n07', 'tf-s07', 'tf-n08', 'tf-n09', 'tf-s08', 'tf-n10', 'tf-n11', 'tf-s09', 'tf-n12', 'tf-n13', 'tf-s10', 'tf-n14', 'tf-s11', 'tf-s12', 'tf-s13']]
SITE = 'https://shapeupapp.co.uk'
# Desktop hero: where to centre each photo inside the right-hand panel so faces stay in view
POS_D = {'images/ib-hero.webp': '53% 0%', 'images/sip-hero.webp': '13% 0%', 'images/img-21.webp': '13% 0%',
         'images/img-22.webp': '37% 0%', 'images/img-23.webp': '42% 0%', 'images/img-19.webp': '46% 0%',
         'images/img-20.webp': '50% 60%'}

KIT_FAQ = ('What equipment do I need?', 'Every session is laid out in the Shape Up app with a video demo for each exercise, so you can see exactly what kit you need before you start.')
MORE_PAGES = {
    'hot-girl-summer': dict(
        title='10 Week Hot Girl Summer | Shape Up with Gabby',
        desc="Hot Girl Summer is Gabby's 10 week programme: progressive training plus flexible nutrition, gym or home. £59, or included in the Shape Up membership.",
        name='Hot Girl Summer', h1=('Hot Girl', 'Summer'), theme='strength', hero_h=('Hot Girl', 'Summer.'), badge='HOT GIRL SUMMER · 10 WEEKS · ',
        img='images/img-20.webp', img_alt='Shape Up members on a group trip', img_pos='50% 40%', img_pos_m='50% 35%',
        checkout='https://join.shapeupwithgabby.co.uk/p/10-week-hot-girl-summer-programme/one-time',
        sub="Ten weeks of progressive training plus flexible nutrition, so you can actually enjoy the summer you're training for.",
        facts=[('10', 'weeks'), ('Gym', 'or home'), ('Flexible', 'nutrition')],
        ticker=['10 weeks', 'Progressive training', 'Flexible nutrition', 'Gym or home', 'All abilities', 'Enjoy your summer'],
        for_you=[
            "You want to feel your best this summer without living on salad",
            "You want a plan that gets a little harder every week, so you keep progressing",
            "You want food to fit your life, not the other way round",
            "You want to train in the gym, at home, or a mix of both",
        ],
        for_you_tag="Train hard, still enjoy the summer ☀️",
        inside=[
            ('Ten week plan', 'Ten weeks of training written by Gabby, laid out session by session.'),
            ('Progressive training', 'Every week builds on the last, so you keep moving forward instead of standing still.'),
            ('Flexible nutrition', "Eat in a way that fits real life, holidays and nights out included."),
            ('Gym or home', 'Follow it in the gym or at home, whatever suits your week.'),
            ('All abilities catered for', 'Brand new to training or training for years, the plan works for you.'),
            ('Enjoy the summer', "Built so you can enjoy the summer you've been training for."),
        ],
        faq_gym=('Do I need a gym?', 'No. Hot Girl Summer has gym and home options, so you can train wherever suits you.'),
        programme_ticks=['The full 10 week programme', 'Progressive training plus flexible nutrition', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2'),
        intro='Ten weeks of training written by Gabby, laid out session by session in the Shape Up app.',
        trust='10 week structured programme', final_h=('Your 10 weeks', 'start now'), no_phone=True,
    ),
    'shred-in-28': dict(
        title='Shred in 28 | Shape Up with Gabby',
        desc="Shred in 28 is Gabby's 28 day programme, 4 days a week, to get fitter, leaner and stronger. £28, or included in the Shape Up membership.",
        name='Shred in 28', h1=('Shred', 'in 28'), theme='island', hero_h=('Shred', 'in 28.'), badge='SHRED IN 28 · 4 DAYS A WEEK · ',
        img='images/img-21.webp', img_alt='Gabby in the gym with a barbell', img_pos='55% 40%', img_pos_m='55% 35%',
        checkout='https://join.shapeupwithgabby.co.uk/p/summer-shred-in-28/one-time', price='28',
        sub="Four weeks to get fitter, leaner and stronger, structured so every session builds on the last.",
        facts=[('28', 'days'), ('4 days', 'a week'), ('All', 'abilities')],
        ticker=['28 days', '4 days a week', 'Fitter', 'Leaner', 'Stronger', 'Every session builds on the last'],
        for_you=[
            "You want a short, focused block with a clear finish line",
            "You can commit to four sessions a week for four weeks",
            "You want to get fitter, leaner and stronger, fast",
            "You want a plan that tells you exactly what to do, every session",
        ],
        for_you_tag="28 days. Let's go 🔥",
        inside=[
            ('28 day plan', 'Four focused weeks with a clear start and finish line.'),
            ('4 days a week', 'Four sessions a week that fit around real life.'),
            ('Fitter, leaner, stronger', 'Built to improve your fitness, strength and shape in a short space of time.'),
            ('Builds every session', 'Structured so every session builds on the last.'),
            ('All abilities catered for', 'Brand new to training or training for years, the plan works for you.'),
            ('Clear and simple', 'Open the app, follow the session, tick it off.'),
        ],
        faq_gym=KIT_FAQ,
        programme_ticks=['The full 28 day programme', '4 sessions a week', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2'),
        intro='28 days of training written by Gabby, laid out session by session in the Shape Up app.',
        trust='28 day structured programme', final_h=('Your 28 days', 'start now'),
    ),
    'sas-strength-and-sustain': dict(
        title='SAS: Strength & Sustain | Shape Up with Gabby',
        desc="SAS: Strength & Sustain is Gabby's 8 week, 4 day split programme of heavy compound lifts and conditioning. £59, or included in the Shape Up membership.",
        name='SAS: Strength & Sustain', short='SAS', h1=('SAS', 'Strength & Sustain'), theme='strength', hero_h=('Strength &', 'Sustain.'), badge='SAS · STRENGTH & SUSTAIN · ',
        img='images/img-22.webp', img_alt='Gabby carrying a weighted pack', img_pos='40% 40%', img_pos_m='40% 40%',
        checkout='https://join.shapeupwithgabby.co.uk/p/8-week-sas-strength-and-sustain/one-time',
        sub="Heavy compound lifts and conditioning circuits, built to make strength a habit rather than a phase.",
        facts=[('8', 'weeks'), ('4 day', 'split'), ('Strength', '+ conditioning')],
        ticker=['8 weeks', '4 day split', 'Heavy compound lifts', 'Conditioning circuits', 'Strength as a habit', 'All abilities'],
        for_you=[
            "You want to lift heavier and feel properly strong",
            "You want conditioning that keeps your fitness up too",
            "You want strength to become a habit, not a phase",
            "You can commit to four sessions a week",
        ],
        for_you_tag="Strong today, strong for good 💪",
        inside=[
            ('Heavy compound lifts', 'Sessions built around the big lifts, so your strength keeps climbing.'),
            ('Conditioning circuits', 'Conditioning work to keep your fitness and stamina up alongside your strength.'),
            ('4 day split', 'Four sessions a week, each with a clear focus.'),
            ('Built to last', 'Designed to make strength a habit rather than a phase.'),
            ('All abilities catered for', 'Brand new to lifting or training for years, the plan works for you.'),
            ('Eight week plan', 'Eight weeks of training written by Gabby, laid out session by session.'),
        ],
        faq_gym=KIT_FAQ,
        programme_ticks=['The full 8 week programme', 'Heavy compound lifts and conditioning', 'Follow it in the Shape Up app'],
        other=('strength-is-power', 'Strength Is Power'),
    ),
    'glute-programme': dict(
        title='8 Week Glute Programme | Shape Up with Gabby',
        desc="The 8 Week Glute Programme is Gabby's 4 day split built to grow and strengthen your glutes. £59, or included in the Shape Up membership.",
        name='Glute Programme', h1=('Glute', 'Programme'), theme='strength', hero_h=('Glute', 'Programme.'), badge='GLUTE PROGRAMME · 8 WEEKS · ',
        img='images/img-23.webp', img_alt='Gabby holding dumbbells', img_pos='55% 25%', img_pos_m='50% 20%',
        checkout='https://join.shapeupwithgabby.co.uk/p/8-week-glute-programme/one-time',
        sub="Eight weeks on a 4 day split, built to grow and strengthen your glutes, with sessions that progress week on week.",
        facts=[('8', 'weeks'), ('4 day', 'split'), ('Glute', 'focus')],
        ticker=['8 weeks', '4 day split', 'Glute focused', 'Progressive sessions', 'All abilities'],
        for_you=[
            "You want to build and strengthen your glutes",
            "You want a lower body plan that actually progresses",
            "You can commit to four sessions a week",
            "You want to know exactly what to do, every session",
        ],
        for_you_tag="Peach goals, sorted 🍑",
        inside=[
            ('Glute focused', 'Every week is built around growing and strengthening your glutes.'),
            ('4 day split', 'Four sessions a week, each with a clear focus.'),
            ('Progressive sessions', 'Sessions progress week on week, so you keep getting stronger.'),
            ('Eight week plan', 'Eight weeks of training written by Gabby, laid out session by session.'),
            ('All abilities catered for', 'Brand new to lifting or training for years, the plan works for you.'),
            ('Demos for every move', 'A video demo for every exercise, so you know you are doing it right.'),
        ],
        faq_gym=KIT_FAQ,
        programme_ticks=['The full 8 week programme', 'Glute focused 4 day split', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2'),
    ),
    'reset-and-shred': dict(
        title='Reset & Shred | Shape Up with Gabby',
        desc="Reset & Shred is Gabby's programme to reset your routine and get back on track, with structured training that builds week on week. £49, or included in the Shape Up membership.",
        name='Reset & Shred', h1=('Reset', '& Shred'), theme='island', hero_h=('Reset', '& Shred.'), badge='RESET & SHRED · SHAPE UP · ',
        img='images/img-19.webp', img_alt='Gabby in training kit', img_pos='60% 25%', img_pos_m='55% 20%',
        checkout='https://join.shapeupwithgabby.co.uk/p/september-reset-shred/one-time', price='49',
        sub="Reset your routine and get back on track, with structured training that builds week on week.",
        facts=[('Reset', 'your routine'), ('Structured', 'training'), ('All', 'abilities')],
        ticker=['Reset your routine', 'Get back on track', 'Structured training', 'Builds week on week', 'All abilities'],
        for_you=[
            "You've fallen out of your routine and want to get back on track",
            "You want structure, so you never have to wonder what to do",
            "You want training that builds week on week",
            "You want a fresh start with Gabby behind you",
        ],
        for_you_tag="Fresh start, starting now ✨",
        inside=[
            ('Reset your routine', 'A clear plan to get you back into a routine that sticks.'),
            ('Structured training', 'Every session laid out for you, so you just show up and follow it.'),
            ('Builds week on week', 'Each week builds on the last, so you keep moving forward.'),
            ('All abilities catered for', 'Brand new to training or getting back into it, the plan works for you.'),
            ('Demos for every move', 'A video demo for every exercise, so you know you are doing it right.'),
            ('In the Shape Up app', 'Your sessions, tasks and progress all in one place.'),
        ],
        faq_gym=KIT_FAQ,
        programme_ticks=['The full Reset & Shred programme', 'Structured training, week on week', 'Follow it in the Shape Up app'],
        other=('island-body-v2', 'Island Body V2'),
        intro='Training written by Gabby, laid out session by session in the Shape Up app.',
        trust='Structured programme', final_h=('Your reset', 'starts now'),
    ),
}

PAGES = {
    'island-body-v2': dict(
        title='Island Body V2 | Shape Up with Gabby',
        desc="Island Body V2 is Gabby's revamped 8 week lower body focused strength programme, with upper body conditioning. All abilities. £59, or included in the Shape Up membership.",
        name='Island Body V2', h1=('Island', 'Body V2'), theme='island', hero_h=('Island Body', 'V2.'), stat=('8 weeks', 'Lower body focus'), badge='ISLAND BODY V2 · 8 WEEKS · ',
        img='images/ib-hero.webp', img_alt='Gabby in a tropical setting', img_pos='50% 30%', img_pos_m='50% 25%',
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
        new=True,
    ),
    'strength-is-power': dict(
        title='Strength Is Power | Shape Up with Gabby',
        desc="Strength Is Power is Gabby's new 8 week full body strength programme, built around the big compound lifts. All abilities, gym or home. £59, or included in the Shape Up membership.",
        name='Strength Is Power', h1=('Strength', 'Is Power'), theme='strength', hero_h=('Strength', 'is power.'), stat=('8 weeks', 'Full body strength'), badge='STRENGTH IS POWER · 8 WEEKS · ',
        img='images/sip-hero.webp', img_alt='Gabby in the gym with a barbell', img_pos='40% 45%', img_pos_m='42% 40%',
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
        new=True,
    ),
}
PAGES.update(MORE_PAGES)

CSS = r'''
:root{
  --ink:#121212;--body:#3d3d3d;--muted:#6f6f6f;
  --yellow:#FDE08D;--cream:#FFF7DD;--blue:#62BAF5;--blue-soft:#EAF4FE;--blue-line:#9FD2F8;
  --head:'Oswald','Arial Narrow',Arial,sans-serif;
  --text:'Poppins',system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  box-sizing:border-box;
}
*,*::before,*::after{box-sizing:inherit}
html{scroll-behavior:smooth;scroll-padding-top:90px;overflow-x:clip}
body{margin:0;color:var(--ink);font-family:var(--text);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased;background:#fff;overflow-x:hidden;padding-bottom:env(safe-area-inset-bottom,0px)}
main{overflow-x:clip}
img{max-width:100%;display:block}
a{color:inherit}
:focus-visible{outline:3px solid var(--blue);outline-offset:3px}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.h2{font-family:var(--head);text-transform:uppercase;font-size:clamp(36px,5vw,58px);line-height:1.02;margin:0;font-weight:300;letter-spacing:-.5px}
.h2 strong{font-weight:700;display:block}
.eyebrow{font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
.intro{font-size:14px;line-height:1.55;margin:0;max-width:320px}
.head-row{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;margin-bottom:44px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;font:600 13px var(--text);letter-spacing:1px;text-transform:uppercase;text-decoration:none;padding:15px 34px;border:1.5px solid transparent;cursor:pointer;transition:transform .15s ease;background:var(--blue);color:#fff}
.btn:hover{transform:translateY(-1px)}
.btn--yellow{background:var(--yellow);color:var(--ink)}
.btn--ink{background:var(--ink);color:#fff}
.btn--outline{background:#fff;border-color:var(--ink);color:var(--ink)}
.wave{display:block;width:100%;height:70px;margin-bottom:-1px}

/* Header */
.top{position:fixed;top:0;left:0;right:0;z-index:50;padding:calc(env(safe-area-inset-top,0px) + 12px) 24px 0}
.nav{max-width:1220px;margin:0 auto;background:rgba(255,253,245,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-radius:999px;box-shadow:0 6px 24px rgba(180,150,60,.12);display:flex;align-items:center;justify-content:space-between;padding:10px 10px 10px 28px;gap:16px}
.nav .logo img{height:26px;width:auto}
.nav ul{list-style:none;display:flex;gap:28px;margin:0;padding:0}
.nav ul a{text-decoration:none;font-weight:600;font-size:13px}
.nav .btn{padding:13px 24px}

/* Hero: full-bleed photo with brand flair */
.hero{position:relative;min-height:100vh;min-height:100svh;display:flex;flex-direction:column;justify-content:flex-end;color:#fff;overflow:hidden;background:#1d2a33}
.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos);transform:scale(1.06);animation:zoom 16s ease-out forwards;z-index:0}
@keyframes zoom{to{transform:scale(1)}}
.hero-shade{position:absolute;inset:0;z-index:1;background:radial-gradient(45% 55% at 0% 100%,rgba(98,186,245,.55) 0%,rgba(98,186,245,0) 70%),linear-gradient(90deg,rgba(12,32,48,.78) 0%,rgba(12,32,48,.5) 38%,rgba(12,32,48,.08) 64%,rgba(12,32,48,0) 80%),linear-gradient(0deg,rgba(12,32,48,.55) 0%,rgba(12,32,48,0) 38%)}
.hero-in{position:relative;z-index:3;width:100%;max-width:1180px;margin:0 auto;padding:150px 24px 150px}
.rating{display:inline-flex;align-items:center;gap:10px;background:#fff;color:var(--ink);border-radius:999px;padding:6px 14px 6px 6px;font-size:12px;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,.18);margin:0 0 22px}
.rating .avs{display:flex}.rating .avs img{width:24px;height:24px;border-radius:50%;border:2px solid #fff;object-fit:cover;margin-left:-7px}.rating .avs img:first-child{margin-left:0}
.rating .st{color:#F6C21B;letter-spacing:1px}
.hero h1{font-family:var(--head);text-transform:uppercase;margin:0 0 24px;line-height:.86;letter-spacing:-1px}
.hero h1 .l1{display:block;font-weight:700;font-size:clamp(56px,7vw,104px);text-shadow:0 6px 30px rgba(0,0,0,.25)}
.hero h1 .l2{position:relative;display:inline-block;font-weight:700;font-size:clamp(84px,11vw,170px);color:var(--yellow);padding-bottom:10px}
.hero h1.t-strength .l2{text-transform:none;font-size:clamp(70px,8.6vw,128px)}
.scribble{position:absolute;left:-2%;bottom:-6px;width:104%;height:28px;overflow:visible}
.scribble path{fill:none;stroke:var(--blue);stroke-width:7;stroke-linecap:round;stroke-dasharray:520;stroke-dashoffset:520;animation:draw 1.4s .6s ease forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.hero .lead{font-size:17px;line-height:1.6;font-weight:500;max-width:480px;margin:0 0 24px;color:rgba(255,255,255,.92)}
.chips-row{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 30px;padding:0;list-style:none}
.chips-row li{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.35);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-radius:999px;padding:9px 16px;font-size:12.5px;font-weight:600}
.chips-row li b{color:var(--yellow);font-weight:700;margin-right:4px}
.hero .ctas{display:flex;gap:14px;flex-wrap:wrap}
.btn--hero{background:var(--yellow);color:var(--ink);padding:18px 34px;font-size:13.5px;box-shadow:0 14px 30px rgba(0,0,0,.25)}
.btn--clear{background:transparent;color:#fff;border-color:#fff;padding:18px 32px;font-size:13.5px}
.btn--clear:hover{background:rgba(255,255,255,.14)}
.hero .price{margin:16px 0 0;font-size:13px;font-weight:500;color:rgba(255,255,255,.85)}
.hero-phone{position:absolute;z-index:3;right:7%;bottom:150px;width:200px;--r:5deg}
.hero-price{position:absolute;z-index:4;right:calc(7% + 160px);bottom:300px;background:#fff;color:var(--ink);border-radius:18px;padding:12px 16px;box-shadow:0 16px 36px rgba(0,0,0,.25);font-size:12px;font-weight:600;line-height:1.25;animation:bob 6s ease-in-out infinite;animation-delay:-2s}
.hero-price b{display:block;font-family:var(--head);font-size:28px;line-height:1}
.hero .spark{position:absolute;z-index:2;color:var(--yellow);font-size:26px;line-height:1;animation:twinkle 3.2s ease-in-out infinite;pointer-events:none}
.hero .spark.s1{top:24%;left:46%}.hero .spark.s2{top:58%;left:52%;font-size:18px;animation-delay:-1.1s}.hero .spark.s3{top:16%;left:8%;font-size:16px;animation-delay:-2.2s}
@keyframes twinkle{0%,100%{opacity:.2;transform:scale(.7) rotate(0)}50%{opacity:1;transform:scale(1.15) rotate(20deg)}}
.hero{clip-path:polygon(0 0,100% 0,100% calc(100% - 3.6vw - 24px),0 calc(100% - 24px))}
.strip.strip--hero{margin-top:-118px;margin-bottom:-30px;z-index:5}
@media (max-width:640px){.strip.strip--hero{margin-top:-80px}}
/* Desktop: sharp photo panel on the right, starting below the nav, over a blurred copy */
.hero-blur{display:none}
.hero.no-phone .hero-phone,.hero.no-phone .hero-price{display:none}
@media (max-width:1299px){.hero-phone,.hero-price{display:none}}
@media (min-width:981px){
  .hero-blur{display:block;position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:blur(28px) brightness(.5) saturate(1.1);transform:scale(1.15);z-index:0}
  .hero-bg{left:auto;right:0;top:86px;width:60%;height:calc(100% - 86px);object-position:var(--pos-d);
    -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 24%),linear-gradient(180deg,transparent 0,#000 7%);-webkit-mask-composite:source-in;
    mask-image:linear-gradient(90deg,transparent 0,#000 24%),linear-gradient(180deg,transparent 0,#000 7%);mask-composite:intersect;transform-origin:50% 0}
  .hero-shade{background:radial-gradient(45% 55% at 0% 100%,rgba(98,186,245,.45) 0%,rgba(98,186,245,0) 70%),linear-gradient(90deg,rgba(12,32,48,.55) 0%,rgba(12,32,48,.25) 40%,rgba(12,32,48,0) 60%),linear-gradient(0deg,rgba(12,32,48,.45) 0%,rgba(12,32,48,0) 30%)}
}
@media (max-width:980px){
  .hero-phone,.hero-price{display:none}
}
@media (max-width:640px){
  .hero{min-height:100svh}
  .hero .chips-row,.hero .btn--clear{display:none}
  .hero h1{margin-bottom:16px}
  .hero-bg{object-position:var(--pos-m)}
  .hero-shade{background:radial-gradient(70% 40% at 0% 100%,rgba(98,186,245,.5) 0%,rgba(98,186,245,0) 70%),linear-gradient(0deg,rgba(12,32,48,.9) 0%,rgba(12,32,48,.6) 45%,rgba(12,32,48,.1) 75%,rgba(12,32,48,0) 100%)}
  .hero-in{padding:130px 20px 120px;text-align:center}
  .hero h1 .l1{font-size:clamp(44px,13vw,64px)}
  .hero h1 .l2{font-size:clamp(68px,22vw,110px)}
  .hero h1.t-strength .l2{font-size:clamp(52px,15vw,84px)}
  .hero .lead{margin:0 auto 20px;font-size:15px}
  .chips-row{justify-content:center}
  .hero .ctas{flex-direction:column}
  .hero .ctas .btn{width:100%}
  .hero .spark.s1{left:70%;top:30%}.hero .spark.s2{display:none}
}
@media (prefers-reduced-motion:reduce){.hero-bg,.spark,.hero-price{animation:none}.hero-bg{transform:none}.scribble path{animation:none;stroke-dashoffset:0}}

/* Phone */
.phone{background:#fff;border:3px solid var(--blue);border-radius:30px;padding:5px;box-shadow:0 18px 40px rgba(60,120,170,.18);overflow:hidden}
.phone .scr{position:relative;border-radius:24px;overflow:hidden;aspect-ratio:380/826;background:#f4f4f4}
.phone .scr img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .45s ease}
.bob{animation:bob 7s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(var(--r,0deg))}50%{transform:translateY(-12px) rotate(var(--r,0deg))}}

/* Tilted banner */
.strip{position:relative;z-index:4;margin-top:-26px;height:110px}
.strip::before{content:"";position:absolute;inset:30px -20px 20px;background:var(--yellow);transform:rotate(-1deg)}
.strip-band{position:absolute;left:-30px;right:-30px;top:20px;background:var(--blue);transform:rotate(-3deg);overflow:hidden;padding:14px 0;box-shadow:0 8px 20px rgba(0,0,0,.08)}
.strip-track{display:flex;gap:46px;width:max-content;animation:marquee 32s linear infinite;color:#fff;font-size:17px;text-transform:uppercase;white-space:nowrap;align-items:center}
.strip-track b{font-weight:700}
.strip-track .spark{color:#FFE08A;font-size:22px}
@keyframes marquee{to{transform:translateX(-50%)}}

/* For you */
.foryou{padding:110px 0 110px}
.foryou-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:60px;align-items:center}
.foryou p.sub{max-width:400px;font-size:14.5px;margin:22px 0 0;color:var(--body)}
.fy-tag{display:inline-block;margin-top:22px;background:var(--yellow);border-radius:999px;padding:10px 18px;font-weight:600;font-size:14px}
.ticks{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.ticks li{display:grid;grid-template-columns:34px 1fr;gap:14px;align-items:center;background:var(--cream);border-radius:18px;padding:16px 18px;font-weight:500;font-size:15px;line-height:1.45}
.ticks li::before{content:"✓";width:34px;height:34px;border-radius:50%;background:var(--blue);color:#fff;display:grid;place-items:center;font-size:14px;font-weight:700}

/* What you get */
.get{background:linear-gradient(180deg,var(--blue-soft) 0%,var(--blue-soft) 92%,#fff 100%);padding:40px 0 90px}
.feat-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px}
.feat{position:relative;background:#fff;border:1.5px solid var(--blue-line);border-radius:22px;padding:44px 24px 30px;overflow:hidden;min-height:190px}
.feat .num{position:absolute;top:-6px;right:12px;font-family:var(--head);font-weight:700;font-size:88px;line-height:1;color:#FFF0C2;z-index:0}
.feat h3{position:relative;z-index:1;font-family:var(--text);font-weight:700;font-size:16.5px;text-transform:uppercase;line-height:1.2;margin:0 0 10px;max-width:220px}
.feat p{position:relative;z-index:1;font-size:14px;color:var(--body);margin:0;line-height:1.5}
.feat--accent{background:var(--blue);border-color:var(--blue)}
.feat--accent h3,.feat--accent p{color:#fff}
.feat--accent .num{color:rgba(255,255,255,.2)}

/* App spotlight */
.app{padding:90px 0 40px}
.app-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:70px;align-items:center}
.app .app-intro{font-size:14.5px;max-width:420px;margin:18px 0 28px}
.feats{list-style:none;margin:0;padding:0;border-top:1px solid rgba(0,0,0,.1)}
.feats li{border-bottom:1px solid rgba(0,0,0,.1);position:relative}
.feats button{all:unset;box-sizing:border-box;width:100%;cursor:pointer;display:grid;grid-template-columns:44px 1fr 24px;align-items:center;padding:17px 0;font-family:var(--head);font-size:21px;font-weight:500;text-transform:uppercase;color:#6f7d8a;transition:color .2s}
.feats button:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
.feats .ic{font-size:21px;filter:grayscale(1);opacity:.5;transition:all .2s}
.feats .pl{font-family:var(--text);font-size:20px;font-weight:400;transition:transform .2s}
.feats p{margin:0;max-height:0;overflow:hidden;font-size:14px;color:var(--body);padding-left:44px;transition:max-height .35s ease,padding .35s ease}
.feats .pbar{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--blue)}
.feats li.on button{color:var(--ink)}
.feats li.on .ic{filter:none;opacity:1}
.feats li.on .pl{transform:rotate(45deg)}
.feats li.on p{max-height:110px;padding-bottom:17px}
.feats li.on .pbar{animation:progbar 4.5s linear forwards}
.feats.paused li.on .pbar{animation:none;width:100%}
@keyframes progbar{to{width:100%}}
.stage{position:relative;height:620px;display:flex;align-items:center;justify-content:center}
.stage::before{content:"";position:absolute;width:440px;height:440px;border-radius:50%;background:var(--yellow)}
.stage::after{content:"";position:absolute;width:530px;height:530px;border-radius:50%;border:2px dashed rgba(98,186,245,.55);animation:spin 60s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.stage .phone{position:relative;width:270px;z-index:2}
.chip{position:absolute;z-index:3;background:#fff;border-radius:14px;padding:10px 14px;font-size:12px;font-weight:600;box-shadow:0 12px 30px rgba(40,90,140,.15);display:flex;align-items:center;gap:8px;animation:bob 6s ease-in-out infinite}
.chip span{font-size:18px}
.chip.c1{top:110px;left:10px}.chip.c2{bottom:120px;right:0;animation-delay:-3s}

/* Phone row + pills */
.inapp{padding:60px 0 100px}
.inapp .head-row{align-items:center;text-align:center;flex-direction:column}
.phones{display:flex;justify-content:center;align-items:flex-start;gap:16px;margin:30px 0 48px}
.phones .phone{width:166px;flex:0 0 auto;margin-top:70px}
.phones .phone:nth-child(2),.phones .phone:nth-child(4){margin-top:30px}
.phones .phone:nth-child(3){margin-top:0}
.phones .phone:nth-child(1){animation-delay:-1s}.phones .phone:nth-child(2){animation-delay:-3s}.phones .phone:nth-child(3){animation-delay:-5s}.phones .phone:nth-child(4){animation-delay:-2s}.phones .phone:nth-child(5){animation-delay:-4s}
.pills{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;max-width:820px;margin:0 auto;padding:0;list-style:none}
.pills li{border:1.5px solid var(--blue-line);background:#fff;border-radius:999px;padding:8px 18px;font-size:13.5px;font-weight:500}
.pills li:nth-child(odd){background:#D6ECFD}
.pills i{font-style:normal;margin-right:6px}

/* Results */
.results{background:linear-gradient(180deg,var(--cream) 0%,var(--cream) 92%,#fff 100%);padding:40px 0 100px}
.story{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);border-radius:20px;overflow:hidden;background:var(--yellow);box-shadow:0 20px 50px rgba(150,110,20,.14)}
.story .ph{position:relative;background:#fff;min-height:470px}
.story .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}
.story .txt{padding:36px 34px 30px;display:flex;flex-direction:column}
.story .stars{color:#fff;font-size:14px;letter-spacing:2px}
.story h3{font-family:var(--head);font-weight:700;font-size:32px;text-transform:uppercase;margin:10px 0 18px;line-height:1.05}
.story .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:22px}
.story .stats div{background:#fff;border-radius:12px;padding:12px 12px 10px}
.story .stats b{display:block;font-family:var(--head);font-size:30px;font-weight:700;line-height:1}
.story .stats span{font-size:10.5px;line-height:1.3;display:block;margin-top:4px}
.story blockquote{margin:0 0 12px;font-size:16px;font-weight:500;line-height:1.45}
.story .extra{margin:0;font-size:13.5px;line-height:1.5}
.story cite{font-style:normal;font-size:10px;letter-spacing:1.4px;font-weight:700;text-transform:uppercase;margin-top:auto;padding-top:20px}
.lbl{position:absolute;top:12px;z-index:2;font-size:9px;letter-spacing:1px;font-weight:700;padding:3px 8px;border-radius:4px;text-transform:uppercase}
.lbl.b{left:12px;background:var(--yellow);color:var(--ink)}
.lbl.a{left:calc(50% + 10px);background:var(--blue);color:#fff}
.tf-head{display:flex;justify-content:space-between;align-items:flex-end;margin:46px 0 14px}
.tf-head h3{font-family:var(--head);font-weight:500;font-size:20px;text-transform:uppercase;margin:0}
.arrows{display:flex;gap:10px}
.arrow{width:44px;height:44px;border-radius:50%;border:1.5px solid var(--ink);background:#fff;font-size:22px;line-height:1;cursor:pointer;display:grid;place-items:center;padding-bottom:3px;color:var(--ink)}
.arrow:hover:not(:disabled){background:var(--yellow)}
.arrow:disabled{opacity:.3;cursor:default}
.tf-track{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:0 max(24px,calc((100vw - 1180px)/2 + 24px)) 6px;scroll-padding-left:max(24px,calc((100vw - 1180px)/2 + 24px));scrollbar-width:none}
.tf-track::-webkit-scrollbar{display:none}
.tf{position:relative;flex:0 0 330px;aspect-ratio:1/1;margin:0;border-radius:16px;overflow:hidden;background:#f3f3f3;scroll-snap-align:start}
.tf img{width:100%;height:100%;object-fit:cover}
.res-note{text-align:center;font-size:12px;color:var(--muted);margin:22px 0 0}
.res-cta{display:flex;justify-content:center;margin-top:26px}

/* Pricing */
.pricing{position:relative;background:linear-gradient(180deg,var(--cream) 0%,var(--cream) 88%,#fff 100%);padding:30px 0 80px;text-align:center}
.pricing .h2 strong{display:inline}
.pricing .lede{max-width:500px;margin:14px auto 46px;font-size:14px}
.plans{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:18px;text-align:left;max-width:860px;margin:0 auto}
.plan{position:relative;background:#fff;border:1.5px solid #F4E3A8;border-radius:16px;display:flex;flex-direction:column}
.plan .ph{height:200px;overflow:hidden;border-radius:15px 15px 0 0}
.plan .ph img{width:100%;height:100%;object-fit:cover}
.plan .bd{padding:20px 20px 26px;display:flex;flex-direction:column;flex:1}
.plan .term{font-size:10px;font-weight:600;letter-spacing:1.6px;color:var(--muted);text-transform:uppercase}
.plan .price{display:flex;align-items:baseline;gap:6px;margin:4px 0 8px;flex-wrap:wrap}
.plan .price b{font-family:var(--head);font-size:44px;font-weight:700;line-height:1}
.plan .price span{font-size:11.5px}
.plan .pp{align-self:flex-start;background:var(--yellow);border-radius:999px;font-size:10px;font-weight:700;letter-spacing:1px;padding:4px 10px;text-transform:uppercase;margin-bottom:16px}
.plan ul{list-style:none;padding:0;margin:0 0 20px;display:grid;gap:7px}
.plan li{display:flex;gap:9px;font-size:13.5px;line-height:1.4}
.plan li::before{content:"✓";flex:0 0 18px;height:18px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-size:10px;font-weight:700;margin-top:1px}
.plan .btn{width:100%;margin-top:auto;padding:14px}
.plan--pop{background:var(--yellow);border-color:var(--yellow)}
.plan--pop .term{color:var(--ink)}
.plan--pop .pp{background:transparent;border:1.5px solid var(--ink)}
.plan--pop .btn{background:var(--ink);color:#fff}
.plan .flag{position:absolute;top:-10px;left:18px;z-index:2;background:#fff;border-radius:999px;font-size:9px;font-weight:700;letter-spacing:1.3px;padding:4px 10px;text-transform:uppercase;box-shadow:0 2px 6px rgba(0,0,0,.08)}
.plan .annual{display:block;text-align:center;margin-top:10px;font-size:12px;font-weight:600;text-underline-offset:3px}
.trust{display:flex;justify-content:center;flex-wrap:wrap;gap:8px 24px;margin:28px 0 0;font-size:12px;list-style:none;padding:0}
.trust li{display:flex;align-items:center;gap:7px}
.trust li::before{content:"✓";display:inline-grid;place-items:center;width:15px;height:15px;border-radius:50%;background:var(--ink);color:#fff;font-size:9px;font-weight:700}

/* FAQ */
.faq{padding:70px 0 80px}
.faq-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px}
.faq-side p{font-size:13px;margin:14px 0 22px;max-width:280px}
.faq details{border-bottom:1px solid #e3e3e3}
.faq summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:30px 1fr 26px;align-items:center;padding:16px 0;font-weight:600;font-size:14.5px}
.faq summary::-webkit-details-marker{display:none}
.faq summary .n{font-size:9px;color:var(--muted);letter-spacing:1px}
.faq summary .t{display:grid;place-items:center;width:24px;height:24px;border-radius:50%;border:1px solid #999;font-size:15px;font-weight:400;line-height:1}
.faq details[open]{background:var(--blue-soft);border-radius:14px;border-bottom-color:transparent;padding:0 16px 18px;margin:0 -16px 6px}
.faq details[open] summary .t{background:var(--blue);border-color:var(--blue);color:#fff;transform:rotate(45deg)}
.faq details p{margin:0 0 0 30px;font-size:13.5px;color:var(--body);line-height:1.55}

/* Final */
.final{background:var(--blue);color:#fff;padding:20px 0 70px}
.final-grid{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:40px;align-items:center}
.final .eyebrow{color:#fff}
.final p{font-size:14px;max-width:440px;margin:12px 0 0}
.final .ctas{display:flex;flex-direction:column;gap:12px;min-width:300px}
.final .btn--outline{background:transparent;border-color:#fff;color:#fff}
.final .other{display:inline-block;margin-top:14px;font-size:13px;font-weight:600;color:#fff;text-underline-offset:3px}

/* Footer */
.footer{background:var(--yellow);padding:30px 0 calc(24px + env(safe-area-inset-bottom,0px))}
.foot-grid{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding-bottom:24px;border-bottom:1px solid rgba(0,0,0,.12)}
.foot-grid img{height:26px;width:auto}
.foot-grid nav{display:flex;gap:22px;flex-wrap:wrap}
.foot-grid nav a{text-decoration:none;font-size:13px;font-weight:600}
.legal{padding-top:14px;font-size:11px}

/* Mobile buy bar */
.buybar{display:none}

/* Reveal */
.rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}
.rv.in{opacity:1;transform:none}

@media (max-width:1024px){
  .nav ul{gap:18px}
  .phones .phone{width:140px}
}
@media (max-width:860px){
  .top{padding:10px 12px 0}
  .nav{border-radius:18px;padding:10px 10px 10px 18px}
  .nav ul{display:none}
  .nav .btn{padding:11px 18px;font-size:11.5px}
  .strip{margin-top:-40px}
  .strip-track{font-size:14px}
  .head-row{flex-direction:column;align-items:flex-start;gap:14px;margin-bottom:30px}
  .intro{max-width:none}
  .foryou{padding:40px 0 70px}
  .foryou-grid{grid-template-columns:minmax(0,1fr);gap:28px}
  .feat-grid{grid-template-columns:minmax(0,1fr);gap:14px}
  .feat{min-height:0}
  .app{padding:60px 0 20px}
  .app-grid{grid-template-columns:minmax(0,1fr);gap:16px}
  .stage{order:-1;height:430px}
  .stage::before{width:300px;height:300px}
  .stage::after{width:360px;height:360px}
  .stage .phone{width:190px}
  .chip.c1{left:0;top:50px}.chip.c2{right:0;bottom:50px}
  .feats button{font-size:18px;grid-template-columns:36px 1fr 24px}
  .feats p{padding-left:36px}
  .inapp{padding:40px 0 70px}
  .phones{justify-content:flex-start;overflow-x:auto;scroll-snap-type:x mandatory;padding:10px 24px 20px;margin:0 -24px 28px;scrollbar-width:none}
  .phones::-webkit-scrollbar{display:none}
  .phones .phone{width:190px!important;margin-top:0!important;scroll-snap-align:center;animation:none}
  .pills{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 14px;max-width:none}
  .pills li,.pills li:nth-child(odd){display:flex;align-items:center;gap:10px;background:none;border:0;border-bottom:1px solid #E3EDF6;border-radius:0;padding:10px 0;font-size:12.5px;line-height:1.25}
  .pills i{flex:0 0 30px;height:30px;margin:0;border-radius:9px;background:var(--blue-soft);display:grid;place-items:center;font-size:14px}
  .results{padding:30px 0 70px}
  .story{grid-template-columns:minmax(0,1fr)}
  .story .ph{min-height:0;aspect-ratio:761/738}
  .story .txt{padding:22px 20px}
  .story h3{font-size:26px}
  .story .stats b{font-size:clamp(20px,6.4vw,26px)}
  .tf-head .arrows{display:none}
  .tf{flex-basis:80%}
  .plans{grid-template-columns:minmax(0,1fr);max-width:440px}
  .plan--pop{order:-1}
  .trust{flex-direction:column;align-items:flex-start;max-width:440px;margin:24px auto 0}
  .faq-grid{grid-template-columns:minmax(0,1fr);gap:20px}
  .faq-side{text-align:center}
  .faq-side p{margin:12px auto 20px}
  .final-grid{grid-template-columns:minmax(0,1fr);gap:24px}
  .final .ctas{min-width:0}
  .foot-grid{flex-direction:column;align-items:flex-start}
}
@media (max-width:640px){
  body{padding-bottom:calc(84px + env(safe-area-inset-bottom,0px))}
  .wrap{padding:0 20px}
  .buybar{display:flex;position:fixed;left:10px;right:10px;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:60;align-items:center;justify-content:space-between;gap:12px;background:var(--ink);color:#fff;border-radius:20px;padding:10px 10px 10px 18px;box-shadow:0 14px 34px rgba(0,0,0,.3);transform:translateY(140%);transition:transform .25s ease}
  .buybar.show{transform:none}
  .buybar b{display:block;font-family:var(--head);font-size:17px;text-transform:uppercase;line-height:1.1}
  .buybar span{font-size:11.5px;color:rgba(255,255,255,.75)}
  .buybar .btn{padding:12px 18px;font-size:11.5px;background:var(--yellow);color:var(--ink)}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .bob,.chip,.stage::after,.strip-track{animation:none}
  .feats li.on .pbar{animation:none;width:100%}
  .rv{opacity:1;transform:none;transition:none}
  .btn,.buybar,.phone .scr img{transition:none}
  .btn:hover{transform:none}
}
'''


def esc(s):
    return html.escape(s, quote=False)


WAVE_BLUE_SOFT = '<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 C 300 0, 700 -10, 1000 30 S 1440 40, 1440 30 L1440 70 Z" fill="#EAF4FE"/></svg>'
WAVE_CREAM = '<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 70 C 400 -10, 1040 -10, 1440 70 Z" fill="#FFF7DD"/></svg>'
WAVE_BLUE = '<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true"><path d="M0 40 C 300 -5, 700 0, 1050 45 S 1440 20, 1440 20 L1440 70 L0 70 Z" fill="#62BAF5"/></svg>'
WAVE_YELLOW = '<svg class="wave" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true" style="background:#62BAF5"><path d="M0 40 C 400 0, 900 10, 1440 30 L1440 70 L0 70 Z" fill="#FDE08D"/></svg>'


def page(slug, p):
    e = esc
    p = dict(p)
    p.setdefault('price', '59'); p.setdefault('short', p['name']); p.setdefault('new', False)
    p.setdefault('intro', 'Eight weeks of training written by Gabby, laid out session by session in the Shape Up app.')
    p.setdefault('trust', '8 week structured programme'); p.setdefault('final_h', ('Your 8 weeks', 'start now'))
    price, short, new = p['price'], p['short'], p['new']
    h1a, h1b = p['h1']
    facts = ''.join(f'<li><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in p['facts'])
    chips = ''.join(f'<li><b>{e(a)}</b>{e(b)}</li>' for a, b in p['facts'])
    tick = ''.join(f'<span>{e(x)}</span><span class="spark">✦</span>' for x in p['ticker'])
    fy = ''.join(f'<li>{e(x)}</li>' for x in p['for_you'])
    feats_prog = ''.join(
        f'<article class="feat{" feat--accent" if i == 5 else ""}"><span class="num" aria-hidden="true">{i + 1:02d}</span><h3>{e(h)}</h3><p>{e(t)}</p></article>'
        for i, (h, t) in enumerate(p['inside']))
    feat_items = ''.join(
        f'<li class="{"on" if i == 0 else ""}" data-img="{img}"><button aria-expanded="{"true" if i == 0 else "false"}"><span class="ic" aria-hidden="true">{ic}</span>{e(h)}<span class="pl" aria-hidden="true">+</span></button><p>{e(d)}</p><span class="pbar" aria-hidden="true"></span></li>'
        for i, (ic, h, d, img) in enumerate(APP_FEATS))
    strip_imgs = ['images/app-meals.webp', 'images/app-today.webp', 'images/app-home.webp', 'images/app-log.webp', 'images/app-habits.webp']
    phones = ''.join(f'<div class="phone bob"><div class="scr"><img src="{s}" alt="" loading="lazy"></div></div>' for s in strip_imgs)
    pills = ''.join(f'<li><i aria-hidden="true">{ic}</i>{e(n)}</li>' for ic, n in APP_PILLS)
    tfs = ''.join(f'<figure class="tf"><img src="{s}" alt="Shape Up member before and after" loading="lazy"><span class="lbl b">Before</span><span class="lbl a">After</span></figure>' for s in TRANSFORMATIONS)
    pticks = ''.join(f'<li>{e(x)}</li>' for x in p['programme_ticks'])
    other_slug, other_name = p['other']
    faqs = [
        ('Is it suitable for beginners?', 'Yes. It is built for all abilities, so whether you are brand new to lifting or you have been training for years, you can follow it and progress at your own pace.'),
        p['faq_gym'],
        ('How do I access it?', 'Everything lives in the Shape Up app. Once you have checked out, log in to the app and your programme will be there, ready for your first session.'),
        ('Should I get the programme or the membership?', f"If you just want {p['name']}, the programme on its own is £{price}. If you would like both new programmes plus every other Shape Up programme, meal plans and the community, the annual membership is £199 a year, with 7 days free."
         if new else f"If you just want {p['name']}, the programme on its own is £{price}. If you would like every Shape Up programme, including the new Island Body V2 and Strength Is Power, plus meal plans and the community, the annual membership is £199 a year, with 7 days free."),
        ('Can I do both new programmes?', 'Absolutely. Island Body V2 and Strength Is Power are both included in the membership, so you can finish one and go straight into the other.')
        if new else ('Can I do more than one programme?', 'Yes. Every Shape Up programme is included in the membership, so you can finish one and go straight into the next.'),
    ]
    if 'faq_extra' in p: faqs.insert(2, p['faq_extra'])
    lede = (f"Get {e(p['name'])} on its own, or get it with both new programmes and everything else in the Shape Up membership." if new
            else f"Get {e(p['name'])} on its own, or get it with every other Shape Up programme in the membership.")
    mem_li = f"{e(p['name'])} and {e(other_name)}" if new else f"{e(p['name'])}, plus Island Body V2 and Strength Is Power"
    final_p = (f"Get {e(p['name'])} for £{price}, or get both new programmes and everything else with the Shape Up membership." if new
               else f"Get {e(p['name'])} for £{price}, or get every Shape Up programme with the Shape Up membership.")
    other_link = f'<a class="other" href="/{other_slug}">Also new: {e(other_name)} →</a>' if new else '<a class="other" href="/one-off-programmes">See all programmes →</a>'
    foot_links = (f'<a href="/one-off-programmes">All programmes</a><a href="/{other_slug}">{e(other_name)}</a>' if new
                  else '<a href="/one-off-programmes">All programmes</a><a href="/island-body-v2">Island Body V2</a><a href="/strength-is-power">Strength Is Power</a>')
    faq_html = ''.join(
        f'<details{" open" if i == 0 else ""}><summary><span class="n">{i + 1:02d}</span>{e(q)}<span class="t" aria-hidden="true">+</span></summary><p>{e(a)}</p></details>'
        for i, (q, a) in enumerate(faqs))

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
<body>

<header class="top">
  <nav class="nav" aria-label="Main">
    <a class="logo" href="/"><img src="images/img-01.webp" alt="Shape Up"></a>
    <ul>
      <li><a href="#for-you">Who It's For</a></li>
      <li><a href="#what-you-get">What You Get</a></li>
      <li><a href="#results">Results</a></li>
      <li><a href="#pricing">Pricing</a></li>
      <li><a href="#faq">FAQ</a></li>
    </ul>
    <a class="btn btn--yellow" href="{p['checkout']}">Get it · £{price}</a>
  </nav>
</header>

<main>
<!-- HERO -->
<section class="hero{" no-phone" if p.get("no_phone") else ""}" style="--pos:{p['img_pos']};--pos-m:{p['img_pos_m']};--pos-d:{POS_D[p['img']]}">
  <img class="hero-blur" src="{p['img']}" alt="" aria-hidden="true">
  <img class="hero-bg" src="{p['img']}" alt="{html.escape(p['img_alt'])}">
  <div class="hero-shade" aria-hidden="true"></div>
  <span class="spark s1" aria-hidden="true">✦</span><span class="spark s2" aria-hidden="true">✦</span><span class="spark s3" aria-hidden="true">✦</span>
  <div class="hero-in">
    <div class="rating"><span class="avs"><img src="images/img-02.webp" alt=""><img src="images/img-03.webp" alt=""><img src="images/img-04.webp" alt=""><img src="images/img-05.webp" alt=""></span><span class="st" aria-hidden="true">★★★★★</span><span>48,000+ Reviews</span></div>
    <h1 class="t-{p['theme']}"><span class="l1">{e(p['hero_h'][0])}</span><span class="l2">{e(p['hero_h'][1])}<svg class="scribble" viewBox="0 0 300 28" preserveAspectRatio="none" aria-hidden="true"><path d="M4 18 C 60 6, 120 26, 180 14 S 270 8, 296 16"/></svg></span></h1>
    <p class="lead">{e(p['sub'])}</p>
    <ul class="chips-row">{chips}</ul>
    <div class="ctas">
      <a class="btn btn--hero" id="heroBuy" href="{p['checkout']}">Get {e(short)} <span aria-hidden="true">→</span></a>
      <a class="btn btn--clear" href="#what-you-get">Explore the app</a>
    </div>
    <p class="price">£{price} one-time payment · or included in the membership</p>
  </div>
  <div class="phone hero-phone bob" aria-hidden="true"><div class="scr"><img src="images/app-workout.webp" alt=""></div></div>
  <div class="hero-price" aria-hidden="true"><b>£{price}</b>one time</div>
</section>
<div class="strip strip--hero" aria-hidden="true">
  <div class="strip-band"><div class="strip-track">{tick}{tick}</div></div>
</div>

<!-- THIS IS FOR YOU IF -->
<section class="foryou" id="for-you">
  <div class="wrap foryou-grid">
    <div class="rv">
      <p class="eyebrow">Who it's for</p>
      <h2 class="h2">This is for you<strong>if...</strong></h2>
      <p class="sub">If any of these sound like you, {e(p['name'])} was made for you.</p>
      <span class="fy-tag">{e(p['for_you_tag'])}</span>
    </div>
    <ul class="ticks rv">{fy}</ul>
  </div>
</section>

<!-- WHAT YOU GET -->
{WAVE_BLUE_SOFT}
<section class="get" id="what-you-get">
  <div class="wrap">
    <div class="head-row rv">
      <div>
        <p class="eyebrow">What you get</p>
        <h2 class="h2">Everything in<strong>{e(p['name'])}</strong></h2>
      </div>
      <p class="intro">{e(p['intro'])}</p>
    </div>
    <div class="feat-grid rv">{feats_prog}</div>
  </div>

  <div class="app">
    <div class="wrap app-grid">
      <div class="rv">
        <p class="eyebrow">Inside the Shape Up app</p>
        <h2 class="h2">Your programme,<strong>in your pocket</strong></h2>
        <p class="app-intro">{e(p['name'])} lives in the Shape Up app, so every session, every set and every bit of progress is right there on your phone.</p>
        <ul class="feats" id="feats">{feat_items}</ul>
      </div>
      <div class="stage" aria-hidden="true">
        <div class="chip c1"><span>📈</span>Log every set</div>
        <div class="phone bob"><div class="scr"><img id="appScr" src="{APP_FEATS[0][3]}" alt=""></div></div>
        <div class="chip c2"><span>🎥</span>Video demos</div>
      </div>
    </div>
  </div>
</section>

<section class="inapp">
  <div class="wrap">
    <div class="head-row rv">
      <div>
        <p class="eyebrow">Inside the app</p>
        <h2 class="h2">Everything you need,<strong>right there in your pocket.</strong></h2>
      </div>
    </div>
    <div class="phones" aria-hidden="true">{phones}</div>
    <ul class="pills rv">{pills}</ul>
  </div>
</section>

<!-- RESULTS -->
{WAVE_CREAM}
<section class="results" id="results">
  <div class="wrap">
    <div class="head-row rv">
      <div>
        <p class="eyebrow">Results</p>
        <h2 class="h2">Real women,<strong>real results</strong></h2>
      </div>
      <p class="intro">Every one of these women trained with Shape Up. Different starting points, different goals, same app and the same community behind them.</p>
    </div>

    <article class="story rv">
      <div class="ph"><img src="images/tf-beth.webp" alt="Beth's before and after, side view, four weeks apart" loading="lazy"><span class="lbl b">Before</span><span class="lbl a">After</span></div>
      <div class="txt">
        <span class="stars" aria-label="5 stars">★★★★★</span>
        <h3>Beth, 4 weeks in</h3>
        <div class="stats">
          <div><b>1.5kg</b><span>down</span></div>
          <div><b>4.5cm</b><span>off her waist</span></div>
          <div><b>4</b><span>weeks of hard work</span></div>
        </div>
        <blockquote>“My mindset again is feeling good and positive about the gym and I've really enjoyed the set of exercises as I feel they've allowed me to push myself.”</blockquote>
        <p class="extra">“This group really have made things much easier to stick to and push through all the challenges that crop up!”</p>
        <cite>Beth · Shape Up member</cite>
      </div>
    </article>

    <div class="tf-head">
      <h3>More member transformations</h3>
      <div class="arrows">
        <button class="arrow" data-dir="-1" aria-label="Previous transformations">‹</button>
        <button class="arrow" data-dir="1" aria-label="Next transformations">›</button>
      </div>
    </div>
  </div>
  <div class="tf-track" id="tfTrack" tabindex="0" aria-label="Member before and after photos">{tfs}</div>
  <div class="wrap">
    <p class="res-note">Results from Shape Up members across Gabby's programmes. Everyone's results are different.</p>
    <div class="res-cta"><a class="btn" href="#pricing">Start your transformation</a></div>
  </div>
</section>

<!-- CHECKOUT -->
<section class="pricing" id="pricing">
  <div class="wrap">
    <p class="eyebrow">Get started</p>
    <h2 class="h2">If you're waiting<br>for a sign, <strong>this is it</strong></h2>
    <p class="lede">{lede}</p>
    <div class="plans rv">
      <article class="plan">
        <div class="ph"><img src="{p['img']}" alt="" style="object-position:{p['img_pos']}" loading="lazy"></div>
        <div class="bd">
          <span class="term">{e(p['name'])}</span>
          <div class="price"><b>£{price}</b><span>one time</span></div>
          <span class="pp">The programme on its own</span>
          <ul>{pticks}</ul>
          <a class="btn btn--outline" href="{p['checkout']}">Get {e(short)}</a>
        </div>
      </article>
      <article class="plan plan--pop">
        <span class="flag">Best value</span>
        <div class="ph"><img src="images/img-19.webp" alt="" style="object-position:center 20%" loading="lazy"></div>
        <div class="bd">
          <span class="term">Shape Up Membership</span>
          <div class="price"><b>£199</b><span>a year</span></div>
          <span class="pp">Annual membership · 7 days free</span>
          <ul>
            <li>{mem_li}</li>
            <li>Every other Shape Up programme</li>
            <li>New content added every month</li>
            <li>Meal plans and barcode food scanner</li>
            <li>Cycle and habit tracking, plus the community</li>
          </ul>
          <a class="btn" href="{MEM_YEARLY}">Start free trial</a>
        </div>
      </article>
    </div>
    <ul class="trust"><li>{e(p['trust'])}</li><li>All abilities catered for</li><li>iOS &amp; Android</li></ul>
  </div>
</section>

<!-- FAQ -->
<section class="faq" id="faq">
  <div class="wrap faq-grid">
    <div class="faq-side">
      <p class="eyebrow">FAQ</p>
      <h2 class="h2">Everything<strong>you'd ask</strong></h2>
      <p>Still unsure? Send Gabby's team a message on Instagram and they'll help you pick.</p>
      <a class="btn btn--yellow" href="{p['checkout']}">Get {e(short)}</a>
    </div>
    <div>{faq_html}</div>
  </div>
</section>

<!-- FINAL -->
{WAVE_BLUE}
<section class="final">
  <div class="wrap final-grid">
    <div>
      <p class="eyebrow">Ready when you are</p>
      <h2 class="h2">{e(p['final_h'][0])}<strong>{e(p['final_h'][1])}</strong></h2>
      <p>{final_p}</p>
      {other_link}
    </div>
    <div class="ctas">
      <a class="btn btn--yellow" id="finalBuy" href="{p['checkout']}">Get {e(short)} · £{price}</a>
      <a class="btn btn--outline" href="#pricing">See membership</a>
    </div>
  </div>
</section>
</main>

{WAVE_YELLOW}
<footer class="footer">
  <div class="wrap">
    <div class="foot-grid">
      <a href="/"><img src="images/img-01.webp" alt="Shape Up"></a>
      <nav>{foot_links}<a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></nav>
    </div>
    <div class="legal">© 2026 Shape Up with Gabby. All rights reserved.</div>
  </div>
</footer>

<div class="buybar" id="buyBar" aria-hidden="true">
  <div><b>{e(short)}</b><span>£{price} one time</span></div>
  <a class="btn" href="{p['checkout']}" tabindex="-1">Get it</a>
</div>

<script>
(function(){{
  var io=('IntersectionObserver' in window);
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // App spotlight: auto-advances, tap to choose
  var list=document.getElementById('feats'),scr=document.getElementById('appScr');
  if(list&&scr){{
    var items=[].slice.call(list.children),cur=0,timer=null,DUR=4500;
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

  // Transformations carousel arrows
  var tr=document.getElementById('tfTrack'),arr=document.querySelectorAll('.arrow');
  if(tr&&arr.length){{
    function upd(){{arr[0].disabled=tr.scrollLeft<5;arr[1].disabled=tr.scrollLeft+tr.clientWidth>=tr.scrollWidth-5;}}
    arr.forEach(function(a){{a.addEventListener('click',function(){{var c=tr.querySelector('.tf');tr.scrollBy({{left:(c.offsetWidth+14)*a.dataset.dir}});}});}});
    tr.addEventListener('scroll',upd);window.addEventListener('resize',upd);upd();
  }}

  // Reveal on scroll
  var rv=[].slice.call(document.querySelectorAll('.rv'));
  if(io){{
    var ob=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');ob.unobserve(x.target);}}}});}},{{threshold:.12}});
    rv.forEach(function(el){{ob.observe(el);}});
  }} else rv.forEach(function(el){{el.classList.add('in');}});

  // Mobile buy bar between the hero and final buttons
  var bar=document.getElementById('buyBar'),hb=document.getElementById('heroBuy'),fb=document.getElementById('finalBuy');
  if(io&&bar){{
    var hv=true,fv=false;
    function show(){{var on=!hv&&!fv;bar.classList.toggle('show',on);bar.setAttribute('aria-hidden',on?'false':'true');bar.querySelector('a').tabIndex=on?0:-1;}}
    new IntersectionObserver(function(e){{hv=e[0].isIntersecting;show();}}).observe(hb);
    new IntersectionObserver(function(e){{fv=e[0].isIntersecting;show();}}).observe(fb);
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
