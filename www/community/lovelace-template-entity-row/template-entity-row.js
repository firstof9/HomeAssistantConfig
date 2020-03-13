!function(t){var e={};function i(o){if(e[o])return e[o].exports;var s=e[o]={i:o,l:!1,exports:{}};return t[o].call(s.exports,s,s.exports,i),s.l=!0,s.exports}i.m=t,i.c=e,i.d=function(t,e,o){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:o})},i.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(i.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)i.d(o,s,function(e){return t[e]}.bind(null,s));return o},i.n=function(t){var e=t&&t.__esModule?function(){return t.default}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="",i(i.s=1)}([function(t){t.exports=JSON.parse('{"name":"template-entity-row","private":true,"version":"1.0.1","description":"","scripts":{"build":"webpack","watch":"webpack --watch --mode=development","update-card-tools":"npm uninstall card-tools && npm install thomasloven/lovelace-card-tools"},"repository":{"type":"git","url":"github.com:thomasloven/lovelace-template-entity-row"},"keywords":[],"author":"Thomas Lovén","license":"MIT","devDependencies":{"webpack":"^4.41.5","webpack-cli":"^3.3.10"},"dependencies":{"card-tools":"github:thomasloven/lovelace-card-tools"}}')},function(t,e,i){"use strict";i.r(e);const o=customElements.get("home-assistant-main")?Object.getPrototypeOf(customElements.get("home-assistant-main")):Object.getPrototypeOf(customElements.get("hui-view")),s=o.prototype.html;o.prototype.css;function n(){return document.querySelector("home-assistant")?document.querySelector("home-assistant").hass:document.querySelector("hc-main")?document.querySelector("hc-main").hass:void 0}let r=function(){if(window.fully&&"function"==typeof fully.getDeviceId)return fully.getDeviceId();if(!localStorage["lovelace-player-device-id"]){const t=()=>Math.floor(1e5*(1+Math.random())).toString(16).substring(1);localStorage["lovelace-player-device-id"]=`${t()}${t()}-${t()}${t()}`}return localStorage["lovelace-player-device-id"]}();function a(t){return!!String(t).includes("{%")||(!!String(t).includes("{{")||void 0)}function c(t,e,i){t||(t=n().connection);let o={user:n().user.name,browser:r,hash:location.hash.substr(1)||" ",...i.variables},s=i.template,a=i.entity_ids;return t.subscribeMessage(t=>{let i=t.result;i=i.replace(/_\([^)]*\)/g,t=>n().localize(t.substring(2,t.length-1))||t),e(i)},{type:"render_template",template:s,variables:o,entity_ids:a})}const l=["icon","active","name","secondary","state","condition","image","entity","color"];class d extends o{static get properties(){return{hass:{},state:{}}}setConfig(t){this._config={...t},this.state={...this._config};let e=this._config.entity_ids;e||!this._config.entity||a(this._config.entity)||(e=[this._config.entity]);for(const t of l)this._config[t]&&a(this._config[t])&&c(null,e=>{this.state[t]=e,this.requestUpdate()},{template:this._config[t],variables:{config:this._config},entity_ids:e})}render(){if(void 0!==this.state.condition&&"true"!==String(this.state.condition).toLowerCase())return s``;const t=this.hass.states[this.state.entity],e=t&&JSON.parse(JSON.stringify(t))||{entity_id:"light.",attributes:{icon:"no:icon"}},i=void 0!==this.state.icon?this.state.icon||"no:icon":void 0,o=this.state.image,n=void 0!==this.state.name?this.state.name:t?t.attributes.friendly_name||t.entity_id:void 0,r=this.state.secondary,c=void 0!==this.state.state?this.state.state:e?e.state:void 0,l=void 0!==this.state.active?"true"===String(this.state.active).toLowerCase():void 0;return void 0!==l&&(e.attributes.brightness=255,e.attributes.hs_color=void 0===this.state.color||a(this.state.color)?[0,0]:JSON.parse(this.state.color)),s`
      <div id="wrapper">
        <state-badge
          .hass=${this.hass}
          .stateObj=${e}
          style=${void 0!==l?l?"--paper-item-icon-color: var(--paper-item-icon-active-color, #fdd835);":"--paper-item-icon-active-color: var(--paper-item-icon-color, #44739e);":""}
          .overrideIcon=${i}
          .overrideImage=${o}
        ></state-badge>
        <div class="flex">
          <div
            class="info"
          >
            ${n}
            <div class="secondary">
              ${r}
            </div>
          </div>
          <div class="state">
          ${c}
          </div>
        </div>
      </div>
    `}static get styles(){let t=customElements.get("hui-generic-entity-row").styles;return t.cssText=t.cssText.replace(":host","#wrapper")+"\n      .state {\n        text-align: right;\n      }\n      #wrapper {\n        min-height: 40px;\n      }\n      ",t}}if(!customElements.get("template-entity-row")){customElements.define("template-entity-row",d);const t=i(0);console.info(`%cTEMPLATE-ENTITY-ROW ${t.version} IS INSTALLED`,"color: green; font-weight: bold","")}}]);