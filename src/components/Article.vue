<!--suppress ALL -->
<template>
    <div>
        <div class="article">
            <div class="article-item">
                <div class="article-detail">
                    <router-link to="#" class="article-detail-img">
                        <img src="../../public/imgs/infoFace.jpg" width="50" height="50">
                    </router-link>
                    <div class="article-detail-info">
                        <div class="wb-info">
                            <router-link to="#" class="wb-info-name">中国知青青年</router-link>
                            <a class="wb-mark">
                                <em class="fa fa-plus" aria-hidden="true"></em>
                                <span>加关注</span>
                            </a>
                        </div>
                        <div class="wb-time">
                            5月11日 07:10 来自 iPhone 6s Plus
                        </div>
                        <div class="wb-text">
                            【历史是有痕迹的】上一代的恩怨，后辈们吸取教训，不作恶，是做人的最基本底线。认错的认错，放下的放下吧，就是给自己一个舒服的现在，不是嚒。
                        </div>
                        <div class="wb-img">
                            <ul class="wb-media">
                                <li>
                                    <img src="../../public/imgs/mt1.jpg">
                                </li>
                                <li>
                                    <img src="../../public/imgs/mt2.jpg">
                                </li>
                                <li>
                                    <img src="../../public/imgs/mt3.jpg">
                                </li>
                                <li>
                                    <img src="../../public/imgs/mt4.jpg">
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="article-feed-handle">
                    <ul class="wb-row-line">
                        <li>
                            <a>
                                <span>
                                    <em class="fa fa-star-o" aria-hidden="true"></em>
                                    <em>收藏</em>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a>
                                <span>
                                   <em class="fa fa-external-link" aria-hidden="true"></em>
                                    <em>2324</em>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a>
                                <span>
                                    <em class="fa fa-commenting-o" aria-hidden="true"></em>
                                    <em>2034</em>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a>
                                <span>
                                    <em class="fa fa-thumbs-o-up" aria-hidden="true"></em>
                                    <em>23333</em>
                                </span>
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="article-feed-repeat">
                    <div class="wb-feed-push">
                        <div class="wb-face">
                            <router-link to="">
                                <img src="../../public/imgs/mt4.jpg" width="30" height="30">
                            </router-link>
                        </div>
                        <div class="wb-push">
                            <textarea class="W-input"></textarea>
                            <a>
                                <span>提交</span>
                            </a>
                        </div>
                    </div>
                    <div class="wb-repeat-list">
                        <div class="wb-repeat-top">
                            <span>按时间</span>
                        </div>
                        <div class="repeat">
                            <repeat :face="face">

                            </repeat>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <p class="company">
                <span>Copyright © 2017 weibo 信安三班某组</span>
            </p>
        </footer>
    </div>
</template>
<style scoped>
    a {
        cursor: pointer;
        color: #2e2e2e;
        text-decoration: none;
    }

    ul li {
        list-style: none;
    }

    em {
        font-style: normal;
    }

    .article {
        display: block;
        width: 800px;
        margin: 16px auto 0;
        border: 1px solid #ccc;
        background-color: #fff;
        overflow: hidden;
    }

    .article-item {
        display: block;
        width: 100%;
        min-height: 620px;
        overflow: hidden;

    }

    .article-detail {
        display: block;
        width: 760px;
        padding: 20px 20px;
    }

    .article-detail-img {
        display: block;
        float: left;
        position: relative;
    }

    .article-detail-img img {
        display: block;
        border-radius: 50px;
    }

    .article-detail-info {
        font-size: 13px;
        margin-left: 60px;
        overflow: hidden;
    }

    .wb-info {
        display: block;
        width: 100%;
        height: 30px;
    }

    .wb-info-name {
        float: left;
        line-height: 30px;
    }

    .wb-mark:hover {
        color: #f77c3d;
        border-color: #d9d9d9;
    }

    .wb-mark {
        display: inline-block;
        width: 54px;
        height: 18px;
        padding: 5px 4px;
        float: right;
        border-width: 1px;
        border-style: solid;
        border-color: #d9d9d9;
        box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1);
    }

    .wb-time {
        display: block;
        width: 100%;
        height: 30px;
        font-size: 13px;
    }

    .wb-text {
        margin-bottom: 2px;
        padding-bottom: 0;
        font-size: 14px;
        padding: 1px 0 3px;
        overflow: hidden;
        line-height: 23px;
        word-wrap: break-word;
    }

    .wb-img {
        display: block;
        width: 100%;
        overflow: hidden;
        margin-bottom: 5px;
    }

    .wb-img img {
        display: inline-block;
        width: 120px;
        height: 120px;
    }

    .wb-img li {
        width: 120px;
        height: 120px;
        margin: 4px 0 0 4px;
        float: left;
    }

    .wb-media {
        width: 372px;

    }

    .article .article-item .wb-row-line em {
        color: #808080;
        font-size: 13px;

    }

    .article-feed-handle {
        display: block;
        width: 100%;
        height: 40px;
        border-top: 1px solid #ccc;
        border-bottom: 1px solid #ccc;
        margin-left: -1px;
    }

    .wb-row-line li {
        width: 25%;
        float: left;
        height: 38px;
        text-align: center;
    }

    .wb-row-line span {
        display: block;
        height: 22px;
        margin: 7px 0;
        border-left-width: 1px;
        border-left-style: solid;
        line-height: 22px;
        border-color: #ccc;
    }

    .article-feed-repeat {
        display: block;
        width: 100%;
        padding: 16px 0 6px;
        background-color: #f2f2f5;
    }

    .wb-feed-push {
        width: 760px;
        height: 70px;
        padding: 0 20px 0 20px;
        overflow: hidden;
    }

    .wb-face {
        float: left;
    }

    .wb-repeat-list {
        padding: 0 20px;
    }

    .wb-repeat-top {
        width: 760px;
        margin: 6px 0 4px;
        padding: 12px 0 0;
        border-color: #ccc;
        border-top: 1px solid;
        overflow: hidden;
        line-height: 20px;
        font-size: 13px;
    }

    .wb-push {
        width: 700px;
        margin-left: 40px;
        overflow: hidden;
    }

    .W-input {
        width: 98%;
        height: 23px;
        margin: 0px;
        padding: 5px 2px 0px 6px;
        font-size: 12px;
        word-wrap: break-word;
        line-height: 18px;
        overflow: hidden;
        outline: none;
        box-shadow: 0px 0px 3px 0px rgba(0, 0, 0, 0.15) inset;
        border: 1px solid #ccc;
        border-radius: 2px;
    }

    .wb-push a {
        display: block;
        float: right;
        margin-right: 2px;
        width: 60px;
        height: 26px;
        background: #ffc09f;
        line-height: 26px;
        font-size: 12px;
        text-align: center;
        color: #ffffff;
        border-radius: 2px;
    }

    textarea {
        resize: none;
    }

    .W-input:focus {
        border-color: #f77c3d;
    }

    .company {
        display: block;
        width: 300px;
        margin: 20px auto;
    }

</style>
<script>
    import Repeat from './RepeatList.vue'

    export default{
        data(){
            return {
                face: [
                    {
                        name: "gello",
                        age: 12,
                        children: [
                            {
                                name: "gello",
                                age: 12,
                            }, {

                                name: "gello",
                                age: 12,
                            },
                            {
                                name: "gello",
                                age: 12,
                            },
                            {
                                name: "gello",
                                age: 12,
                            }
                        ]
                    },
                    {
                        name: "gello",
                        age: 12,
                        children: {
                            name: "hello"
                        }
                    },
                    {
                        name: "gello",
                        age: 12,
                        children: {
                            name: "hello"
                        }
                    }
                ]
            }
        },
        components: {
            Repeat
        }

    }
</script>