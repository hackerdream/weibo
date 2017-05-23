import Vue from 'vue'
import VueRouter from 'vue-router'
import UWeibo from './components/weibo/UWeibo.vue'
import WContent from './components/weibo/UContent.vue'
import axios from 'axios'
//Vue.config.debug = true;

Vue.use(VueRouter);

Vue.prototype.$axios = axios;

const routes = [
    {path: '/', component: WContent}
];

const router = new VueRouter({
    routes,
    hashbang: false,
    history: true
});

new Vue({
    router,
    render: h=>h(UWeibo)
}).$mount('#app');
