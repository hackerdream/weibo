<template>
    <div class="head">
        <div class="head-box">
            <div class="head-position">
                <div class="head-img">
                    <img src="../../../../static/public/imgs/mt4.jpg" width="100" height="100"
                         style="border-radius:50%;">
                </div>
                <p style="margin-top:10px;font-size:18px;">最帅的人</p>
                <p style="margin-top:10px;font-size:12px;">我只因为你而嫣然一笑</p>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .head-box {
        position: relative;
        width: 900px;
        height: 300px;
        margin: 20px auto;
    }

    .head-position {
        position: absolute;
        width: 100%;
        height: 300px;
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
</style>
<script>
    export default{}
</script>
