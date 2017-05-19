<template>
    <div id="app">
        <div>
            <m-nav class="nav" :isLogin=true></m-nav>
        </div>
        <div class="">
            <m-head></m-head>
        </div>
        <div>
            <m-content></m-content>
        </div>
    </div>
</template>
<style scoped>
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
<script>
    import MNav from '../Nav.vue'
    import MContent from '../main/MContent.vue'
    import MHead from '../main/MHead.vue'

    export default{
        components: {
            MContent, MNav,MHead
        }
    }
</script>
