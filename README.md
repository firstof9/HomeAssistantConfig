# TBSmartHome - Home Assistant Configuration

<img align="right" src="./.assets/logo.png?raw=true">

This is my [Home Assistant](https://www.home-assistant.io/) configuration - based on many of the other great configurations are out there (and listed below)

I live in ![Australia](http://flags.ox3.in/mini/au.png) so some of what you find here may not be relevent, or you may have access to better (and probably cheaper) ways.

It's very much a work-in-progress, but feel free to steal ideas or code to use for your own setup

_Please :star: this repo if you find it useful_

![Hits](http://hits.dwyl.io/bacco007/HomeAssistantConfig.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/bacco007/HomeAssistantConfig?style=flat-square) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/bacco007/HomeAssistantConfig?style=flat-square)
![Licence](https://img.shields.io/badge/license-Unlicense-blue.svg?style=flat-square)

![Twitter Follow](https://img.shields.io/twitter/follow/bacco007?style=social)

---

## Table of Contents

- [TBSmartHome - Home Assistant Configuration](#tbsmarthome---home-assistant-configuration)
  - [Table of Contents](#table-of-contents)
  - [Ecosystem](#ecosystem)
    - [Hardware](#hardware)
    - [Zigbee](#zigbee)
  - [Stats](#stats)
  - [Integrations Used](#integrations-used)
    - [Custom Components Used](#custom-components-used)
  - [Screenshots](#screenshots)
  - [Hass.io Addons](#hassio-addons)
  - [Other Good HA Resources/Configs](#other-good-ha-resourcesconfigs)

---

## Ecosystem

My smarthome setup seems to be ever-growing, but at this stage it's unlikely that I'll make any major changes from here

### Hardware

- Dell Optiplex 9020 SFF (i5, 24Gb RAM, 500Gb HDD) running Proxmox
  - I run two VMs from this machine, one for Hass.IO and related elements and one for other home server stuff
- Lenovo ThinkMachine M73 Tiny (Intel Pentium G3240T, 4Gb RAM, 500Gb HDD)
  - Ubuntu Server 18.10, this machine runs my UniFi controller and Nginx Reverse Proxy Setup
- Raspberry Pi 3
  - Pi-Hole

### Zigbee

I'm running a combination of Xiaomi Aqara and Samsung SmartThings sensors and a ConBee II as the host

---

## Stats

_Stats as at {{ states('sensor.time') }}, {{ states('sensor.date_long_format') }}_

| HA Version                               | No. Integrations                                        | No. Entities | No. Sensors | No. Automations |
| ---------------------------------------- | ------------------------------------------------------- | ------------ | ----------- | --------------- |
| {{ states('sensor.ha_current_version')}} | {{ states.sensor.hass_main_config.attributes.components | count }}     | {{states    | count}}         | {{states.sensor | count}} | {{states.automation | count}} |

---

## Integrations Used

Here is a list of all the integrations I use, including any Custom Components (which are also listed below)

<details>
<summary>Expand Integrations List</summary>
{% set a = states.sensor.hass_main_config.attributes.components %}
{% for integration in a|sort %}
- [{{integration}}](https://www.home-assistant.io/components/{{integration}}){% endfor -%}
</details>

{% if custom_components %}

### Custom Components Used

<details>
<summary>Expand Custom Components List</summary>
{% for integration in custom_components|sort(attribute='name') %}
- [{{integration.name}}]({{integration.documentation}}){% endfor -%}
{% endif %}
</details>

---

## Screenshots

![Screenshot - Home](./.assets/screencapture-home.png?raw=True)

<details>
<summary>More Screenshots Here</summary>

![Screenshot - System](./.assets/screencapture-system.png?raw=True)

![Screenshot - Fire](./assets/screencapture-fire.png?raw=True)

![Screenshot - HA](./.assets/screencapture-homeassistant.png?raw=True)

</details>

---

## Hass.io Addons

Here are the addons I use inside Hass.io, some of the other things I run can be done inside Hass.io, but I've elected not to do so.

- [ADB - Android Debug Bridge](https://github.com/hassio-addons/addon-adb)
- [Almond]()
- [AppDaemon](https://github.com/hassio-addons/addon-appdaemon3)
- [deCONZ](https://github.com/home-assistant/hassio-addons/tree/master/deconz)
- [Grafana](https://github.com/hassio-addons/addon-grafana)
- [Home Panel]()
- [InfluxDB](https://github.com/hassio-addons/addon-influxdb)
- [JupyterLab Lite](https://github.com/hassio-addons/addon-jupyterlab-lite)
- [MQTT Server & Web Client](https://github.com/hassio-addons/addon-mqtt/)
- [MariaDB]()
- [Node-RED](https://github.com/hassio-addons/addon-node-red/)
- [SQLite Web](https://github.com/hassio-addons/addon-sqlite-web/)
- [SSH & Web Terminal](https://github.com/hassio-addons/addon-ssh/)
- [Visual Studio Code]()

---

## Other Good HA Resources/Configs

These resources have either provided inspiration or some great code that has helped me get my configuration up and running

- [aFFekopp/homeassistant](https://github.com/aFFekopp/homeassistant)
  - This is where I've copied the great theme from
- [danrspencer/hass-config](https://github.com/danrspencer/hass-config)
- [JamesMcCarthy79/Home-Assistant-Config](https://github.com/JamesMcCarthy79/Home-Assistant-Config)
- [jimz011/homeassistant](https://github.com/jimz011/homeassistant)
- [Limych/HomeAssistantConfiguration](https://github.com/Limych/HomeAssistantConfiguration)

---

Generated by the [custom readme integration](https://github.com/custom-components/readme)
