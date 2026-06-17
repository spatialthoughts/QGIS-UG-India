---
type: "page"
title: "Every Map is a Story: From QGIS to Social Media"
subtitle: "Tips, resources, and articles for QGIS users"
draft: false
date: 2026-06-17
sidebar: true
thumbnail: "./img/storytelling-with-qgis/gorakhpur_pm25_animation.gif"
og_image: "blog/img/storytelling-with-qgis/gorakhpur_pm25_animation.gif"
author: "Jyoti"
---

{{< content-start >}}

# Every Map is a Story: From QGIS to Social Media

Maps are often viewed as technical tools for analysis. However, they are also powerful instruments of storytelling -- making complex data easier to grasp and enabling us to weave a compelling narrative. So how does one move from a blank QGIS canvas to an impactful social media post? Read on, as I walk you through our process from a mere thought to a tangible output.

## Finding the Narrative

A map is more than just a collection of coordinates and pixels - it is a [conversation](https://wri-india.org/perspectives/tangible-insights-planning-resilience-physical-maps). Every map starts long before we begin technical production. We don't just look for datasets; we look for a story to tell. Everything, from data to the processing tool, revolves around this narrative that is timely and meaningful, with the intent of turning a global climate conversation into a locally contextualised story.

At [WRI India](https://wri-india.org/), we rely heavily on open-source data. [Google Earth Engine Catalog](https://developers.google.com/earth-engine/datasets) and [GEE community catalogs](https://gee-community-catalog.org/) help us with analysis-ready data like global population density layers and climate data that save us hours of preprocessing. A huge part of our workflow involves taking traditional data, such as data from the Census of India, and connecting it with spatial parameters to visualise patterns that are otherwise invisible in its raw form. For example, on [World Habitat Day](https://www.linkedin.com/posts/wri-india_habitat-day-activity-7115182635575853056-gBTV?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy), we focused on Tamil Nadu, creating a visualisation of migration data from Census 2011 and spatially joining it with administrative units to reveal hitherto invisible patterns of migration in the state.

<p align="center">
  <img src="../img/storytelling-with-qgis/tamil_nadu_migration_map.webp" alt="Map showing number of male migrants by place of birth in Tamil Nadu">
</p>
<p align="center"><em>Map showing number of male migrants by place of birth other than place of enumeration in Tamil Nadu, created for World Habitat Day 2023.</em></p>

## Curating the Visual Language

Once our narrative and data choice is clear, we then move to the phase: "How should the data look?" We break the visual language into colours, shapes, and symbols. Our blog on [air quality in Gorakhpur](https://wri-india.org/perspectives/gorakhpur-changing-so-its-air) is a good example of how we decipher visual language.

<p align="center">
  <img src="../img/storytelling-with-qgis/gorakhpur_pm25_animation.gif" alt="Animation showing monthly PM2.5 concentrations in North India">
</p>
<p align="center"><em>Animation showing monthly PM2.5 concentrations in North India, created for a blog focused on Gorakhpur's air quality.</em></p>

**Colours for Impact:** We pick colours based on the emotion we want to convey through the narrative. For the Gorakhpur story, we chose a palette of deep reds, oranges and yellows to naturally raise a sense of urgency. Similarly, in a [heat-stress](https://www.linkedin.com/feed/update/urn:li:activity:6929397697359548416/) story, hot colours (using a heatmap with a gradual gradient) immediately convey a region grappling with heat. To depict the economic growth of a city region, we used [nightlights](https://www.linkedin.com/posts/wri-india_internationaldayoflight-internationaldayoflight-activity-7329026474487771138-5I7E?utm_source=share&utm_medium=member_desktop&rcm=ACoAACGfJIsBXwW-3cAgkRqbM6IZvHB0LtiNnGQ) and a dark-mode aesthetic, letting the yellow lights glow through.

<p align="center">
  <img src="../img/storytelling-with-qgis/urban_heat_island_animation.gif" alt="Animation showing Urban Heat Island effect in four Indian cities">
</p>
<p align="center"><em>Animation showing Urban Heat Island effect in four Indian cities.</em></p>

<p align="center">
  <img src="../img/storytelling-with-qgis/nightlights_cities_animation.gif" alt="Animation showing long-term changes in intensity of nightlights in four Indian cities">
</p>
<p align="center"><em>Animation shows long-term changes in intensity of nightlights in four Indian cities, created for International Day of Light 2024.</em></p>

**Labels for Geographical Context**: Because the story focuses on Gorakhpur, we used a bold white label for the city. We also marked Delhi in bold because the national capital provides a familiar geographical context for readers. We styled the word "HIMALAYAS" in bold, spread-out capitals to deliver the narrative that these mountains act as a physical barrier, trapping pollutants in the northern plains. Other mountain ranges were set in smaller capital italics, and other country names in light capitals, ensuring that Gorakhpur and the Himalayas remain the story's focal point.

**Shapes and Symbols:** The choice of geometric shapes how the audience perceives the relationships among different datasets. We use small, subtle dots to mark city locations. These tiny symbols are essential for providing geographical context without distracting from the main story. In our post on [Economic Growth in the National Capital Region (NCR)](https://www.linkedin.com/feed/update/urn:li:activity:7198645426634317824/), we used two distinct shapes to tell a single story. To represent employment, we use graduated circles. By scaling bubble sizes with the number of jobs, we gave the data physical weight, allowing the eye to instantly identify major hubs like Delhi by their size alone.

<p align="center">
  <img src="../img/storytelling-with-qgis/ncr_nightlights_economic_activity.gif" alt="Animation showing long-term changes in nightlights and economic activity in NCR">
</p>
<p align="center"><em>Animation showing the long-term changes in intensity of nightlights and economic activity in and around the National Capital Region (NCR), created for International Day of Light 2025.</em></p>

### The Art of Letting Go

As Antoine de Saint-Exupery rightly said, *"Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."*

State, country or municipal boundaries are essential for context, but they should not compete with the data or the story we want to tell. We always mute elements that initially seem important to the story but ultimately do not serve the main narrative. This greatly reduces the cognitive load on the viewer, allowing them to understand the message and visualisation at a quick glance.

For instance, in our [World Rivers Day](https://www.linkedin.com/posts/wri-india_worldriversday-ecocityregions-thrivingecocityregions-activity-7111945976013033472-30As?utm_source=share&utm_medium=member_desktop) post, the Metropolitan Area Boundary of Srinagar is greyed out to avoid distracting the audience from the main story -- the built-up expansion over floodplains. While visualising [nightlights](https://www.linkedin.com/posts/wri-india_internationaldayoflight-internationaldayoflight-activity-7329026474487771138-5I7E?utm_source=share&utm_medium=member_desktop&rcm=ACoAACGfJIsBXwW-3cAgkRqbM6IZvHB0LtiNnGQ), we keep city administrative boundaries subtle to gently indicate urban growth doesn't always stop where a city ends. Similarly, in our post on [Tamil Nadu](https://www.linkedin.com/posts/wri-india_habitat-day-activity-7115182635575853056-gBTV?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy), we refrained from showing other states' boundaries. Our intention was to keep the audience's eye within the state, and this was achieved by keeping the background muted and giving the Tamil Nadu polygon a popping-up effect.

<p align="center">
  <img src="../img/storytelling-with-qgis/kashmir_builtup_growth_animation.gif" alt="Animation showing long-term built-up growth in the Kashmir Valley">
</p>
<p align="center"><em>Animation showing long-term built-up growth in the Kashmir Valley, overlaid with the 2014 flood extent, created for World Rivers Day 2023.</em></p>

### The Final Touch

While QGIS is where the data processing and basic cartography happens, the final look is often a team effort. We work with our design team to give visuals a more polished look. They help us move beyond the technical GIS look to create something that resonates with all. They help us refine our colour palette and add graphic elements that match the theme. For example, on [World Rivers Day](https://www.linkedin.com/posts/wri-india_worldriversday-ecocityregions-thrivingecocityregions-activity-7111945976013033472-30As?utm_source=share&utm_medium=member_desktop), we added mountainous scenery as background graphic elements, which made the visual feel more fluid and engaging. We have also found that animations are one of the most powerful ways to show changing patterns -- whether it's the expansion of a city's economic footprint or rising temperatures.

### Conclusion

We have seen how spatial data can move beyond technical reports and reach a wider audience through these international days. Our goal in doing so remains the same - to make the invisible visible. For the QGIS India community, this is a reminder that geospatial and cartographic skills are powerful tools for increasing awareness and sparking conversations that might otherwise get lost. All we need is a clear narrative, the right data and a design that speaks.

As we continue to map the challenges of our climate and environment, we hope these stories inspire others to look at their own narratives and data, not just as numbers, but as stories waiting to be told.

### About the Author

[Jyoti](https://www.linkedin.com/in/jyotisingh26/) is a geospatial analyst at WRI India, where she's spent over six years using maps to drive data-led decision-making. Her work focuses on turning complex data into actionable insights for a sustainable future. She has contributed to vulnerability assessments, heat mitigation strategies, and air quality initiatives at regional and local scales in India.

She is passionate about public communication and raising awareness through social media. An avid QGIS user, she loves experimenting with new cartographic styles and sharing tips and tricks she has learned along the way with the wider GIS community.

Explore a collection of her maps and projects [here](https://geo-ti.github.io/portfolio/).

## Contributors

[Raj Bhagat Palanichamy](https://www.linkedin.com/in/raj-bhagat-palanichamy-098a1827/), Senior Program Manager - GeoAnalytics, WRI India

[Rama Thoopal](https://www.linkedin.com/in/ramathoopal/), Director - Communications, WRI India

{{< content-end >}}
