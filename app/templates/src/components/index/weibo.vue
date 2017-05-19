<template>

    <div id="app">

        <w-nav class="nav" @show-login="showLoginBox"></w-nav>

        <div class="content">
            <w-content></w-content>
        </div>

        <div class="layer">
            <div style="position: fixed; top: 0; left: 0; width: 100%; height:100%; background: rgb(0, 0, 0); opacity: 0.3; z-index: 100;"></div>
            <login-layer class="login-layer" @close-layer="close"></login-layer>
        </div>

    </div>
</template>

<script>
    import WNav from '../weibo/WNav.vue'
    import WContent from './WContent.vue'
    import LoginLayer from './LoginLayer.vue'

    export default {
        components: {
            WNav, WContent, LoginLayer
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

    .layer {
        display: none;

    }

    .login-layer {
        display: block;
        position: absolute;
        width: 600px;
        height: 400px;
        top: 50%;
        left: 50%;
        margin-left: -300px;
        margin-top: -200px;
        z-index: 999;
        background: #ffffff;
    }
</style>
