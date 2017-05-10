import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './weibo.vue'
import Content from './components/Content.vue'

//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
  {path:'/main',component:Content}
];

const router  = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(Weibo)
});
