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
    3. Replace members.csv with the new export (retain only the four
       columns: Full Name, City / Town, State / Union Territory,
       Organization / Institution Name).
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
<div id="member-dir-controls" class="mb-4">
  <div class="columns is-multiline is-vcentered">
    <div class="column is-12-mobile is-5-tablet is-5-desktop">
      <div class="field">
        <label class="label is-small" for="md-search">Search</label>
        <div class="control has-icons-left">
          <input id="md-search" class="input is-small" type="search"
                 placeholder="Search by name or organisation…" autocomplete="off">
          <span class="icon is-left is-small"><i class="fas fa-search"></i></span>
        </div>
      </div>
    </div>
    <div class="column is-6-mobile is-3-tablet is-3-desktop">
      <div class="field">
        <label class="label is-small" for="md-city">City / Town</label>
        <div class="control">
          <div class="select is-small is-fullwidth">
            <select id="md-city"><option value="">All cities</option></select>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-6-mobile is-3-tablet is-3-desktop">
      <div class="field">
        <label class="label is-small" for="md-state">State</label>
        <div class="control">
          <div class="select is-small is-fullwidth">
            <select id="md-state"><option value="">All states</option></select>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-6-mobile is-1-tablet is-1-desktop" style="padding-top:1.75rem">
      <button id="md-reset" class="button is-small is-light is-fullwidth"
              type="button" title="Clear filters">Reset</button>
    </div>
  </div>
  <p id="md-count" class="is-size-7 has-text-grey"></p>
</div>
"""

# Vanilla JS placed after the columns section so the table is already in the DOM.
# Columns: 0=#  1=Name  2=City/Town  3=State  4=Organisation
FILTER_SCRIPT = """\
<script>
(function () {
  var controls = document.getElementById('member-dir-controls');
  if (!controls) return;

  // The only table on the page is the member table
  var table = document.querySelector('table');
  if (!table) return;

  var tbody = table.querySelector('tbody');
  if (!tbody) return;

  var rows     = Array.from(tbody.querySelectorAll('tr'));
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
            if name:
                members.append({"name": name, "city": city, "state": state, "org": org})
    members.sort(key=lambda r: r["name"].lower())
    return members


def build_table(members: list[dict]) -> str:
    lines = [
        "| # | Name | City / Town | State | Organisation |",
        "|---|------|-------------|-------|--------------|",
    ]
    for i, m in enumerate(members, start=1):
        org = m["org"] if m["org"] else "—"
        org = org.replace("|", "\\|")
        name = m["name"].replace("|", "\\|")
        city = m["city"].replace("|", "\\|")
        state = m["state"].replace("|", "\\|")
        lines.append(f"| {i} | {name} | {city} | {state} | {org} |")
    return "\n".join(lines)


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

{{{{< columns-start >}}}}
{{{{< column-start class="is-flex-direction-column is-full">}}}}
{{{{< rich-box-start >}}}}
{{{{< rich-content-start themeClass="coloring-1" >}}}}

{CONTROLS_HTML}
{build_table(members)}

{{{{< rich-content-end >}}}}
{{{{< rich-box-end >}}}}
{{{{< column-end >}}}}
{{{{< columns-end >}}}}

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
