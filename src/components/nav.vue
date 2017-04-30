<template>

    <div class="nav">
        <div class="nav-head left">
            <div class="logo left">
                <a href="/" class="logo-box">
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
                            <i class="fa fa-home fa-2x left"></i>
                            <a class="left">首页</a>
                        </li>
                    </ul>
                </div>
                <div class="nav-login left">
                    <a href="#" class="left">登录</a>
                    <div class="block left">|</div>
                    <a href="#" class="left">注册</a>
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
            background-image: url(../../public/imgs/WB_logo-x2.png);
            background-size: 60px 20px;
        }
    }

    .logo-box .logo-bg {
        display: block;
        width: 80px;
        height: 48px;
        cursor: pointer;
        background: url(../../public/imgs/WB_logo-x2.png) no-repeat 0 40%;
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
            width: 150px;
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
        margin-left: -10px;
        padding: 10px;

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
    }

    .nav-content a:hover {
        cursor: pointer;
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
    export default{}
</script>