# Shape Up Waitlist

Pre-registration page for upcoming Shape Up with Gabby programmes.

- `index.html` was the waitlist page. Since launch it says the new programmes are live, with one button to /programmes. (The sign-up form and its Google Sheet/CRM script were removed from the page; `scripts/waitlist-sheet.gs` is kept for reference.)
- `images/` holds the logo and Gabby's photo.
- `scripts/waitlist-sheet.gs` is the Google Apps Script that saves sign-ups to the "Gabby Waitlist Sign Ups" Google Sheet. Its web app URL is set in `SHEET_URL` in `index.html`.

- `thank-you.html` is the page people land on after signing up. It greets them by first name.
- `links.html` is Gabby's link-in-bio page (shapeupapp.co.uk/links).
- `images/avatar.webp` is the round photo on the links page.
- `programmes.html` is the new programmes page (shapeupapp.co.uk/programmes): Island Body V2 and Strength Is Power at £59 each, plus a full-width membership option (£24.99 a month or £199 a year).
- Every page has the Google Analytics tag (G-KNYFB4VHQ3) in its head.
- `island-body-v2.html` and `strength-is-power.html` are the sales pages for the two new programmes (shapeupapp.co.uk/island-body-v2 and /strength-is-power). Both are generated from `scripts/build_sales.py`: edit the copy there and rerun `python3 scripts/build_sales.py .` from the repo root.
