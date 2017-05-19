<template>
    <div>
        <div class="manager">
            <div class="manager-box">
                <div class="manager-list"
                     style="background-color:#261d3b;width:230px;height:300px;float:left; font-size:14px;color:#918ea5;text-align:center;">
                    <ul>
                        <li>
                            <router-link to="/manager/111/follow">关注</router-link>
                        </li>

                        <li>
                            <router-link to="/manager/111/fensi">粉丝</router-link>
                        </li>
                    </ul>
                </div>
                <div class="fensi">
                    <div class="fensi-box">
                        <div class="fensi-name">
                            <span>
                                全部粉丝 ：93
                            </span>
                        </div>
                        <ul class="fensi-list">
                            <li class="fensi-list-box">
                                <div class="list-detail">
                                    <div class="list-face">
                                        <router-link to="">
                                            <img src="../../../../static/public/imgs/mt4.jpg" width="50" height="50">
                                        </router-link>
                                    </div>
                                    <div class="list-info">
                                        <div class="name">
                                            <span>我是大帅比</span>
                                        </div>
                                        <div class="status">互相关注</div>
                                        <div class="summary">
                                            <span>吃饭睡觉打豆豆</span>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            <li class="fensi-list-box">
                                <div class="list-detail">
                                    <div class="list-face">
                                        <router-link to="">
                                            <img src="../../../../static/public/imgs/mt4.jpg" width="50" height="50">
                                        </router-link>
                                    </div>
                                    <div class="list-info">
                                        <div class="name">
                                            <span>我是大帅比</span>
                                        </div>
                                        <div class="status">互相关注</div>
                                        <div class="summary">
                                            <span>吃饭睡觉打豆豆</span>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            <li class="fensi-list-box">
                                <div class="list-detail">
                                    <div class="list-face">
                                        <router-link to="">
                                            <img src="../../../../static/public/imgs/mt4.jpg" width="50" height="50">
                                        </router-link>
                                    </div>
                                    <div class="list-info">
                                        <div class="name">
                                            <span>我是大帅比</span>
                                        </div>
                                        <div class="status">互相关注</div>
                                        <div class="summary">
                                            <span>吃饭睡觉打豆豆</span>
                                        </div>
                                    </div>
                                </div>
                            </li>
                            <li class="fensi-list-box">
                                <div class="list-detail">
                                    <div class="list-face">
                                        <router-link to="">
                                            <img src="../../../../static/public/imgs/mt4.jpg" width="50" height="50">
                                        </router-link>
                                    </div>
                                    <div class="list-info">
                                        <div class="name">
                                            <span>我是大帅比</span>
                                        </div>
                                        <div class="status">互相关注</div>
                                        <div class="summary">
                                            <span>吃饭睡觉打豆豆</span>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
<style scoped>
    ul li {
        list-style: none;
    }

    a {
        cursor: pointer;
        text-decoration: none;
    }

    .manager {
        width: 1000px;
        height: 200px;
        min-height: 400px;
        overflow: hidden;
        margin: 0 auto;
    }

    .manager-box {
        width: 1000px;
        overflow: hidden;
        margin: 0 auto;
    }

    .manager-list li a {
        display: block;
        color: #918ea5;
        height: 40px;
        line-height: 40px;
    }

    .manager-list li {
        border-bottom: 1px solid #302552;
    }

    .manager-list li a:hover {
        color: #eb7350;
    }

    .fensi {
        width: 680px;
        height: 300px;
        float: right;
        background-color: #261d3b
    }

    .fensi-box {
        display: block;
        width: 680px;
        min-height: 420px;
    }

    .fensi-name {
        display: block;
        width: 200px;
        height: 30px;
        margin: 10px 10px;
        color: #918ea5;
        font-size: 14px;

    }

    .fensi-list {
        border-top: 1px solid #3e355b;
        display: block;
        width: 100%;
        padding-top: 20px;
    }

    .fensi-list-box {
        display: inline-block;
        width: 330px;
        height: 106px;
        margin: 6px 0 0 6px;
        background-color: #1d1531;
    }

    .list-detail {
        width: 308px;
        height: 84px;
        padding: 16px 0 16px 16px;
    }

    .list-face {
        position: relative;
        float: left;
        width: 72px;
        height: 84px;
        border-right: 1px solid #3e355b;
    }

    .list-face a {
        display: block;
        width: 60px;
        height: 60px;
        margin-top: 6px;
    }

    .list-face a img {
        border-radius: 50%;
    }

    .list-info {
        margin-left: 90px;
    }

    .name {
        display: block;
        margin-top: -4px;
        height: 24px;
        font-size: 18px;
        color: #918ea5;
    }

    .status {
        display: block;
        font-size: 13px;
        height: 30px;
        line-height: 30px;
        color: #918ea5;
    }

    .summary {
        display: block;
        font-size: 12px;
        height: 40px;
        line-height: 40px;
        color: #5b577c;
    }
</style>
<script>
    export default{}
</script>
