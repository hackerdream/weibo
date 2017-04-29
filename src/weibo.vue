<template>

   <div id="weibo">
       <w-nav class="nav"></w-nav>
       <div class="main">
           <w-content class="content"></w-content>
           <login class="login"></login>
       </div>
   </div>

</template>

<script>
    import WNav from './components/nav.vue'
    import WContent from './components/content.vue'
    import Login from './components/login.vue'

    export default {
        components:{
            WNav,WContent,Login
        }
    }
</script>

<style lang="scss" scoped>
    *{
        margin: 0;
        padding: 0;
    }
    #weibo{
        padding-top: 60px;
        overflow: hidden;

    }
    .main{
        width: 1060px;
        margin: 0 auto;
    }
    @media screen and (max-width: 1050px){
        .main{
            width: 760px;
            margin: 0 auto;
        }
    }
    .nav {
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        border-bottom: 1px solid #cacaca;
        z-index: 999;
        background-color: #ffffff;
        overflow: hidden;
    }
    .content{
        display: inline-block;
        position: relative;
        vertical-align: top;
        margin: 0 auto;
        width: 760px;
        z-index: 1;
    }
    .login{
        margin-left: 20px;
        display: inline-block;
        position: relative;
        width: 240px;
        padding: 0 16px;
        z-index: 10;
        border: 1px solid #ccc;

    }
    @media screen  and (max-width: 1050px){
        .login{
            display: none;
        }
    };
</style>
