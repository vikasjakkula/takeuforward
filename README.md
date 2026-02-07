# Code – Learning & Practice

Quick reference for basics and where to find things. **Main focus: C, Python, JavaScript** (in `code1`). Rest (CSS, HTML, Next.js, scraping, SQL) lives in `code2` for occasional use.

---

## Folder structure

| Folder | Use | Contents |
|--------|-----|----------|
| **code1/** | **Primary** – learn and write code here | C, Python, JavaScript |
| **code2/** | **Secondary** – once in a blue moon | CSS, HTML, Next.js, scraping, SQL |

- **code1** = daily learning and practice (C, Python, JS).
- **code2** = reference and rare practice for other topics.

---

## Basics (short, pointwise)

### C (`code1/c/`)
- Compiled, procedural; no OOP built-in.
- Types: `int`, `float`, `char`, arrays, structs.
- Pointers: variables that hold addresses; `*` and `&`.
- Memory: manual (no GC); `malloc`/`free` for heap.
- Control: `if`, `for`, `while`, `switch`.
- Functions: pass by value; use pointers to modify in place.
- Files: `FILE*`, `fopen`, `fread`/`fwrite`/`fprintf`, `fclose`.

### Python (`code1/python/`)
- Interpreted, dynamic typing; indentation = blocks.
- Types: `int`, `float`, `str`, `list`, `dict`, `set`, `tuple`.
- Control: `if`/`elif`/`else`, `for`, `while`; `range()` in loops.
- Functions: `def`; optional args, `*args`, `**kwargs`.
- No pointers; mutable vs immutable (lists vs tuples/strings).
- Files: `open()`, `read`/`write`, context manager `with`.

### JavaScript (`code1/js/`)
- Runs in browser and Node (or Bun); single-threaded, event loop.
- Types: primitives + objects; `typeof`, loose typing.
- Control: `if`, `for`, `while`, `for...of`, `for...in`.
- Functions: `function`, arrow `() =>`; callbacks, promises, `async/await`.
- DOM: select elements, add listeners, change content/style.
- Modules: `import`/`export` (ESM).

### CSS (`code2/css/`)
- Selectors: element, `.class`, `#id`, combinators, pseudo-classes.
- Box model: content, padding, border, margin.
- Layout: `display` (block/inline/flex/grid), Flexbox, Grid.
- Units: `px`, `em`, `rem`, `%`, `vw`/`vh`.
- Responsive: media queries, mobile-first.

### HTML (`code2/html/`)
- Structure: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`.
- Tags: headings, paragraphs, lists, links, images, forms, tables.
- Semantic: `<header>`, `<main>`, `<nav>`, `<article>`, `<footer>`.
- Forms: `<form>`, `<input>`, `<button>`, `action`, `method`.

### Next.js (`code2/nextjs/`)
- React framework: file-based routing (`app/` or `pages/`).
- Pages: create file → get route; `layout.tsx` for shared UI.
- Data: fetch on server, pass as props; API routes for backend.
- Build & run: `npm run dev`, `npm run build`, `npm start`.

### Scraping (`code2/scraping/`)
- Fetch: HTTP client (e.g. `requests` in Python).
- Parse: HTML/XML parsers (e.g. BeautifulSoup, lxml).
- Extract: selectors (CSS/XPath), then save (CSV, JSON, DB).
- Ethics: respect `robots.txt`, rate limit, don’t overload servers.

### SQL (`code2/sql/`)
- Tables: `CREATE TABLE`, columns and types.
- Queries: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`.
- Filter/join: `AND`/`OR`, `IN`, `LIKE`; `JOIN` (INNER, LEFT).
- Change data: `INSERT`, `UPDATE`, `DELETE`.

---

## Run / install

- **JS (Bun):** From project root: `bun install`, then `bun run script.js`.
- **C:** Compile with `gcc file.c -o out` then run `./out`.
- **Python:** `python script.py` or `python3 script.py`.
- **Next.js:** `cd code2/nextjs/<project>` then `npm install` and `npm run dev`.

Navigate: **code1** for C, Python, JS; **code2** for the rest.
