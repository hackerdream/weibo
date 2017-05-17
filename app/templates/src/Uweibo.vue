<template>
    <div id="weibo">
        <w-nav class="nav" ></w-nav>


        <router-view></router-view>

    </div>
</template>
<style>
    * {
        margin: 0;
        padding: 0;
    }

    #weibo {
        padding-top: 60px;
        overflow: hidden;
        background: url(../../../app/static/public/imgs/body_bg2.jpg) no-repeat top center;
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

</style>
<script>
    import WNav from './components/Unav.vue'
    export default{
        components: {
            WNav
        },
    }
</script>