import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './components/index/weibo.vue'
import WContent from './components/index/WContent.vue'
import WArticle from './components/index/WArticle.vue'
import UWeibo from './components/weibo/UWeibo.vue'
import MWeibo from './components/main/MWeibo.vue'

//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
  {path: '/home', component:WContent},
  {path: '/home/1111', component: WArticle}
];

const router = new VueRouter({
  routes
});

new Vue({
  router,
  components:{
    Weibo,WContent,UWeibo,MWeibo
  }
}).$mount('#app');
