# Shape Up Waitlist

Pre-registration page for upcoming Shape Up with Gabby programmes.

- `index.html` is the homepage (shapeupapp.co.uk). It is a copy of the main site homepage from repshealth/shapeupwithgabby, so update both if the homepage changes. (It used to be the waitlist page; the old sign-up script is kept for reference in `scripts/waitlist-sheet.gs`.)
- `one-off-programmes.html` is the full one-off programmes page (shapeupapp.co.uk/one-off-programmes), copied from the main site. The homepage's one-off programmes button links here.
- `images/` holds the logo and Gabby's photo.
- `scripts/waitlist-sheet.gs` is the Google Apps Script that saves sign-ups to the "Gabby Waitlist Sign Ups" Google Sheet. Its web app URL is set in `SHEET_URL` in `index.html`.

- `thank-you.html` is the page people land on after signing up. It greets them by first name.
- `links.html` is Gabby's link-in-bio page (shapeupapp.co.uk/links).
- `images/avatar.webp` is the round photo on the links page.
- `programmes.html` is the new programmes page (shapeupapp.co.uk/programmes): Island Body V2 and Strength Is Power at £59 each, plus a full-width membership option (£24.99 a month or £199 a year).
- Every page has the Google Analytics tag (G-KNYFB4VHQ3) in its head.
- `island-body-v2.html` and `strength-is-power.html` are the sales pages for the two new programmes (shapeupapp.co.uk/island-body-v2 and /strength-is-power). Both are generated from `scripts/build_sales.py`: edit the copy there and rerun `python3 scripts/build_sales.py .` from the repo root.
- `black-friday.html` is the Black Friday VIP waitlist (shapeupapp.co.uk/black-friday). Sign-ups go to the same Google Sheet and to Gabby's leads in the REPS dashboard, tagged "Black Friday VIP waitlist", then land on `black-friday-thank-you.html`.
