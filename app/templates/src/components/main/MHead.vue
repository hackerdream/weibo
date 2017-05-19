<template>
    <div class="head">
        <div class="head-box">
            <div class="head-position">
                <div class="head-img">
                    <img src="../../../../static/public/imgs/mt4.jpg" width="100" height="100"
                         style="border-radius:50%;">
                </div>
                <p style="margin-top:10px;font-size:18px;">最帅的人</p>
                <p style="margin-top:10px;font-size:12px;">我只因为你而嫣然一笑</p>
                <div style="    margin-top: 15px;text-align: center;">
                    <div style="display: inline-block;">
                        <router-link to="#"
                                     style="display: inline-block;height: 34px;line-height: 35px;padding: 0 15px;font-size: 14px;"
                                     class="head-follow">
                            <div v-show="!isFriend">
                                <em class="fa fa-check" aria-hidden="false"></em>
                                <em>关注</em>
                            </div>
                            <div v-show="isFriend">
                                <em style="font-size:18px;">+</em>
                                <em>未关注</em>
                            </div>
                        </router-link>
                    </div>
                </div>
                <div class="content-nav">
                    <router-link to="/">
                        <span>主页</span>
                    </router-link>
                </div>
            </div>
        </div>


        <router-view></router-view>
    </div>
</template>
<style scoped>
    a {
        text-decoration: none;

    }

    .head-box {
        position: relative;
        width: 1000px;
        height: 360px;
        margin: 20px auto;
    }

    .head-position {
        position: absolute;
        width: 100%;
        height: 360px;
        overflow: hidden;
        z-index: 2;
        text-align: center;
    }

    .head-img {
        position: relative;
        width: 100px;
        height: 100px;
        margin: 48px auto 0;
        padding: 4px;
        background: #fff;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
    }

    .head-follow {
        background: #696e78;
        color: #fff;
    }

    .head-follow em {
        font-style: normal;
    }

    .content-nav {
        width: 100%;
        text-align: center;
        margin-top: 10px;
        background-color: #261d3b;
        height: 40px;
        line-height: 40px;
    }

    .content-nav a {
        color: #fff;
    }

    .content-nav a:hover {
        color: #eb7350;
    }

</style>
<script>
    export default{
        data(){
            return {
                isFriend: true
            }
        }
    }
</script>
