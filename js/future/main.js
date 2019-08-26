

import Vue from 'https://cdn.jsdelivr.net/npm/vue/dist/vue.js?module';
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
