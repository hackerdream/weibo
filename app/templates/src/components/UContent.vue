<template>

    <div class="w-content">
        <div class="content">
            <div class="current-news">
                <ul>
                    <router-link to="/home/1111" :class="[{morePicture:true,onePicture:false}]" class="current-new">
                        <div class="pic-tex">
                            <div class="tex-box">
                                <div class="text">
                                    这里是内容你信吗，反正我信了今天是我們倆結婚五週年的日子，老公一早就跟我說了一聲Happy anniversary，
                                    原本以為今年就在月子中心簡單的過，就像過去的每一天一樣，沒想到你們解孵特地去買了我好久沒吃的杯子蛋糕和
                                    花給我驚喜而且今年的花多了一種-康乃馨️真的很特別，謝謝老公那麽有心，總是花心思給我驚喜️愛你，五週年快樂
                                </div>
                            </div>
                            <div class="pic-box">
                                <img src="../../public/imgs/mt1.jpg">
                                <img src="../../public/imgs/mt2.jpg">
                                <img src="../../public/imgs/mt3.jpg">
                            </div>
                            <div class="sub-info-box">
                                <a src="#">
                                    <span class="info-face">
                                        <img src="../../public/imgs/infoFace.jpg" width="20" height="20">
                                    </span>
                                    <span style="font-size: 14px;float: left;line-height: 24px">
                                        @师生情
                                    </span>
                                    <span class="info-time">
                                        4月5日 23:23:10
                                    </span>
                                    <span class="info-com">
                                        <i class="fa fa-commenting-o" aria-hidden="true"></i>
                                        <em>20</em>
                                    </span>
                                    <span class="right-line"></span>
                                    <span class="info-upvote">
                                        <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                                        <em>30</em>
                                    </span>
                                </a>
                            </div>
                        </div>
                    </router-link>
                    <li class="current-new" :class="[{morePicture:false,onePicture:true}]">
                        <div class="pic-tex">
                            <div class="tex-box">
                                <div class="text">
                                    这里是内容你信吗，反正我信了今天是我們倆結婚五週年的日子，老公一早就跟我說了一聲Happy anniversary，
                                    原本以為今年就在月子中心簡單的過，就像過去的每一天一樣，沒想到你們解孵特地去買了我好久沒吃的杯子蛋糕和
                                    花給我驚喜而且今年的花多了一種-康乃馨️真的很特別，謝謝老公那麽有心，總是花心思給我驚喜️愛你，五週年快樂
                                </div>
                            </div>
                            <div class="pic-box">
                                <img src="../../public/imgs/mt1.jpg">
                            </div>
                            <div class="sub-info-box">
                                <a src="">
                                    <span class="info-face">
                                        <img src="../../public/imgs/infoFace.jpg" width="20" height="20">
                                    </span>
                                </a>
                                <span style="font-size: 14px;float: left;line-height: 24px">
                                        @师生情
                                    </span>
                                <span class="info-time">
                                        4月5日 23:23:10
                                    </span>
                                <span class="info-com">
                                        <i class="fa fa-commenting-o" aria-hidden="true"></i>
                                        <em>20</em>
                                    </span>
                                <span class="right-line"></span>
                                <span class="info-upvote">
                                        <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                                        <em>30</em>
                                    </span>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
            <div class="content-ad">
                <div class="advertisement">
                    <a href="#">
                        <img src="../../public/imgs/advertise.png" width="720" height="200">
                    </a>
                </div>
            </div>
            <div class="hot-news">
                <ul>
                    <li :class="[{morePicture:true,onePicture:false}]" class="current-new">
                        <div class="pic-tex">
                            <div class="tex-box">
                                <div class="text">
                                    这里是内容你信吗，反正我信了今天是我們倆結婚五週年的日子，老公一早就跟我說了一聲Happy anniversary，
                                    原本以為今年就在月子中心簡單的過，就像過去的每一天一樣，沒想到你們解孵特地去買了我好久沒吃的杯子蛋糕和
                                    花給我驚喜而且今年的花多了一種-康乃馨️真的很特別，謝謝老公那麽有心，總是花心思給我驚喜️愛你，五週年快樂
                                </div>
                            </div>
                            <div class="pic-box">
                                <img src="../../public/imgs/mt1.jpg">
                                <img src="../../public/imgs/mt2.jpg">
                                <img src="../../public/imgs/mt3.jpg">
                            </div>
                            <div class="sub-info-box">
                                <a src="">
                                    <span class="info-face">
                                        <img src="../../public/imgs/infoFace.jpg" width="20" height="20">
                                    </span>
                                    <span style="font-size: 14px;float: left;line-height: 24px">
                                        @师生情
                                    </span>
                                    <span class="info-time">
                                        4月5日 23:23:10
                                    </span>
                                    <span class="info-com">
                                        <i class="fa fa-commenting-o" aria-hidden="true"></i>
                                        <em>23231</em>
                                    </span>
                                    <span class="right-line"></span>
                                    <span class="info-upvote">
                                        <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                                        <em>42313</em>
                                    </span>
                                </a>
                            </div>
                        </div>
                    </li>
                    <li class="current-new" :class="[{morePicture:false,onePicture:true}]">
                        <div class="pic-tex">
                            <div class="tex-box">
                                <div class="text">
                                    这里是内容你信吗，反正我信了今天是我們倆結婚五週年的日子，老公一早就跟我說了一聲Happy anniversary，
                                    原本以為今年就在月子中心簡單的過，就像過去的每一天一樣，沒想到你們解孵特地去買了我好久沒吃的杯子蛋糕和
                                    花給我驚喜而且今年的花多了一種-康乃馨️真的很特別，謝謝老公那麽有心，總是花心思給我驚喜️愛你，五週年快樂
                                </div>
                            </div>
                            <div class="pic-box">
                                <img src="../../public/imgs/mt1.jpg">
                            </div>
                            <div class="sub-info-box">
                                <a src="">
                                    <span class="info-face">
                                        <img src="../../public/imgs/infoFace.jpg" width="20" height="20">
                                    </span>
                                </a>
                                <span style="font-size: 14px;float: left;line-height: 24px">
                                        @师生情
                                    </span>
                                <span class="info-time">
                                        4月5日 23:23:10
                                    </span>
                                <span class="info-com">
                                        <i class="fa fa-commenting-o" aria-hidden="true"></i>
                                        <em>12415</em>
                                    </span>
                                <span class="right-line"></span>
                                <span class="info-upvote">
                                        <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                                        <em>20000</em>
                                    </span>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>

        <div class="W-person-info">
            <div class="W-person-info-face">
                <img src="../../public/imgs/mt4.jpg" width="50" height="50" alt="我是帅比"
                     class="person-info-face">
            </div>
            <div class="person-info-box">
                <div class="person-info-name">
                    <span>最帅的人</span>
                </div>
                <ul class="user-atten">
                    <li>
                        <router-link to="#">
                            <strong>82</strong>
                            <span>关注</span>
                        </router-link>
                    </li>
                    <li>
                        <router-link to="#">
                            <strong>72</strong>
                            <span>粉丝</span>
                        </router-link>
                    </li>
                    <li>
                        <router-link to="">
                            <strong>5</strong>
                            <span>微博</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </div>
        <footer>
            <p class="company">
                <span>Copyright © 2017 weibo 信安三班某组</span>
            </p>
        </footer>

        <router-view></router-view>
    </div>

</template>
<style scoped>
    ul li {
        display: block;
        list-style: none;
        cursor: pointer;
    }

    .text {
        color: black;
    }

    a {
        cursor: pointer;
        text-decoration: none;
    }

    .w-content {
        width: 990px;
        margin: 0 auto;
        overflow: hidden;

    }

    @media screen and (max-width: 1000px) {
        .w-content {
            width: 722px;
            margin: 0 auto;
            overflow: hidden;
        }

        .w-content .w-login {
            display: none;
        }
    }

    .content {
        display: inline-block;
        position: relative;
        vertical-align: top;
        margin: 0 auto;
        z-index: 1;
    }

    .content {
        width: 722px;
        overflow: hidden;
    }

    .current-news {
        display: block;
        width: 720px;
        position: relative;
    }

    .pic-tex {
        overflow: hidden;
    }

    .morePicture {
        display: block;
        width: 680px;
        margin: 0 auto;
        padding: 20px 20px;
        height: 240px;
        border: 1px solid #ccc;
        background: #ffffff;
    }

    .onePicture {
        display: block;
        width: 680px;
        margin: 0 auto;
        padding: 20px 20px;
        height: 120px;
        border: 1px solid #ccc;
        background: #ffffff;
        overflow: hidden;
    }

    .current-new + .current-new {
        margin-top: 16px;
    }

    .morePicture .tex-box {
        position: relative;
        overflow: hidden;
    }

    .onePicture .tex-box {
        position: relative;
        float: right;
        width: 500px;
        margin-top: 20px;
        overflow: hidden;
    }

    .morePicture .pic-box {
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .onePicture .pic-box {
        display: inline-block;
        overflow: hidden;
        width: 160px;
    }

    .morePicture .text {
        line-height: 23px;
        max-height: 46px;
        _height: 46px;
        font-size: 14px;
        overflow: hidden;
    }

    .onePicture .text {
        line-height: 23px;
        max-height: 46px;
        _height: 46px;
        font-size: 14px;
        overflow: hidden;
    }

    .morePicture .pic-box img {
        display: inline;
        width: 220px;
        height: 130px;
    }

    .onePicture .pic-box img {
        display: block;
        float: right;
        width: 160px;
        height: 108px;
    }

    .morePicture .sub-info-box {
        display: block;
        height: 24px;
        width: 100%;
        font-size: 14px;
    }

    .onePicture .sub-info-box {
        display: inline-block;
        height: 24px;
        width: 500px;
        font-size: 14px;
        float: right;
        margin-top: -40px;
        overflow: hidden;
    }

    .sub-info-box span {
        color: #918ea5;
    }

    .info-face {
        float: left;
        height: 24px;
        margin-right: 5px;
    }

    .info-face img {
        -webkit-border-radius: 10px;
        -moz-border-radius: 10px;
        border-radius: 10px;
    }

    .info-time {
        float: left;
        margin-left: 10px;
        font-size: 14px;
        line-height: 24px;
    }

    .info-com {
        float: right;
        margin-right: 10px;
        line-height: 24px;
    }

    .info-com:hover {
        cursor: pointer;
        color: #eb7350;
    }

    .right-line {
        width: 0;
        height: 10px;
        border-right: 1px solid #ccc;
        margin-top: 7px;
        float: right;
        margin-right: 5px;
    }

    .info-upvote {
        float: right;
        margin-right: 10px;
        line-height: 24px;
    }

    .info-upvote:hover {
        cursor: pointer;
        color: #eb7350;
    }

    .content-ad {
        display: block;
        position: relative;
        width: 720px;
        border: 1px solid #ccc;
        background: #fff;
    }

    .advertisement {
        display: block;
        width: 100%;
        height: 160px;
        margin: 0 auto;
        overflow: hidden;
    }

    .hot-news {
        display: block;
        width: 720px;
        position: relative;
    }

    .current-news + .content-ad, .content-ad + .hot-news {
        margin-top: 16px;
    }

    .w-login {
        width: 224px;
        display: inline-block;
    }

    .login {
        margin-left: 20px;
        position: relative;
        width: 240px;
        padding: 0 16px;
        z-index: 10;
        border: 1px solid #ccc;

    }

    .login h1 {
        padding: 10px 0;
        width: 50%;
        font-size: 16px;
        text-align: center;
        border-bottom: 1px solid #eb7350;
    }

    .login {
        width: 208px;
        font-size: 10px;
        background-color: #ffffff;
        overflow: hidden;
        color: #808080;
    }

    .login-box {
        margin: 0 auto;
        display: block;
        width: 100%;
        text-decoration: none;
    }

    .login-box input {
        width: 186px;
        height: 26px;
        margin-top: 20px;
        padding: 5px 10px;
        line-height: 30px;
        border: 1px solid #ccc;
        font-size: 10px;
        border-radius: 4px;
        outline-style: none;
    }

    input:focus {
        border-color: #eb7350 !important;
    }

    .login-memory {
        display: block;
        width: 50%;
        float: left;
        height: 40px;
        line-height: 40px;
    }

    .refoundPsd {
        display: block;
        width: 50%;
        float: right;
        height: 40px;
        line-height: 40px;
        text-align: right;
    }

    .refoundPsd a {
        text-decoration: none;
    }

    .refoundPsd:hover {
        cursor: pointer;
    }

    .clearFLoat {
        clear: both;
    }

    .login-weibo {
        display: block;
        width: 206px;
        height: 32px;
        line-height: 30px;
        background: #ff8140;
        border: 1px solid #f77c3d;
        border-radius: 4px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.25);
        white-space: nowrap;
        text-align: center;
        color: #ffffff;
        font-size: 16px;
        outline: none;
        text-decoration: none;
        margin-bottom: 40px;
    }

    .login-weibo:hover {
        cursor: pointer;
    }

    .company {
        display: block;
        width: 300px;
        margin: 20px auto;
    }

    .W-person-info {
        display: block;
        position: relative;
        float: right;
        width: 260px;
        height: 190px;
        overflow: hidden;
        text-align: center;
        border-right: 1px solid #3e355b;
        box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
        border-radius: 2px;
        background-color: #261d3b;
    }

    .user-atten {
        display: block;
        width: 228px;
        height: 35px;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .user-atten li {
        float: left;
        width: 75px;
        border-right: 1px solid #918ea5;
    }

    .user ul {
        height: 34px;
        overflow: hidden;
        margin: 10px 0 0 0;
        font-size: 18px;
    }

    .user-atten li:last-child {
        border: 0;
    }

    .user-atten li span, .user-atten li strong {
        display: block;
        text-align: center;
        color: #918ea5;
        font-size: 13px;
    }

    .W-person-info-face {
        display: block;
        width: 100%;
        height: 75px;
        background-image: url(../../public/imgs/profile_cover_s.jpg)
    }

    .person-info-face {
        border-radius: 50%;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -45px;
        margin-left: -25px;
    }

    .person-info-box {
        display: block;
        width: 228px;
        height: 70px;
        padding: 30px 16px
    }

    .person-info-name {
        display: block;
        text-align: center;
        color: #918ea5;
    }
</style>
<script>
    export default{
        data(){
            return {
                moreThreePicture: true,
                lessThreePicture: false
            }
        }
    }
</script>