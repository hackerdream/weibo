import Vue from 'vue'
import VueRouter from 'vue-router'
import UWeibo from './Uweibo.vue'
import UContent from './components/UContent.vue'

//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
  {path: '/', component: UContent},
  {path: '/home', component: UContent},
]

const router = new VueRouter({
  routes
});

new Vue({
  router,
  render: h => h(UWeibo)
}).$mount('#weibo');
