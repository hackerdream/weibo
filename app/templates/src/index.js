import Vue from 'vue'
import VueRouter from 'vue-router'
import Weibo from './components/index/weibo.vue'
import WContent from './components/index/WContent.vue'
import WArticle from './components/index/WArticle.vue'
import axios from 'axios'

//Vue.config.debug = true;

Vue.use(VueRouter);
Vue.prototype.$axios = axios;


const routes = [
    {path: '/', component: WContent},
    {path: '/home/:id', component: WArticle}
];

const router = new VueRouter({
    routes
});

new Vue({
    router,
    render: h=>h(Weibo)
}).$mount('#app');
