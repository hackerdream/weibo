<template>
    <div class="w-login">
        <div>
            <a class="close-layer" @click="closeLayer">
                <em class="fa fa-times" aria-hidden="true"></em>
            </a>
        </div>
        <div class="login-info">
            <span>账号登录</span>
        </div>
        <div class="login">
            <input type="text" placeholder="用户名">
            <input type="password" placeholder="密码">
        </div>
        <div class="sub-login-info">
            <div class="remember-login">
                <input type="checkbox">
                <em>下次自动登录</em>
            </div>
            <div class="forget-login-pwd">
                <a href="#">
                    <span>忘记登录密码</span>
                </a>
            </div>
        </div>
        <div class="login-box">
            <a href="#" class="w-btn-34">
                <em>登录</em>
            </a>
        </div>
    </div>
</template>
<style scoped>
    .w-login {
        display: block;
        background-color: #ffffff;
        overflow: hidden;
    }

    .close-layer {
        float: right;
        margin-right: 10px;
    }
    .close-layer:hover{
        cursor: pointer;
    }

    .login-info {
        width: 370px;
        height: 30px;
        margin: 60px auto 10px;
        padding-bottom: 10px;
        text-align: center;
        border-bottom: 3px solid #f7691d;
        font-weight: bold;
    }

    .login {
        display: block;
        height: 90px;
        width: 370px;
        padding: 16px;
        margin: 0 auto;
    }

    .login input {
        display: block;
        height: 20px;
        width: 220px;
        margin: 10px auto;
        padding: 5px 10px;
        border-radius: 4px;
        border: 1px solid #ccc;
        outline-style: none;
    }

    .login input:focus {
        border: 1px solid #f77c3d !important;
    }

    .sub-login-info {
        width: 240px;
        margin: 0 auto;
        overflow: hidden;
        font-size: 12px;
    }

    .sub-login-info .remember-login {
        float: left;
    }

    .sub-login-info .forget-login-pwd {
        float: right;
    }

    .sub-login-info .forget-login-pwd a {
        text-decoration: none;
        color: black;
    }

    .login-box {
        display: block;
        width: 240px;
        height: 35px;
        margin: 10px auto;

    }

    .login-box .w-btn-34 {
        display: inline-block;
        width: 210px;
        height: 35px;
        padding: 0 15px;
        line-height: 35px;
        text-align: center;
        font-size: 14px;
        color: #ffffff;
        border: 1px solid #f77c3d;
        background-color: #ff8140;
    }

    .login-box a {
        text-decoration: none;

    }
</style>
<script>
    export default{
        methods:{
            closeLayer(){
                this.$emit('close-layer');
            }
        }
    }
</script>