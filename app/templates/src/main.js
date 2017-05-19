import Vue from 'vue'
import VueRouter from 'vue-router'
import MWeibo from './components/main/MWeibo.vue'
import MContent from './components/main/MContent.vue'
import Follow from './components/main/Follow.vue'
import Fensi from './components/main/Fensi.vue'
//Vue.config.debug = true;

Vue.use(VueRouter);

const routes = [
    {path: '/', component: MContent},
    {path: '/manager/111/follow', component: Follow},
    {path: '/manager/111/fensi', component: Fensi}

];

const router = new VueRouter({
    routes
});

new Vue({
    router,
    render: h => h(MWeibo)
}).$mount('#app');
