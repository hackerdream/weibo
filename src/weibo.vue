<template>

    <div id="weibo">

        <w-nav class="nav" @show-login="showLoginBox"></w-nav>

        <div class="layer">
            <div style="position: fixed; top: 0; left: 0; width: 100%; height:100%; background: rgb(0, 0, 0); opacity: 0.3; z-index: 100;"></div>
            <login-layer class="login-layer" @close-layer="close"></login-layer>
        </div>

        <router-view></router-view>

    </div>
</template>

<script>
    import WNav from './components/Nav.vue'
    import WContent from './components/Content.vue'
    import LoginLayer from './components/LoginLayer.vue'

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

    #weibo {
        padding-top: 60px;
        overflow: hidden;
        background: url(../public/imgs/body_bg2.jpg) no-repeat top center;
        background-color: #1d0e2b;
    }

    .main {
        width: 990px;
        margin: 0 auto;
        overflow: hidden;
    }

    @media screen and (max-width: 1000px) {
        .main {
            width: 722px;
            margin: 0 auto;
            overflow: hidden;
        }
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

    @media screen  and (max-width: 1000px) {
        .login {
            display: none;
        }
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
