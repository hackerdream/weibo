<template>

    <div class="w-content">
        <div class="content">

            <div class="article-edit">
                <textarea class="edit-box" v-model="weibo_content">

                </textarea>
                <div class="article-edit-bar">
                    <div v-show="imgs.length >0">
                        <ul>
                            <li v-for="image in imgs"
                                style="display:inline-block;position:relative;width:100px;height:100px;margin-left:10px;">
                                <img :src="image.base64" width="100" height="100" style="display:inline-block;"/>
                                <a href="#" style="position: absolute;top:0;right:0;" @click='delImage($index)'>
                                    <em class="fa fa-times" aria-hidden="true"></em>
                                </a>
                            </li>
                        </ul>
                    </div>

                    <div class="article-img-push">
                        <a class="article-img-upload">
                            <em class="fa fa-picture-o" style="color:#84c002;" aria-hidden="true"></em>
                            <em style="color:#918ea5">图片</em>
                            <div>
                                <input id="inputFile" type="file" accept="image/png,image/gif,image/jpg" multiple
                                       @change="onFileChange">
                            </div>
                        </a>

                        <div class="article-push" @click="submitEdit">
                            <a>
                                <span>提交</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <ul class="article">
                <li class="article-item" v-for="article in articles">
                    <div class="article-detail">
                        <router-link to="#" class="article-detail-img">
                            <img src="static/public/imgs/infoFace.jpg" width="50" height="50">
                        </router-link>
                        <div class="article-detail-info">
                            <div class="wb-info">
                                <router-link to="#" class="wb-info-name">{{article.host}}</router-link>
                            </div>
                            <div class="wb-time">
                                {{article.time}}
                            </div>
                            <div class="wb-text">
                                {{article.text}}
                            </div>
                            <div class="wb-img">
                                <ul class="wb-media">
                                    <li v-for="photo in article.photo">
                                        <img :src="photo.url">
                                        <img src="static/public/imgs/mt4.jpg">
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
                                    <em>23333</em>
                                </span>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="article-feed-repeat" v-if="isOnClickToCom">
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

        <div class="W-person-info">
            <div class="W-person-info-face">
                <img src="static/public/imgs/mt3.jpg" width="50" height="50" alt="我是帅比"
                     class="person-info-face" @click="toMainPage">
            </div>
            <div class="person-info-box">
                <div class="person-info-name" @click="toMainPage">
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
                        <router-link to="#">
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
        color: #918ea5;
        text-decoration: none;
    }

    ul li {
        list-style: none;
    }

    em {
        font-style: normal;
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

    .article-edit {
        width: 680px;
        min-height: 150px;
        padding: 20px 20px;
        margin-top: 10px;
        outline-style: none;
        background-color: #261d3b;
    }

    .edit-box {
        width: 644px;
        height: 64px;
        padding: 16px 16px;
    }

    .edit-box:focus {
        border-color: #f77c3d;
    }

    .article-edit-bar {
        display: block;
        width: 100%;
        margin-top: 10px;
        overflow: hidden;
    }

    .article-img-push {
        display: block;
        float: left;
        width: 100%;
        height: 30px;
    }

    .article-push {
        display: block;
        float: right;
        width: 60px;
        height: 30px;
        margin: 0 auto;
    }

    .article-img-upload {
        display: inline-block;
        position: relative;
        width: 60px;
        height: 30px;
    }

    .article-img-push .article-img-upload input:hover {
        cursor: pointer !important;
    }

    .article-img-push .article-img-upload:hover {
        cursor: pointer !important;
    }

    .article-img-upload input {
        position: absolute;
        width: 60px;
        height: 30px;
        right: 0;
        top: 0;
        opacity: 0;
        filter: alpha(opacity=0);
        cursor: pointer
    }

    .article-push a {
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

    .article {
        display: block;
        width: 720px;
        margin: 10px auto 0;
        border: 1px solid #261d3b;
        font-size: 13px;
        overflow: hidden;
    }

    .article-item {
        display: block;
        width: 100%;
        min-height: 420px;
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
        background-color: #261d3b;
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
        border-top: 1px solid #3e355b;
        border-bottom: 1px solid #3e355b;
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
        border-color: #3e355b;
    }

    .article-feed-repeat {
        display: block;
        width: 100%;
        padding: 16px 0 6px;
        background-color: #1d1531;
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

    @media screen and (max-width: 1000px) {
        .content .W-person-info {
            display: none;
        }
    }

    .W-person-info {
        display: block;
        position: relative;
        float: right;
        width: 260px;
        height: 190px;
        overflow: hidden;
        text-align: center;
        margin-top: 10px;
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
        background-image: url(../../../../static/public/imgs/profile_cover_s.jpg)
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

    import Repeat from './URepeatList.vue'
    import store from '../../store/store.js'
    export default{
        created(){
            var that = this;
            this.$axios.get('/weibo/article')
                    .then(function (resp) {
                        [].forEach.call(resp.data, function (item) {
                            that.articles.push(item);
                        })
                    });
            this.$axios.get('/weibo/user').then(function (res) {
                that.user_id = res.data.id;
            }).catch(function (err) {
                console.log(err);
            });
        },
        data(){
            return {
                articles: [],
                isOnClickToCom: false,
                imgs: [],
                weibo_content: '',
                user_id:null
            }
        },
        components: {
            Repeat
        },
        methods: {
            addPic () {
                $('input[type=file]').trigger('click');
                return false
            },
            onFileChange (e) {
                var files = e.target.files || e.dataTransfer.files;
                if (!files.length) return;
                console.log("files[0]", files)
                this.createImage(files)
            },
            createImage (file) {
                var that = this;
                var reader = null;
                var leng = file.length;
                for (var i = 0; i < leng; i++) {
                    reader = new window.FileReader();
                    reader.readAsDataURL(file[i]);
                    console.log("files1", file[i].name);
                    var fileName = file[i].name;
                    reader.onload = function (e) {
                        that.imgs.push({
                            base64: e.target.result,
                            name: fileName
                        });
                    }
                }
            },
            removeImage: function (e) {
                this.imgs = []
            },
            delImage: function (index) {
                this.imgs.shift(index)
            },
            submitEdit(){
                var that = this;
                console.log({
                    text: that.weibo_content,
                    imgs: that.imgs
                });
                this.$axios.post('/weibo/write_article', {
                    text: that.weibo_content,
                    imgs: that.imgs
                })
                        .then(function (resp) {
                            console.log(resp);
                            window.location.href = '/weibo'
                        }).catch(function (err) {
                    console.log(err);
                })
            },
            toMainPage(){
                window.location.href = '/main/'+this.user_id;
            }
        }
    }
</script>