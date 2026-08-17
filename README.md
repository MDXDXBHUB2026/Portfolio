# Manoj Rajan — Portfolio Site

Single-page portfolio for GitHub Pages. No build step, no npm, no dependencies to install —
Tailwind CSS, FontAwesome and Inter load from CDNs, and the JavaScript is plain vanilla.
Commit the files and the site is live.

```
index.html                 ← the entire site
assets/
  profile.jpg              ← headshot, cropped 3:4 from profile-source.jpg
  profile-source.jpg       ← untouched original, kept for re-cropping
  og-image.png             ← LinkedIn preview card (generated)
  Manoj-Rajan-CV.pdf       ← generated CV, powers the "Download CV" button
  projects/*.svg           ← prototype snapshots, copied from the AI portfolio
tools/
  make-og-image.py         ← regenerates og-image.png
  make-cv-pdf.py           ← regenerates the downloadable CV
.nojekyll                  ← tells GitHub Pages to serve files as-is
```

---

## Step 0 — Three edits before you publish

### 1. Add your photo  ← required, still outstanding

Save one file as:

```
assets/profile.jpg
```

It is used in two places, so crop it to **head and shoulders in portrait orientation**
with your face in the upper third — around 900×1200px:

- **Intro hero** (large, right-hand side) — filled to a tall box, anchored 15% from the
  top, desaturated and faded into the charcoal band, warming to full colour on hover.
- **Sidebar avatar** (112px circle) — anchored to the top of the image.

A full-length shot works poorly in both: the face ends up tiny in the circle. Until the
file exists, both spots show an "MR" placeholder — never a broken image.

To turn off the desaturation, delete the `filter:` line from `.intro-photo` in the
`<style>` block.

### 2. Live URL — already set ✅

The site is wired to **<https://mdxdxbhub2026.github.io/Portfolio/>** in the four tags near
the top of `index.html` (`canonical`, `og:url`, `og:image`, `twitter:image`). These must stay
**absolute URLs** — LinkedIn will not follow a relative path when it builds the preview card.

If you ever rename the repo, update all four.

### 3. Optional extras

- **GitHub icon** — the sidebar GitHub link is commented out. Uncomment it and add your
  handle, or leave it hidden.
- **Download CV** — the button serves `assets/Manoj-Rajan-CV.pdf`, generated from
  `tools/make-cv-pdf.py`. Edit the CONTENT block in that script and re-run to update it,
  or just drop your own PDF in at the same path.
- **Certification years** — the credential cards show the issuing body but no dates.
  Add the year you earned each one in the `#certifications` section.

---

## Steps 1 & 2 — Repository and upload ✅ done

The code lives at <https://github.com/MDXDXBHUB2026/Portfolio> on the `main` branch.

To push later changes:

```bash
git add -A && git commit -m "Update portfolio" && git push
```

## Step 3 — Enable GitHub Pages

1. In the repo, open **Settings** (top bar) → **Pages** (left sidebar).
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Set **Branch** to `main` and folder to `/ (root)`, then **Save**.
4. Wait 1–2 minutes. Refresh the page and GitHub shows: *Your site is live at …*
5. Open that URL and confirm the photo, links and navigation all work.

> First deploys can take a few minutes. If you get a 404, check that the file is named
> exactly `index.html` (lowercase) and sits at the repo root, not inside a subfolder.

## Step 4 — Make the LinkedIn preview card work

The preview card is already wired up. What makes it appear:

| Tag | Purpose |
|---|---|
| `og:title` | Bold headline on the card |
| `og:description` | Grey text under the headline |
| `og:image` | The 1200×630 image — **must be an absolute URL** |
| `og:url` | Canonical link |
| `og:type`, `og:site_name` | Context for the unfurler |

1. Confirm the image loads on its own: open
   <https://mdxdxbhub2026.github.io/Portfolio/assets/og-image.png> directly in a browser.
   If that 404s, LinkedIn will show a bare text link.
2. Go to the **LinkedIn Post Inspector**: <https://www.linkedin.com/post-inspector/>
3. Paste `https://mdxdxbhub2026.github.io/Portfolio/` and click **Inspect**. You'll see
   exactly what the card will look like.
4. **This step matters:** LinkedIn caches preview data for about 7 days. If you share the
   link first and fix the tags afterwards, the old (or empty) card sticks around. Running
   the Inspector forces a re-scrape and clears the cache — so always inspect *after* any
   change to the OG tags or image.

### Regenerating the preview image

`assets/og-image.png` currently shows a typographic card with no photo. Once
`assets/profile.jpg` exists, regenerate it to composite in a circular headshot:

```bash
python tools/make-og-image.py
```

Requires Pillow (`pip install pillow`). Text, colours and metrics are constants at the top
of the script. Re-run after any edit, then re-inspect on LinkedIn to bust the cache.

If you'd rather not run the script, any 1200×630 PNG or JPG dropped in as
`assets/og-image.png` works — keep it under ~5MB and avoid small text, since LinkedIn
renders the card at roughly half size in the feed.

---

## Connecting the contact form  ← action needed

The form in `#contact` is built and validated, but **not yet connected**. GitHub Pages
serves static files and cannot send email, so submissions need a third-party form backend.
Until you connect one, the form falls back to opening the visitor's mail client with
everything they typed already filled in — so it still works, it just isn't seamless.

You have to create the account yourself; then paste one value into `index.html`.

### Option A — Web3Forms (no account, fastest)

1. Go to <https://web3forms.com>, enter `echoflare06@gmail.com`, and click to get an
   access key. Check your inbox and confirm.
2. In `index.html`, find `var FORM_ENDPOINT` near the bottom and set **both**:

   ```js
   var FORM_ENDPOINT = 'https://api.web3forms.com/submit';
   var FORM_ACCESS_KEY = 'paste-your-access-key-here';
   ```

Free tier: 250 submissions/month.

### Option B — Formspree

1. Sign up at <https://formspree.io>, create a new form, and copy its endpoint — it looks
   like `https://formspree.io/f/abcdwxyz`.
2. In `index.html`, set just the endpoint and leave the access key empty:

   ```js
   var FORM_ENDPOINT = 'https://formspree.io/f/abcdwxyz';
   var FORM_ACCESS_KEY = '';
   ```

Free tier: 50 submissions/month. The first submission needs email confirmation.

### Then

Commit, push, and send yourself a test message from the live site to confirm it arrives.

Both services see the contents of every message and the sender's email address — that is
inherent to any form on a static host. If you would rather not involve a third party at
all, delete the `<form id="contact-form">` block; the email, phone, WhatsApp and LinkedIn
cards beside it already give people four ways to reach you.

The form includes a hidden honeypot field that silently discards bot submissions.

## Regenerating the CV

The downloadable CV is built from a script so it stays in step with the site:

```bash
python tools/make-cv-pdf.py
```

Requires reportlab (`pip install reportlab`). All wording lives in the constants at the top
of the script — summary, highlights, roles, education, certifications, expertise. Layout,
spacing and page breaks are handled for you. Two pages, A4.

Certification years are not in the CV yet; add them there and in `#certifications` together.

## Updating the project snapshots

The six cards in `#projects` use SVGs copied into `assets/projects/` from the standalone
AI portfolio, so this site stays self-contained and does not hotlink another page. If you
change a prototype's screenshots over there, refresh the copy here:

```bash
curl -sL -o assets/projects/maritime.svg https://mdxdxbhub2026.github.io/digital-ai-portfolio/images/maritime.svg
```

Cards sit in a 16:9 frame with `object-contain`, so a tall mobile mockup (GreenRoute) is
letterboxed rather than cropped. Snapshot counts in the card links are written by hand —
update them if a prototype gains screens.

## Editing the content later

Everything lives in `index.html`, in plain readable sections marked with comment banners
(`INTRO HERO`, `ABOUT`, `EXPERIENCE`, `PROJECTS`, `SKILLS`, `EDUCATION`, `CERTIFICATIONS`,
`CONTACT`). To add a skill badge,
copy an existing `<li>` in that category and change the text. To add a role, copy a whole
`<li class="reveal relative">` block in the experience timeline.

Commit the change and GitHub Pages redeploys within a minute or so.

## A note on deploying

Avoid pushing twice within about a minute. GitHub Pages cancels the in-flight run and the
next deploy can fail to acquire the `github-pages` environment — the build succeeds but
nothing ships, and the site silently serves the previous commit. If the live site looks
stale, check the run list at
<https://github.com/MDXDXBHUB2026/Portfolio/actions> before assuming a caching problem.
An empty commit (`git commit --allow-empty -m "Retrigger"`) re-runs the deployment.

## Local preview

```bash
python -m http.server 8899
```

Then open <http://localhost:8899>. Use a server rather than double-clicking the file —
opening via `file://` breaks the relative image paths.

## What's built in

- Full-bleed intro hero with a large portrait, desaturated and masked so it dissolves
  into the charcoal band (treatment modelled on goranradmanovic.github.io)
- Projects section carrying six AI prototype cards with snapshots, each linking through
  to the full write-up at mdxdxbhub2026.github.io/digital-ai-portfolio
- Sticky full-height sidebar on desktop, collapsing to a hamburger bar under 1024px
- Smooth scrolling with active-link highlighting driven by scroll position
- Dark/light toggle, remembered in `localStorage`, defaulting to your system setting
- Accessibility: skip link, ARIA labels, `aria-current` on the active nav item, visible
  focus rings, `Esc` to close the mobile menu, and full `prefers-reduced-motion` support
- Contact section closing the page: a validated message form, plus email, phone,
  WhatsApp and LinkedIn cards and a CV download
- `Person` JSON-LD structured data for search engines
- Print stylesheet — "Save as PDF" from the browser produces a clean document
