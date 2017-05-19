import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './components/index/weibo.vue'
import WContent from './components/index/WContent.vue'
import WArticle from './components/index/WArticle.vue'


//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
  {path: '/',component:Weibo},
  {path: '/home', component:WContent},
  {path: '/home/111', component: WArticle},
];

const router = new VueRouter({
  routes
});

new Vue({
  router,
  components:{
    Weibo,WContent
  }
}).$mount('#app');
