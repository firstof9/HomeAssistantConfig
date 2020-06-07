{% for state in states.binary_sensor if 'vmtbsh02_ha_dockermon' in state.entity_id %}
{% set string = state.entity_id.split('.')[1] %}
{% set server = string.split('_')[0] %}
{% set container = string.replace(server + "_ha_dockermon_","") %}
docker*{{container}}\_memory: {%raw%}'{{states.binary_sensor.{%endraw%}{{server}}{%raw%}\_ha_dockermon*{%endraw%}{{container}}{%raw%}.attributes.memory}}'{%endraw%}
docker*{{container}}\_netrx: {%raw%}'{{states.binary_sensor.{%endraw%}{{server}}{%raw%}\_ha_dockermon*{%endraw%}{{container}}{%raw%}.attributes.network*rx_total}}'{%endraw%}
docker*{{container}}_nettx: {%raw%}'{{states.binary_sensor.{%endraw%}{{server}}{%raw%}\_ha_dockermon_{%endraw%}{{container}}{%raw%}.attributes.network_tx_total}}'{%endraw%}
{% endfor %}
