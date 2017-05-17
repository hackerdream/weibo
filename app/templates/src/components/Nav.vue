<template>

    <div class="nav">
        <div class="nav-head left">
            <div class="logo left">
                <a href="#" class="logo-box">
                    <span class="logo-bg"></span>
                </a>
            </div>
            <div class="nav-search left">
                <input type="text" placeholder="大家都在搜">
                <a href="#" class="search"><i class="fa fa-search" aria-hidden="true"></i></a>
            </div>
            <div class="nav-guild right">
                <div class="nav-content left">
                    <ul>
                        <li>
                            <router-link to="/home" class="left">
                                <em class="fa fa-home fa-2x left"></em>
                                <em>首页</em>
                            </router-link>
                        </li>
                    </ul>
                </div>

                <div class="nav-login left" v-if="!isLogin">
                    <a href="#" class="left" @click="showLogin">登录</a>
                    <div class="block left">|</div>
                    <a class="left" href="/register">注册</a>
                </div>


                <div class="nav-login left" v-if="isLogin">
                    <router-link to="#">
                        <em class="fa fa-user-o" aria-hidden="true"></em>
                        <em>我是帅哥</em>
                    </router-link>
                </div>
            </div>
        </div>
        <router-view></router-view>

    </div>

</template>
<style scoped>
    a {
        display: block;
        text-decoration: none;
        color: #696e78;
    }

    em {
        font-style: normal
    }

    .left {
        float: left;
    }

    .right {
        float: right;
    }

    .nav .nav-head {
        display: block;
        position: relative;
        width: 90%;
        padding: 0 40px;
        margin: 0 auto;
    }

    .nav-content a:hover {
        color: #eb7350;
    }

    .nav-login a:hover {
        color: #eb7350;
    }

    @media screen and (max-width: 1050px) {
        .nav .nav-head {
            width: 800px;
        }
    }

    .logo {
        display: block;
        width: 80px;
        height: 50px;
        padding: 6px 0;

    }

    @media only screen and (-webkit-min-device-pixel-ratio: 2), not all, not all, not all {
        .logo-box .logo-bg {
            background-image: url(../../../static/public/imgs/WB_logo-x2.png);
            background-size: 60px 20px;
        }
    }

    .logo-box .logo-bg {
        display: block;
        width: 80px;
        height: 48px;
        cursor: pointer;
        background: url(../../../static/public/imgs/WB_logo-x2.png) no-repeat 0 40%;
        background-size: 80px 30px;
    }

    .nav .nav-search {
        display: block;
        position: relative;
        padding: 10px;
    }

    .nav-search input {
        display: block;
        padding: 5px 15px;
        width: 258px;
        height: 26px;
        border: 1px solid #ccc;
        border-radius: 20px;
        outline-style: none;
    }

    @media screen and (max-width: 1050px) {
        .nav .nav-search input {
            display: block;
            padding: 5px 15px;
            width: 150px;
            height: 26px;
            border: 1px solid #ccc;
            border-radius: 20px;
            outline-style: none;
        }
    }

    .search {
        display: block;
        position: absolute;
        color: #696e78;
        top: 18px;
        right: 10px;
        float: left;
        width: 30px;
        height: 26px;
    }

    .search:hover {
        cursor: pointer;
    }

    .nav-guild {
        margin-right: 10px;
        padding: 10px;
        overflow: hidden;

    }

    .nav-guild .nav-content {
        display: block;
        width: 320px;
        height: 40px;
        line-height: 40px;
        color: #696e78;
    }

    .nav-guild .nav-content ul {
        list-style: none;
    }

    .nav-guild .nav-content i {
        line-height: 40px;
    }

    .nav-guild .nav-content a {
        height: 40px;
        line-height: 40px;
    }

    .nav-guild .nav-login {
        display: block;
        position: relative;
        height: 40px;
        line-height: 40px;
        overflow: hidden;
    }

    .nav-content a:hover {
        cursor: pointer;
        overflow: hidden;
    }

    .nav-login a {
        padding: 0 10px;
    }

    .nav-login a:hover {
        cursor: pointer;
    }

    .nav-login .block {
        display: block;
        position: relative;
        width: 1px;
        height: 30px;
        line-height: 40px;
    }


</style>
<script>
    export default{
        props: {
            isLogin: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            showLogin(){
                this.$emit('show-login')
            }
        }
    }
</script>