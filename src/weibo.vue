<template>

   <div id="weibo">
       <nav-head></nav-head>
       <content></content>
   </div>

</template>

<script>
    import NavHead from './components/nav.vue'
    import Content from './components/content.vue'

    export default {
        components:{
            NavHead,
        }
    }
</script>

<style lang="scss" scoped>
    *{
        margin: 0;
        padding: 0;
    }
</style>
