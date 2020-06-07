# 🏠TBSmartHome - Home Assistant Configuration <!-- omit in toc -->

## Dwains-Theme - Page Configs <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [More Pages](#more-pages)
  - [Media](#media)

---

## More Pages

<p align="right"><a href="#top" title="Back to top">Top</a></p>

### Media

| Element | Packages                                                                                                                                                                                                                                                                                                                                                                                | Notes                                                                                                                         |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Sonarr  | [Sonarr Sensors](../../packages/services/sonarr.yaml)<br/>[Sonarr Upcoming Media](../../packages/services/sonarr_upcoming_media.yaml)<br/> [Custom Upcoming Media Sensors](../../packages/media/upcomingmedia/upcomingmedia_sonarr.yaml)                                                                                                                                                | Requires [Sonarr Upcoming Media](https://github.com/custom-components/sensor.sonarr_upcoming_media) Custom Component          |
| Radarr  | [Radarr Sensors](../../packages/services/radarr.yaml)<br/>[Radarr Upcoming Media](../../packages/services/radarr_upcoming_media.yaml)<br/>[Custom Upcoming Media Sensors](../../packages/media/upcomingmedia/upcomingmedia_radarr.yaml)                                                                                                                                                 | Requires [Radarr Upcoming Media](https://github.com/custom-components/sensor.radarr_upcoming_media) Custom Component          |
| Plex    | Plex Sensors (Setup in UI)<br/>[Plex Recently Added](../../packages/services/plex_upcoming_media.yaml)<br/>[Tautulli](../../packages/services/plex_tautulli.yaml)<br/>[Custom Recently Added Sensors - TV](.././packages/media/upcomingmedia/upcomingmedia_plex_tv.yaml)<br/>[Custom Recently Added Sensors - Movies](.././packages/media/upcomingmedia/upcomingmedia_plex_movies.yaml) | Requires [Plex Recently Added](https://github.com/custom-components/sensor.plex_recently_added) Custom Component and Tautulli |

![Screenshot - More](../../.assets/more_media.png?raw=True)

<p align="right"><a href="#top" title="Back to top">Top</a></p>
