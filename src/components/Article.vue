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
                            <router-link to="#"></router-link>
                            <a>
                                <i></i>
                                <span>加关注</span>
                            </a>
                        </div>
                        <div class="wb-time">

                        </div>
                        <div class="wb-text">

                        </div>
                        <div class="wb-img">

                        </div>
                    </div>
                </div>
                <div class="article-feed-handle">

                </div>
                <div class="article-feed-repeat">

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
    a{
        cursor: pointer;
        color: #2e2e2e;
        text-decoration: none;
    }
    .article {
        display: block;
        width: 800px;
        padding: 20px 20px;
        margin: 16px auto 0;
        background-color: #e0e0e0;
        overflow: hidden;
    }

    .article-item {
        display: block;
        width: 100%;
        min-height: 620px;
        background-color: #a3be8c;

    }

    .article-detail {
        display: block;
        width: 100%;
        height: 360px;
        background-color: #bf616a;
    }

    .article-detail-img {
        display: block;
        float: left;
        position: relative;
    }
    .article-detail-img img{
        display: block;
        border-radius: 50px;
    }
    .article-detail-info{
        font-size: 13px;
        height: 200px;
        margin-left: 60px;
        overflow: hidden;
        background-color: #888888;
    }
    .article-detail-info a{
        display: block;
        width: 100%;
    }
    .article-feed-handle {
        display: block;
        width: 100%;
        height: 40px;
        background-color: #d4d5e0;
    }

    .article-feed-repeat {
        display: block;
        width: 100%;
        height: 200px;
        background-color: #E9DC51;
    }

    .company {
        display: block;
        width: 300px;
        margin: 20px auto;
    }
</style>
<script>
    export default{}
</script>