<template>
    <div class="m-content">
        <div class="content">

            <div class="m-user">
                <div class="left m-user-info" style=" padding:12px 0;">
                    <ul class="user-atten">
                        <li>
                            <router-link :to="{ name : 'follow' , params: { id : uid } }">
                                <strong>82</strong>
                                <span>关注</span>
                            </router-link>
                        </li>
                        <li>
                            <router-link :to="{ name : 'fensi' , params : {id : uid} }">
                                <strong>72</strong>
                                <span>粉丝</span>
                            </router-link>
                        </li>
                        <li>
                            <router-link to="#">
                                <strong>5</strong>
                                <span>微博</span>
                            </router-link>
                        </li>
                    </ul>
                </div>
                <div class="content-box right">
                    <ul class="article">
                        <li class="article-item" v-for="article in articles">
                            <div class="article-detail">
                                <router-link to="#" class="article-detail-img">
                                    <img src="/static/public/imgs/infoFace.jpg" width="50" height="50">
                                </router-link>
                                <div class="article-detail-info">
                                    <div class="wb-info">
                                        <router-link to="#" class="wb-info-name">{{article.host}}</router-link>
                                        <a class="wb-mark" v-show="isOwn">
                                            <em class="fa fa-plus" aria-hidden="true"></em>
                                            <span>加关注</span>
                                        </a>
                                    </div>
                                    <div class="wb-time">
                                        5月11日 07:10 来自 iPhone 6s Plus
                                    </div>
                                    <div class="wb-text">
                                        {{article.text}}
                                    </div>
                                    <div class="wb-img">
                                        <ul class="wb-media">
                                            <li v-for='photo in article.photo'>
                                                <img :src="photo.url">
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
                                            <span @click="isOnClickToCom = !isOnClickToCom">
                                                <em class="fa fa-commenting-o" aria-hidden="true"></em>
                                                <em>2034</em>
                                            </span>
                                        </a>
                                    </li>
                                    <li>
                                        <a>
                                            <span>
                                                <em class="fa fa-thumbs-o-up" aria-hidden="true"></em>
                                                <em>{{article.up}}</em>
                                            </span>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            <div class="article-feed-repeat" v-show="isOnClickToCom">
                                <div class="wb-repeat-list">
                                    <div class="repeat">
                                        <repeat :face="face">

                                        </repeat>
                                    </div>
                                </div>
                            </div>
                        </li>
                    </ul>

                </div>

            </div>
        </div>
        <router-view></router-view>
    </div>
</template>
<style scoped>
    ul li {
        list-style: none;
    }

    a {
        text-decoration: none;
        cursor: pointer;
    }

    .left {
        float: left;
    }

    .right {
        float: right;
    }

    .m-user {
        width: 1000px;
        height: 600px;
    }

    .content {
        display: block;
        width: 1000px;
        margin: 0 auto;
    }

    @media screen and (max-width: 1000px) {
        .m-content .m-user-info {
            display: none;
        }

        .m-content .content {
            display: block;
            width: 722px;
            margin: 0 auto;
        }

        .m-content .m-user {
            display: block;
            width: 722px;
            margin: 0 auto;
        }
    }

    .m-content a {
        color: #918ea5;
        font-size: 13px;
        text-align: center;
    }

    .user-atten {
        display: block;
        width: 228px;
        height: 35px;
        padding-top: 10px;
        padding-bottom: 10px;
        background-color: #261d3b;
    }

    .user-atten li {
        float: left;
        width: 75px;
        border-right: 1px solid #918ea5;

    }

    .user-atten ul {
        height: 34px;
        overflow: hidden;
        margin: 10px 0 0 0;
        font-size: 18px;
    }

    .user-atten li:last-child {
        border: 0;
    }

    .user-atten span, .user-atten strong {
        display: block;

    }

    .user-atten .user li:hover {
        color: #eb7350 !important;
    }

    .m-content a:hover {
        color: #eb7350;
    }

    .content-box {
        display: inline-block;
        width: 722px;
        margin-top: 10px;
        overflow: hidden;
    }

    . .article {
        display: block;
        width: 720px;
        margin: 10px auto 0;
        border: 1px solid #ccc;
        font-size: 13px;
        overflow: hidden;
    }

    .article-item {
        display: block;
        width: 100%;
        overflow: hidden;
        background-color: #261d3b;
    }

    .article-item + .article-item {
        margin-top: 10px;
    }

    .article-detail {
        display: block;
        width: 680px;
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
        border-color: #302552;
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
        border-top: 1px solid #302552;
        border-bottom: 1px solid #302552;
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
        border-color: #302552;
    }

    .article-feed-repeat {
        display: block;
        width: 100%;
        padding: 16px 0 6px;
        background-color: #261d3b;
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
</style>
<script>
    import Repeat from './MRepeatList.vue'

    export default{
        created(){
            var that = this;

            function modifyPhoto(photos) {
                [].forEach.call(photos, function (photo) {
                    photo.url = '/' + photo.url;
                });
                return photos;
            }
            function getMsg(uid){
                that.$axios.get('/main/' + uid + '/article').then(function (res) {
                    that.user_id = res.data.id;
                    that.user_name = res.data.name;
                });
                that.$axios.get('/main/' + uid + '/article').then(function (res) {
                    [].forEach.call(res.data, function (item) {
                        that.articles.push(
                                {
                                    host: item.host,
                                    text: item.text,
                                    photo: modifyPhoto(item.photo),
                                    time: item.time,
                                    up: item.up,
                                    isShow:item.isShow,
                                    repeats:item.repeats
                                }
                        )

                    })
                })
            }

            if (this.$route.params.id) {
                this.uid = this.$router.app._route.params.id;
                getMsg(this.uid);
            }
            else {
                this.uid = window.location.pathname.split("/")[2];
                getMsg(this.uid);
            }
            console.log('uid'+this.uid);

        },
        data(){
            return {
                isOnClickToCom: false,
                isOwn: false,
                articles: [],
                user_id: null,
                user_name: '',
                uid: null
            }
        },
        components: {
            Repeat
        },
        computed: {
            isOwn(){
                return this.uid === this.user_id
            }
        }
    }
</script>
