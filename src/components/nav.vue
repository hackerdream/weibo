<template>

    <div class="nav">
        <div class="nav-head">
            <div class="icon left">
                <img src="#" height="40" width="80" alt="微博">
            </div>
            <div class="nav-search left">
                <input type="text" placeholder="大家都在搜">
                <a href="#" class="search"><i class="fa fa-search" aria-hidden="true"></i></a>
            </div>
            <div class="nav-guild right">
                <div class="nav-content left">
                    <ul>
                        <li>
                            <i class="fa fa-home fa-2x left"></i>
                            <a class="left">首页</a>
                        </li>
                    </ul>
                </div>
                <div class="nav-login left">
                    <a href="#" class="left">登录</a>
                    <a href="#" class="left">注册</a>
                </div>
            </div>
        </div>
    </div>

</template>
<style scoped>
    a{
        display: block;
        text-decoration: none;
        color: #696e78;
    }
    .nav {
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        overflow: hidden;
    }
    .left{
        float: left;
    }

    .right{
        float: right;
    }

    .nav .nav-head{
        width: 1100px;
    }

    @media screen and (max-width: 1000px) {
        .nav .nav-head{
            width: 800px;
        }
    }
    .icon {
        display: block;
        margin-left: 40px;
        width: 80px;
        height: 40px;
        padding: 10px;
    }

    .nav .nav-search {
        display: block;
        position: relative;
        margin-left: 20px;
        padding: 10px;
    }

    .nav-search input{
        display: block;
        padding: 5px 15px;
        width: 258px;
        height: 26px;
        border: 1px solid #ccc;
        border-radius: 20px;
        outline-style: none;
    }

    @media screen and (max-width: 1000px) {
        .nav .nav-search input{
            width: 150px;
        }
    }

    .search{
        display: block;
        position: absolute;
        color: #696e78 ;
        top: 18px;
        right: 10px;
        float: left;
        width: 30px;
        height: 26px;
    }

    .search:hover{
        cursor: pointer;
    }

    .nav-guild {
        margin-left: -10px;
        padding: 10px;

    }
    .nav-guild .nav-content{
        display: block;
        width: 320px;
        height: 40px;
        line-height: 40px;
        color: #696e78;
    }

    .nav-guild .nav-content ul{
        list-style: none;
    }

    .nav-guild .nav-content i{
        line-height: 40px;
    }

    .nav-guild .nav-content a{
        height: 40px;
        line-height: 40px;
    }
    .nav-guild .nav-login{
        display: block;
        height: 40px;
        line-height: 40px;
    }
    .nav-login a{
        margin: 0 10px;
    }

</style>
<script>
    export default{}
</script>