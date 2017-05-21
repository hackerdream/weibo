<template>
    <div class="w-login">
        <div class="login">
            <h1>账号登录</h1>
            <div class="login-box">
                <input type="email" placeholder="请输入邮箱" v-model="email">
                <input type="password" placeholder="请输入密码" v-model="password">
            </div>
            <footer>
                <div class="login-msg">
                    <div class="login-memory">
                        <input type="checkbox" value="记住密码">
                        <span>记住我</span>
                    </div>
                    <div class="refoundPsd">
                        <a>忘记密码</a>
                    </div>
                </div>
                <div class="clearFLoat"></div>
                <a class="login-weibo" @click="login()">
                    <span>登录</span>
                </a>
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
        font-size: 10px;
        background-color: #ffffff;
        overflow: hidden;
        color:#808080;
    }

    .login-box {
        margin: 0 auto;
        display: block;
        width: 100%;
        text-decoration: none;
    }

    .login-box input {
        width: 186px;
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
    .login-memory{
        display: block;
        width: 50%;
        float: left;
        height: 40px;
        line-height: 40px;
    }
    .refoundPsd{
        display: block;
        width: 50%;
        float: right;
        height: 40px;
        line-height: 40px;
        text-align: right;
    }
    .refoundPsd a{
        text-decoration: none;
    }
    .refoundPsd:hover{
        cursor: pointer;
    }
    .clearFLoat{
        clear: both;
    }
    .login-weibo{
        display: block;
        width: 206px;
        height: 32px;
        line-height: 30px;
        background: #ff8140;
        border: 1px solid #f77c3d;
        border-radius: 4px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.25);
        white-space: nowrap;
        text-align: center;
        color: #ffffff;
        font-size: 16px;
        outline: none;
        text-decoration: none;
        margin-bottom: 40px;
    }
    .login-weibo:hover{
        cursor: pointer;
    }
</style>
<script>
    export default{
        data(){
            return {
                email:'',
                password:''
            }
        },
        methods:{
            login(){
                console.log("effect");
                this.axios.post('/user_login',{
                    email:this.email,
                    password:this.password
                }).then(function(res){
                    window.location.href='/weibo';
                }).catch(function (err) {
                    console.log(err);
                })
            }
        }
    }
</script>