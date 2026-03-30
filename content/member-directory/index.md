---
type: "page"
title: "Member Directory"
subtitle: "QGIS India User Group members across the country"
draft: false
sidebar: true
---

{{< content-start >}}

# Member Directory

This directory lists members of the QGIS India User Group who have chosen to be listed publicly. The list is sorted alphabetically by name.

Want to be listed here, or update your entry? Fill in the [member registration form](https://forms.gle/Y738efwadTUFggpg8).

> **Last updated:** March 30, 2026  |  **Total members listed:** 28

{{< columns-start >}}
{{< column-start class="is-flex-direction-column is-full">}}
{{< rich-box-start >}}
{{< rich-content-start themeClass="coloring-1" >}}

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

| # | Name | City / Town | State | Organisation |
|---|------|-------------|-------|--------------|
| 1 | Abhilasha | New Delhi | Delhi | Jawaharlal Nehru University, New Delhi |
| 2 | Abhishek Goyal | Jodhpur | Rajasthan | Kanha Technocrats |
| 3 | Amruth Kiran | Bengaluru | Karnataka | Indian Institute for Human Settlements |
| 4 | Anand Kumar Gupta | Dehradun | Uttarakhand | Wadia Institute of Himalayan Geology, Dehradun |
| 5 | Ankita Raju Khobragade | Nagpur | Maharashtra | Vasantrao Naik Government Institute of Arts and Social Sciences Nagpur |
| 6 | Arun P A | Mananthavdy | Kerala | Impact Metrics LLP |
| 7 | Arvind Kumar Pandey | Tirupati | Andhra Pradesh | Indian Institute of Technology (IIT) |
| 8 | Asok Kumar Kar | Bengaluru | Karnataka | APF |
| 9 | Dr. Mitali Chandnani | Bengaluru | Karnataka | rize.farm |
| 10 | Dr. Vaibhav Puri | New Delhi | New Delhi | Sri Guru Gobind Singh College Of Commerce, Delhi University |
| 11 | Gaurav Khairnar | Hyderabad | Telangana | Indian National Centre for Ocean Information Services, Hyderabad |
| 12 | Khushbu Birawat | Bengaluru | Karnataka | WE360 - Water and Environment Consultants |
| 13 | Khushdeep Kaur | Ahmedabad | Gujarat | Ahmedabad University |
| 14 | Kiran Bhamblani | Vadodara | Gujarat | — |
| 15 | Nitin Pandit | Devrukh | Maharashtra | Independent |
| 16 | Parimelazhagan D | Bangalore | Karnataka | Louis Dreyfus Company India |
| 17 | Parth Godhani | Rajkot | Gujarat | Environment Auditor |
| 18 | Pulakesh Pradhan | Kharagpur | West Bengal | Ravenshaw University |
| 19 | Sanjana A H | Valancherry, Malappuram | Kerala | — |
| 20 | Santanu Samanta | Kolkata | West Bengal | NeoGeoInfo Technologies Ltd. |
| 21 | Satish Khamkar | Pune | Maharashtra | TomTom |
| 22 | Shailesh Chaure | Indore | Madhya Pradesh | Govt. Holkar Science College, Indore |
| 23 | Shashank Palur | Bengaluru | Karnataka | WELL Labs |
| 24 | Shyama Mohan | Hyderabad | Telangana | NIGST, Survey of India |
| 25 | Ujaval Gandhi | Ahmedabad | Gujarat | Spatial Thoughts |
| 26 | Venkatesh Vidala | Tirupati | Andhra Pradesh | Indian Institute Of Technology (IIT) Tirupati |
| 27 | Venugopal T.V | Bangalore | Karnataka | Bhuvan Infra Tech |
| 28 | Vishal Bhave | Ratnagiri | Maharashtra | Srushti Conservation Foundation |

{{< rich-content-end >}}
{{< rich-box-end >}}
{{< column-end >}}
{{< columns-end >}}

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


{{< rich-box-start icon="📋" layoutClass="tips">}}

##### Join or Update Your Listing

Not in the directory yet, or need to update your details? Use the [member registration form](https://forms.gle/Y738efwadTUFggpg8) — it only takes a minute.

{{< rich-content-end >}}
{{< rich-box-end >}}

{{< content-end >}}
