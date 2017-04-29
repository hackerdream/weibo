<template>

    <div class="w-content">
        <div class="content">
            <div class="current-news">
                <ul>
                    <li class="current-new"></li>
                    <li class="current-new"></li>
                </ul>
            </div>
            <div class="content-ad">
                <div class="advertisement">

                </div>
            </div>
            <div class="hot-news">
                <ul>

                </ul>
            </div>
        </div>
    </div>

</template>
<style>
    ul li {
        display: block;
        list-style: none;
    }

    .content{
        display: block;
        padding: 0 5px;
        overflow: hidden;
    }

    .current-news {
        display: block;
        position: relative;
        padding: 16px 16px;
        border: 1px solid #ccc;
        width: 728px;
        background-color: #888888;
    }

    .current-new {
        display: block;
        width: 100%;
        margin: 0 auto;
        height: 240px;
        background: #bf616a;
    }

    .current-new + .current-new {
        margin-top: 16px;
    }

    .content-ad {
        display: block;
        position: relative;
        width: 728px;
        padding: 16px 16px;
        border: 1px solid #ccc;
        background: #bf616a;
    }
    .current-news + .content-ad ,.content-ad + .hot-news{
        margin-top: 16px;
    }
    .advertisement{
        display:block;
        width: 100%;
        height: 160px;
    }
    .hot-news{
        display: block;
        width: 728px;
        padding: 16px 16px;
        border: 1px solid #ccc;
        height: 240px;
        background: #E9DC51;
    }
</style>
<script>
    export default{}
</script>