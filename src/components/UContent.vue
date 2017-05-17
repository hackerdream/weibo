<template>

    <div class="w-content">

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