# Manoj Rajan — Portfolio Site

Single-page portfolio for GitHub Pages. No build step, no npm, no dependencies to install —
Tailwind CSS, FontAwesome and Inter load from CDNs, and the JavaScript is plain vanilla.
Commit the files and the site is live.

```
index.html                 ← the entire site
assets/
  profile.jpg              ← YOUR HEADSHOT (you need to add this)
  og-image.png             ← LinkedIn preview card (generated)
  Manoj-Rajan-CV.pdf       ← optional, powers the "Download CV" button
tools/
  make-og-image.py         ← optional, regenerates og-image.png
.nojekyll                  ← tells GitHub Pages to serve files as-is
```

---

## Step 0 — Three edits before you publish

### 1. Add your headshot  ← required

Crop the photo to a **square around head and shoulders** (not the full seated shot —
in a 112px circle a full-body crop makes the face unreadable). Save it as:

```
assets/profile.jpg
```

Roughly 600×600px is plenty. Until this file exists the site shows a slate "MR" circle
instead — it never shows a broken image.

### 2. Live URL — already set ✅

The site is wired to **<https://mdxdxbhub2026.github.io/Portfolio/>** in the four tags near
the top of `index.html` (`canonical`, `og:url`, `og:image`, `twitter:image`). These must stay
**absolute URLs** — LinkedIn will not follow a relative path when it builds the preview card.

If you ever rename the repo, update all four.

### 3. Optional extras

- **GitHub icon** — the sidebar GitHub link is commented out. Uncomment it and add your
  handle, or leave it hidden.
- **Download CV** — drop your PDF at `assets/Manoj-Rajan-CV.pdf`, or delete that block
  from the sidebar.
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

## Editing the content later

Everything lives in `index.html`, in plain readable sections marked with comment banners
(`ABOUT`, `EXPERIENCE`, `SKILLS`, `EDUCATION`, `CERTIFICATIONS`). To add a skill badge,
copy an existing `<li>` in that category and change the text. To add a role, copy a whole
`<li class="reveal relative">` block in the experience timeline.

Commit the change and GitHub Pages redeploys within a minute or so.

## Local preview

```bash
python -m http.server 8899
```

Then open <http://localhost:8899>. Use a server rather than double-clicking the file —
opening via `file://` breaks the relative image paths.

## What's built in

- Sticky full-height sidebar on desktop, collapsing to a hamburger bar under 1024px
- Smooth scrolling with active-link highlighting driven by scroll position
- Dark/light toggle, remembered in `localStorage`, defaulting to your system setting
- Accessibility: skip link, ARIA labels, `aria-current` on the active nav item, visible
  focus rings, `Esc` to close the mobile menu, and full `prefers-reduced-motion` support
- `Person` JSON-LD structured data for search engines
- Print stylesheet — "Save as PDF" from the browser produces a clean document
