<template>

    <div id="app">

        <u-nav class="nav" :isLogin=true></u-nav>

    <router-view></router-view>
    </div>
</template>

<script>
    import UNav from './UNav.vue'
    import UContent from './UContent.vue'

    export default {
        components: {
            UNav, UContent
        },
        methods: {
            close(){
                document.getElementsByClassName('layer')[0].style.display = "none";
            },
            showLoginBox(){
                document.getElementsByClassName('layer')[0].style.display = "block"
            }
        }
    }
</script>

<style lang="scss" scoped>
    * {
        margin: 0;
        padding: 0;
    }

    #app {
        padding-top: 60px;
        overflow: hidden;
        background: url(../../../../static/public/imgs/body_bg2.jpg) no-repeat top center;
        background-color: #1d0e2b;
    }

    .nav {
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        border-bottom: 1px solid #cacaca;
        z-index: 99;
        background-color: #ffffff;
        overflow: hidden;
    }

</style>
