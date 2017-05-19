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
                    <div class="user-manager">
                        <a class="user-manager-box" @mouseenter="showItem()"
                           @mouseleave="hideItem()">
                            <em class="fa fa-cog" aria-hidden="true"></em>
                            <em>管理</em>
                        </a>
                        <div class="gn-topmenulist">
                            <!--data start-->
                            <ul>
                                <li>
                                    <router-link to="/manager/111">帐号设置</router-link>
                                </li>
                                <li>
                                    <a>退出</a>
                                </li>
                            </ul>
                            <div class="W_layer_arrow">
                                <span class="W_arrow_bor W_arrow_bor_t">
                                    <i class="S_line3"></i>
                                    <em class="S_bg2_br"></em>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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

    ul li {
        list-style: none;
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
            background-image: url(../../../../static/public/imgs/WB_logo-x2.png);
            background-size: 60px 20px;
        }
    }

    .logo-box .logo-bg {
        display: block;
        width: 80px;
        height: 48px;
        cursor: pointer;
        background: url(../../../../static/public/imgs/WB_logo-x2.png) no-repeat 0 40%;
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

    }

    .nav-guild .nav-content {
        display: block;
        width: 200px;
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

    .nav-login a {
        display: block;
        position: relative;
        width: 240px;
        height: 40px;
        line-height: 40px;
    }

    .nav-content a:hover {
        cursor: pointer;
    }

    .nav-login a:first-child {
        display: inline-block;
        width: 90px;
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

    .user-manager {
        display: inline-block;
        width: 100px;
        height: 30px
    }

    .nav .user-manager a {
        padding: 0 4px;
    }

    .gn-topmenulist {
        position: absolute;
        display: none;
        background: #fff;
        width: 84px;
        top: 60px;
        color: #333;
        border: 1px solid #ccc;
        border-radius: 2px;
        padding: 2px;
        box-shadow: 0px 2px 8px 1px rgba(0, 0, 0, 0.2);
        z-index: 10;
    }

    .nav .user-manager .nav-login .gn_topmenulist ul li {
        position: static;
        width: 64px;
        float: none;
        margin: 0;
        padding: 0;
        display: inline;
        border-bottom: 1px solid #ccc;
    }

    .W_arrow_bor {
        display: block;
        position: relative;
    }

    .W_arrow_bor_t i, .W_arrow_bor_t em {
        _border-style: dashed dashed solid dashed;
        border-top-color: transparent;
        border-right-color: transparent;
        border-left-color: transparent;
    }

    .S_line3 {
        border-color: #ccc;
        position: absolute;
        top: -99px;
        right: 35px;
    }

    .S_bg2_br {
        position: absolute;
        top: -97px;
        right: 35px;
        color: #fff;
        border-color: #fff;
    }

    .W_arrow_bor i, .W_arrow_bor em {
        display: inline-block;
        width: 0;
        height: 0;
        border-width: 7px;
        border-style: solid;
        overflow: hidden;
        font-size: 0;
        line-height: 0;
        vertical-align: top;
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
            },
            showItem() {
                document.getElementsByClassName('gn-topmenulist')[0].style.display = "block";
            },
            hideItem() {
                setTimeout("document.getElementsByClassName('gn-topmenulist')[0].style.display = \"none\";", 1200);
            }
        }
    }
</script>