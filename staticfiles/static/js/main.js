"use strict";(self.webpackChunkemployee=self.webpackChunkemployee||[]).push([[757],{909:(e,t,n)=>{var i=n(755);function r(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function a(e,t){for(var n=0;n<t.length;n++){var i=t[n];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(e,i.key,i)}}var o=function(){function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"body",n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:[];r(this,e),this.container=document.querySelector(t),this.internalLinks=this.container.querySelectorAll('a[href^="/"]'),this.externalLinks=this.container.querySelectorAll('a[href^="http"]'),this.anchorLinks=this.container.querySelectorAll('a[href^="#"]'),this.uri=window.location.pathname,this.exclude=n,this.internalLinks&&this._internal(),this.externalLinks&&this._external(),this.anchorLinks&&this._anchor()}var t,n,o;return t=e,(n=[{key:"_internal",value:function(){var e=this;this.internalLinks.forEach((function(t,n){if(!t.classList.toString().split(/\s/).some((function(t){return e.exclude.includes(t)}))){var i=t.getAttribute("href").split("?")[0];e.uri===i?(t.classList.add("active"),t.nextElementSibling.style.display="block"):"/"===e.uri&&0===n&&t.classList.add("active")}}))}},{key:"_external",value:function(){this.externalLinks.forEach((function(e){e.setAttribute("targer","_blank")}))}},{key:"_anchor",value:function(){this.anchorLinks.forEach((function(e){var t=e.getAttribute("href");e.addEventListener("click",(function(e){e.preventDefault(),"#"!==t&&document.querySelector(t)&&i("body, html").animate({scrollTop:i(t).offset().top},250)}))}))}}])&&a(t.prototype,n),o&&a(t,o),Object.defineProperty(t,"prototype",{writable:!1}),e}();n(755)((function(){new o(".sidebar")}))},468:()=>{}},e=>{var t=t=>e(e.s=t);e.O(0,[902,162],(()=>(t(909),t(468))));e.O()}]);