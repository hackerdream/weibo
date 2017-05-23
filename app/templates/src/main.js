import Vue from 'vue'
import VueRouter from 'vue-router'
import MWeibo from './components/main/MWeibo.vue'
import MContent from './components/main/MContent.vue'
import Follow from './components/main/Follow.vue'
import Fensi from './components/main/Fensi.vue'
import Manage from './components/main/Manager.vue'
import axios from 'axios'
//Vue.config.debug = true;

Vue.use(VueRouter);
Vue.prototype.$axios = axios;

const routes = [
    {path: '/', component: MContent},
    {path: '/home',component:MContent},
    {path: '/manager/：id/follow', component: Follow},
    {path: '/manager/:id/fensi', component: Fensi},
    {path: '/manager/:id',component:Manage}

];

const router = new VueRouter({
    routes
});

new Vue({
    router,
    render: h => h(MWeibo)
}).$mount('#app');
