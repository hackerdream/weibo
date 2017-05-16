import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from './Main.vue'

//Vue.config.debug = true;

Vue.use(VueRouter);


new Vue({
  render: h => h(Main)
}).$mount('#main');
