<template>
    <div class="head">
        <div class="head-box">
            <div class="head-position">
                <div class="head-img">
                    <img src="../../../../static/public/imgs/mt4.jpg" width="100" height="100"
                         style="border-radius:50%;">
                </div>
                <p style="margin-top:10px;font-size:18px;">{{host_name}}</p>
                <p style="margin-top:10px;font-size:12px;">我只因为你而嫣然一笑</p>
                <div style="    margin-top: 15px;text-align: center;">
                    <div v-show="!isOwn" style="display: inline-block;">
                        <router-link to="#"
                                     style="display: inline-block;height: 34px;line-height: 35px;padding: 0 15px;font-size: 14px;"
                                     class="head-follow">
                            <div v-show="isFriend" @click="deleteFriend">
                                <em class="fa fa-check" aria-hidden="false"></em>
                                <em>关注</em>
                            </div>
                            <div v-show="!isFriend" @click="addFriend">
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
    import store from '../../store/store.js'

    export default{
        created(){
            var that = this;

            function getMsg(id) {
                that.$axios.get('/main/' + id + '/user').then(function (res) {
                    that.host_name = res.data.name;
                    that.host_id = res.data.id;
                }).catch(function (err) {
                    console.log(err);
                });
                that.$axios.get('/weibo/user').then(function (res) {
                    that.user_name = res.data.name;
                    that.user_id = res.data.id;
                    if (that.user_name != null) {
                        that.$axios.get('/main/iff/' + that.host_id)
                                .then(function (resp) {
                                    console.log("1111" + resp.data.judge);
                                    that.isFriend = resp.data.judge;
                                })

                    }
                }).catch(function (err) {
                    console.log(err);
                });
            }

            if (this.$route.params.id) {
                this.uid = this.$router.app._route.params.id;
                getMsg(this.uid)
            }
            else {
                this.uid = window.location.pathname.split("/")[2];
                getMsg(this.uid)
            }
        },
        data(){
            return {
                isFriend: false,
                host_name: null,
                uid: null,
                user_id: null,
                host_id: null,
                user_name: null
            }
        },
        computed: {
            isOwn(){
                return this.uid == this.user_id
            }
        },
        methods: {
            deleteFriend(){
                var that = this;
                this.$axios.post('/main/delf/' + this.host_id)
                        .then(function (resp) {
                            that.isFriend = false
                        })
            },
            addFriend(){
                var that = this;
                if (this.user_name != null) {
                    this.$axios.post('/main/addf/' + this.host_id)
                            .then(function (resp) {
                                that.isFriend = true
                            })
                }
                else {
                    alert("请登陆")
                }
            }
        }

    }
</script>
