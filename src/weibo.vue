<template>

    <div id="weibo">
        <w-nav class="nav"  @show-login="showLoginBox"></w-nav>
        <section class="main">
            <w-content class="content"></w-content>
            <login class="login"></login>
        </section>
        <footer>
            <p class="company">
                <span>Copyright © 2017 weibo 信安三班某组</span>
            </p>
        </footer>

        <div class="layer">
            <div style="position: fixed; top: 0; left: 0; width: 100%; height:100%; background: rgb(0, 0, 0); opacity: 0.3; z-index: 100;"></div>
            <login-layer class="login-layer" @close-layer="close"></login-layer>
        </div>
    </div>
</template>

<script>
    import WNav from './components/nav.vue'
    import WContent from './components/content.vue'
    import Login from './components/login.vue'
    import LoginLayer from './components/loginLayer.vue'

    export default {
        components: {
            WNav, WContent, Login, LoginLayer
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
        background-color: #d4d5e0;
        background-image: url("../public/imgs/body_bg.jpg");
        background-repeat: repeat-x;
        background-position: center 0;
    }

    .main {
        width: 1000px;
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

    .content {
        display: inline-block;
        position: relative;
        vertical-align: top;
        margin: 0 auto;
        z-index: 1;
    }

    .login {
        margin-left: 20px;
        display: inline-block;
        position: relative;
        width: 240px;
        padding: 0 16px;
        z-index: 10;
        border: 1px solid #ccc;

    }

    @media screen  and (max-width: 1000px) {
        .login {
            display: none;
        }
    }

    .company {
        display: block;
        width: 300px;
        margin: 20px auto;
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
