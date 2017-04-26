import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './weibo.vue'

//Vue.config.debug = true;
Vue.use(VueRouter);

new Vue({
  el: '#app',
  render: h => h(Weibo)
});
