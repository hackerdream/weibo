<template>
    <div>
        <div class="info-edit">
            <div class="info-edit-box">
                <ul>
                    <li v-for="info in infos">
                        <div class="info-name">
                            <span>{{info.name}}：</span>
                        </div>
                        <div class="info-detail-box">
                            <span class="info-detail"
                                  :class="{status1:info.edit,status2:!info.edit}">{{info.content}}</span>
                            <input v-model="info.content" :class="{status1:!info.edit,status2:info.edit}">
                            <a style="float:right">
                                <span @click="info.edit =!info.edit"
                                      :class="{status1:info.edit,status2:!info.edit}">编辑</span>
                            </a>
                        </div>
                    </li>

                </ul>
                <a class="edit-submit">
                    <span>保存</span>
                </a>
            </div>
        </div>
    </div>
</template>
<style>
    ul li {
        list-style: none;
    }

    input {
        outline-style: none;
        border: 1px solid #ccc;
    }

    input:focus {
        border: 1px solid #f77c3d;
    }

    a:hover {
        cursor: pointer;
        color: #f77c3d;
    }

    .status1 {
        display: none;
    }

    .status2 {
        display: inline-block;
    }

    .info-edit {
        width: 100%;
        height: 100px;
        min-height: 720px;
        position: absolute;
        top: 60px;
        left: 0;
        z-index: 10;
        background: url(../../../../static/public/imgs/body_bg2.jpg) no-repeat top center;
        background-color: #1d0e2b;
    }

    .info-edit-box {
        display: block;
        width: 800px;
        height: 400px;
        margin: 40px auto;
        padding: 40px;
        background-color: #fff;
    }

    .info-edit-box li {
        width: 640px;
        height: 60px;
        margin: 0 auto;
    }

    .info-edit-box input {
        width: 400px;
        height: 40px;
        padding: 5px 10px;
        font-size: 16px;

    }

    .info-name {
        display: inline-block;
        width: 100px;
        height: 50px;
        line-height: 50px;
        font-size: 14px;
        text-align: left;
    }

    .info-detail-box {
        display: inline-block;
        width: 500px;
        height: 50px;
    }

    .edit-submit {
        display: block;
        width: 640px;
        height: 40px;
        background-color: #ffc09f;
        margin: 0 auto;
        text-align: center;
        line-height: 40px;
        color: #fff;
    }
</style>
<script>
    export default{
        data(){
            return {
                infos: [
                    {
                        name: "昵称",
                        edit: false,
                        content: "最帅的人"
                    },
                    {
                        name: "手机号",
                        edit: false,
                        content: 123456
                    },
                    {
                        name: "邮箱",
                        edit: false,
                        content: "761540662@qq.com"
                    },
                    {
                        name: "个性签名",
                        edit: false,
                        content: "我已经超神了"
                    }
                ]
            }
        }
    }
</script>
