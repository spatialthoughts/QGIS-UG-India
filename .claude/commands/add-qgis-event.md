Add an upcoming QGIS India Community Day event to `content/events.md` in the current project.

The user will provide: date, agenda items, and optionally a Google Calendar link and image filename.

## Steps

1. Read `content/events.md` to see the current state.

2. Build the event block using this exact template:

```
{{< rich-box-start layoutClass="has-right rounded" >}}
{{< rich-content-start themeClass="coloring-2" >}}

### QGIS India Community Day (MONTH YEAR)

When: DAYNAME DD MONTH YYYY, 7-8pm IST &nbsp;<i class="fas fa-calendar-plus"></i> [Add to Google Calendar](CALENDAR_LINK)

Where: Online

**Agenda**

[agenda items as nested markdown list]

<div class="buttons">
{{< button class = "is-primary1" link = "CALENDAR_LINK" text = "Add To Calendar" >}}
{{< button class = "is-light1" link = "https://us02web.zoom.us/meetings/89086905274/invitations?signature=qrvFCuaqpUGeg5vobEu7blGc-VFG94XG3eaYVx57syU" text = "Joining Info" >}}
</div>

{{< rich-content-end >}}
{{< rich-right-start >}}
![](/img/community-day-MONTH-YEAR.webp)
{{< rich-right-end >}}
{{< rich-box-end >}}
```

3. Replace the `## Upcoming Events` section content:
   - If there is a "No upcoming events" placeholder box, replace it entirely with the new event block.
   - If there is already an upcoming event, insert the new one before it (most-upcoming first).

4. If the user provided a PNG image, convert it to webp with `cwebp` and delete the original:
   ```
   cwebp static/img/FILENAME.png -o static/img/FILENAME.webp && rm static/img/FILENAME.png
   ```

## Notes
- `themeClass="coloring-2"` for upcoming events; past events use `coloring-1`
- Image convention: `community-day-MONTH-YEAR.webp` (lowercase month, e.g. `community-day-may-2026.webp`)
- Zoom link is the recurring one above — use it unless the user provides a different link
- Calendar `tmeid` is event-specific; ask the user if they haven't provided it, or use a template link without `tmeid`
- Day name: compute the correct weekday for the given date
- 7-8pm IST = 13:30–14:30 UTC
