<template>
    <div id="app">
        <div>
            <m-nav class="nav" :isLogin=isLogin :username=user_name></m-nav>
        </div>
        <div class="">
            <m-head></m-head>
        </div>

    </div>
</template>
<style scoped>
    * {
        margin: 0;
        padding: 0;
    }

    #app {
        padding-top: 60px;
        overflow: hidden;
        background: url(../../../../static/public/imgs/body_bg2.jpg) no-repeat top center;
        background-color: #1d0e2b;
    }

    .nav {
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        border-bottom: 1px solid #cacaca;
        z-index: 99;
        background-color: #ffffff;
    }


</style>
<script>
    import MNav from './MNav.vue'
    import MContent from './MContent.vue'
    import MHead from './MHead.vue'

    export default{
        created(){
            var that = this;
            this.$axios.get('/weibo/user')
                    .then(function (resp) {
                        that.user_name = resp.data.name;
                        if(that.user_name != undefined){
                            that.isLogin = true;
                            console.log(that.isLogin);
                        }
                    })
        },
        data(){
            return {
                user_name: '',
                isLogin: false
            }
        },
        components: {
            MContent, MNav, MHead
        },

    }
</script>
