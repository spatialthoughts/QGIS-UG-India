#!/usr/bin/env python3
"""
Generate index.md from members.csv.

All files live together in content/member-directory/:
    members.csv                 — source of truth (update this from the Google Form export)
    update-member-directory.py  — this script
    index.md                    — generated output (do not edit by hand)

Usage:
    python3 content/member-directory/update-member-directory.py

Workflow for updating the member list:
    1. Export the latest responses from the Google Form as CSV.
    2. Keep only rows where consent was given.
    3. Replace members.csv with the new export (retain only the columns:
       Full Name, City / Town, State / Union Territory,
       Organization / Institution Name, LinkedIn).
    4. Run this script.
    5. Commit both members.csv and index.md.
"""

import csv
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "members.csv"
OUTPUT_PATH = SCRIPT_DIR / "index.md"

FORM_URL = "https://forms.gle/Y738efwadTUFggpg8"

# Raw HTML injected before the markdown table — uses Bulma classes already
# loaded by the theme, so no extra CSS is needed.
CONTROLS_HTML = """\
<style>
  .md-ctrl-row { display:flex; flex-wrap:wrap; gap:0.75rem; align-items:flex-end; }
  .md-ctrl-search { flex:2 1 200px; min-width:0; }
  .md-ctrl-filter { flex:1 1 140px; min-width:0; }
  .md-ctrl-reset  { flex:0 0 auto; padding-top:1.5rem; }
  .md-ctrl-search .input,
  .md-ctrl-filter select { width:100%; box-sizing:border-box; }
  @media (max-width: 768px) {
    .md-ctrl-search,
    .md-ctrl-filter { flex:0 0 100%; }
    .md-ctrl-reset { padding-top:0; }
  }
</style>
<div id="member-dir-controls" style="margin-bottom:1rem">
  <div class="md-ctrl-row">
    <div class="md-ctrl-search">
      <label class="label is-small" for="md-search">Search</label>
      <div class="control has-icons-left">
        <input id="md-search" class="input is-small" type="search"
               placeholder="Search by name or organisation…" autocomplete="off">
        <span class="icon is-left is-small"><i class="fas fa-search"></i></span>
      </div>
    </div>
    <div class="md-ctrl-filter">
      <label class="label is-small" for="md-city">City / Town</label>
      <select id="md-city" class="input is-small" style="cursor:pointer">
        <option value="">All cities</option>
      </select>
    </div>
    <div class="md-ctrl-filter">
      <label class="label is-small" for="md-state">State</label>
      <select id="md-state" class="input is-small" style="cursor:pointer">
        <option value="">All states</option>
      </select>
    </div>
    <div class="md-ctrl-reset">
      <button id="md-reset" class="button is-small is-light" type="button"
              title="Clear filters">Reset</button>
    </div>
  </div>
  <p id="md-count" class="is-size-7 has-text-grey" style="margin-top:0.5rem"></p>
</div>
"""

# Vanilla JS placed after the columns section so the table is already in the DOM.
# Columns: 0=#  1=Name  2=City/Town  3=State  4=Organisation
FILTER_SCRIPT = """\
<script>
(function () {
  var controls = document.getElementById('member-dir-controls');
  if (!controls) return;

  var tbody = document.getElementById('member-tbody');
  if (!tbody) return;

  var rows = Array.from(tbody.querySelectorAll('tr'));
  var searchEl = document.getElementById('md-search');
  var cityEl   = document.getElementById('md-city');
  var stateEl  = document.getElementById('md-state');
  var resetBtn = document.getElementById('md-reset');
  var countEl  = document.getElementById('md-count');

  function cellText(row, idx) {
    var cells = row.querySelectorAll('td');
    return cells[idx] ? cells[idx].textContent.trim() : '';
  }

  // Populate dropdowns with unique sorted values from table data
  function uniqueSorted(idx) {
    return Array.from(new Set(rows.map(function (r) { return cellText(r, idx); })
      .filter(Boolean))).sort(function (a, b) {
        return a.localeCompare(b, 'en', { sensitivity: 'base' });
      });
  }

  uniqueSorted(2).forEach(function (v) { cityEl.add(new Option(v, v)); });
  uniqueSorted(3).forEach(function (v) { stateEl.add(new Option(v, v)); });

  function applyFilters() {
    var q     = searchEl.value.toLowerCase().trim();
    var city  = cityEl.value;
    var state = stateEl.value;
    var shown = 0;

    rows.forEach(function (row) {
      var name    = cellText(row, 1).toLowerCase();
      var rowCity = cellText(row, 2);
      var rowState= cellText(row, 3);
      var org     = cellText(row, 4).toLowerCase();

      var match = (!q     || name.includes(q) || org.includes(q))
               && (!city  || rowCity  === city)
               && (!state || rowState === state);

      row.style.display = match ? '' : 'none';
      if (match) shown++;
    });

    var total = rows.length;
    countEl.textContent = shown === total
      ? 'Showing all ' + total + ' members'
      : shown + ' of ' + total + ' members';
  }

  searchEl.addEventListener('input',  applyFilters);
  cityEl.addEventListener('change',   applyFilters);
  stateEl.addEventListener('change',  applyFilters);

  resetBtn.addEventListener('click', function () {
    searchEl.value = '';
    cityEl.value   = '';
    stateEl.value  = '';
    applyFilters();
  });

  applyFilters();
}());
</script>
"""


def load_members(csv_path: Path) -> list[dict]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        members = []
        for row in reader:
            name = row.get("Full Name", "").strip()
            city = row.get("City / Town", "").strip()
            state = row.get("State / Union Territory", "").strip()
            org = row.get("Organization / Institution Name", "").strip()
            linkedin = row.get("LinkedIn", "").strip()
            if name:
                members.append({"name": name, "city": city, "state": state, "org": org, "linkedin": linkedin})
    members.sort(key=lambda r: r["name"].lower())
    return members


def esc(text: str) -> str:
    """Minimal HTML escaping for table cell content."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_table(members: list[dict]) -> str:
    rows = []
    for i, m in enumerate(members, start=1):
        org = esc(m["org"]) if m["org"] else "<span style='color:#aaa'>—</span>"
        linkedin = (
            f' <a href="{esc(m["linkedin"])}" target="_blank" rel="noopener" '
            f'title="LinkedIn Profile" style="color:#0077b5">'
            f'<i class="fab fa-linkedin"></i></a>'
            if m["linkedin"]
            else ""
        )
        rows.append(
            f"  <tr>"
            f"<td>{i}</td>"
            f"<td><strong>{esc(m['name'])}</strong>{linkedin}</td>"
            f"<td>{esc(m['city'])}</td>"
            f"<td>{esc(m['state'])}</td>"
            f"<td>{org}</td>"
            f"</tr>"
        )
    return (
        '<div class="table-container">\n'
        '<table class="table is-striped is-hoverable is-fullwidth is-narrow">\n'
        "  <thead><tr>"
        "<th>#</th>"
        "<th>Name</th>"
        "<th>City / Town</th>"
        "<th>State</th>"
        "<th>Organisation</th>"
        "</tr></thead>\n"
        "  <tbody id='member-tbody'>\n"
        + "\n".join(rows)
        + "\n  </tbody>\n</table>\n</div>"
    )


def main():
    today = date.today().strftime("%B %d, %Y")
    members = load_members(CSV_PATH)

    content = f"""\
---
type: "page"
title: "Member Directory"
subtitle: "QGIS India User Group members across the country"
draft: false
sidebar: true
---

{{{{< content-start >}}}}

# Member Directory

This directory lists members of the QGIS India User Group who have chosen to be listed publicly. The list is sorted alphabetically by name.

Want to be listed here, or update your entry? Fill in the [member registration form]({FORM_URL}).

> **Last updated:** {today}  |  **Total members listed:** {len(members)}

{CONTROLS_HTML}

{build_table(members)}

{FILTER_SCRIPT}

{{{{< rich-box-start icon="📋" layoutClass="tips">}}}}

##### Join or Update Your Listing

Not in the directory yet, or need to update your details? Use the [member registration form]({FORM_URL}) — it only takes a minute.

{{{{< rich-content-end >}}}}
{{{{< rich-box-end >}}}}

{{{{< content-end >}}}}
"""

    OUTPUT_PATH.write_text(content, encoding="utf-8")
    print(f"Written {len(members)} members to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
