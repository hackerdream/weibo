import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './weibo.vue'
import Content from './components/Content.vue'
import Article from './components/Article.vue'

//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
  {path: '/', component: Content},
  {path: '/home', component: Content},
  {path: '/home/1111', component: Article}
];

const router = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(Weibo)
});
