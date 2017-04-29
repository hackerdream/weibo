<template>
    <div class="w-login">
        <div class="login">
            <h1>账号登录</h1>
            <div class="login-box">
                <input type="text" placeholder="请输入用户名">
                <input type="password" placeholder="请输入密码">
            </div>
            <footer>
                <div class="login-msg">

                </div>
            </footer>
        </div>
    </div>
</template>
<style scoped>
    .login h1{
        padding: 10px 0 ;
        width: 50%;
        font-size: 16px;
        text-align: center;
        border-bottom: 1px solid #eb7350;
    }
    .login {
        width: 208px;
        height: 400px;
        background: #a3be8c;
        overflow: hidden;
    }

    .login-box {
        margin: 0 auto;
        display: block;
        width: 100%;
        text-decoration: none;
    }

    .login-box input {
        width: 86%;
        height: 26px;
        margin-top: 20px;
        padding: 5px 10px;
        line-height: 30px;
        border: 1px solid #ccc;
        font-size: 10px;
        border-radius: 4px;
        outline-style: none;
    }
    input:focus{
        border-color:#eb7350 !important;
    }
</style>
<script>
    export default{}
</script>