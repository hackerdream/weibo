<template>

    <div>
        <ul class="repeat">
            <li class="repeat-list" v-for="item in face" :style="[Padding]">
                <div style="float: left;" v-if="isFace" class="repeat-face">
                    <img src="../../public/imgs/mt4.jpg" width="30" height="30">
                </div>
                <div class="repeat-info" :style="[MarginLeft]">
                    <router-link to="#">
                        我是你爸爸：
                    </router-link>
                    <span>
                    【历史是有痕迹的】上一代的恩怨，后辈们吸取教训，不作恶，是做人的最基本底线。认错的认错，放下的放下吧，就是给自己一个舒服的现在，不是嚒。
                    </span>
                    <div class="repeat-info-detail">
                        <div class="repeat-info-time">
                            5月12日 13:15
                        </div>
                        <div class="repeat-thumbs">
                            <em class="fa fa-thumbs-o-up" aria-hidden="true"></em>
                            <em style="line-height: 16px">1234</em>
                        </div>
                        <div class="repeat-msg">
                            <a>
                                <span style="color: #b0bdd0" @click="showRepeatInput">
                                回复
                                </span>
                            </a>
                            <span class="W_arrow_bor W_arrow_bor_t" v-if="showRepeat">
                                    <i class="S_bg2_br"></i>
                                </span>
                        </div>
                    </div>
                    <div class="re-repeat-detail" v-if="showRepeat">
                        <div class="repeat-wr">
                            <textarea type="text" class="W-input"></textarea>
                        </div>
                        <div class="repeat-sbm">
                            <a>
                                <span>提交</span>
                            </a>
                        </div>
                    </div>
                </div>

                <repeat-list v-if="item.children"
                             :face="item.children"
                             :improveCount="count"
                             :style="[Box,ChildrenWidth,Color]"
                             :isFace='false'>
                </repeat-list>
            </li>
        </ul>

    </div>

</template>
<style scoped>
    ul li {
        display: block;
        list-style: none;
    }

    .repeat {
        font-size: 13px;
        overflow: hidden;
    }

    .repeat-list {
        padding-top: 20px;
        overflow: hidden;
    }

    .repeat-info a {
        color: #257cde;
        text-decoration: none;
        cursor: pointer;
    }

    .repeat-face {
        display: inline-block;

    }

    .wb-row-line a:hover {
        color: #eb7350 !important;
    }

    .repeat-info-detail {
        display: block;
        position: relative;
        width: 100%;
        height: 30px;
        font-size: 13px;
        color: #b4bdd0;
    }

    .repeat-info-time {
        display: inline-block;
        line-height: 30px;
        float: left;
    }

    .repeat-msg {
        display: inline-block;
        position: relative;
        width: 36px;
        height: 30px;
        float: right;
    }

    .repeat-thumbs {
        display: block;
        float: right;
        height: 16px;
        padding-left: 10px;
        margin-right: 5px;
        margin-top: 5px;
        border-left: 1px solid #ccc;
        line-height: 20px;
    }

    .W_arrow_bor {
        position: absolute;
        top: 17px;
        right: 5px;
    }

    .W_arrow_bor i {
        display: inline-block;
        width: 0;
        height: 0;
        border-width: 7px;
        border-style: solid;
        overflow: hidden;
        color: #fff;
        font-size: 0;
        line-height: 0;
        vertical-align: top;
    }

    .W_arrow_bor_t i {
        _border-style: dashed dashed solid dashed;
        border-top-color: transparent;
        border-right-color: transparent;
        border-left-color: transparent;
    }

    .repeat-info-detail span {
        text-align: center;
        line-height: 30px;
        padding-right: 10px;
        color: #333;
    }

    .repeat-wr {
        width: 95%;
        margin: 0 auto;
        color: #808080;

    }

    .W-input {
        width: 100%;
        height: 23px;
        margin: 0;
        padding: 5px 2px 0 6px;
        font-size: 12px;
        word-wrap: break-word;
        line-height: 18px;
        overflow: hidden;
        outline: none;
        box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.15) inset;
        border: 1px solid #ccc;
        border-radius: 2px;
    }

    .re-repeat-detail {
        position: relative;
        width: 95%;
        padding: 16px 16px;
        background-color: #fff;
    }

    .repeat-sbm {
        display: block;
        width: 95%;
        height: 30px;
        margin: 0 auto;
    }

    .repeat-sbm a {
        display: block;
        float: right;
        margin-right: 2px;
        width: 60px;
        height: 26px;
        background: #ffc09f;
        line-height: 26px;
        font-size: 12px;
        text-align: center;
        color: #ffffff;
        border-radius: 2px;
    }

    .repeat-wr:focus {
        color: #333;
    }

    textarea {
        resize: none;
    }
</style>
<script>

    export default{
        name: "repeat-list",
        props: {
            face: {
                type: [Array, Object, Number]
            },
            improveCount: {
                type: Number,
                default: 0
            },
            isFace: {
                type: Boolean,
                default: true
            }
        },
        data(){
            return {
                showRepeat: false
            }
        },
        methods: {
            showRepeatInput(){
                this.showRepeat = !this.showRepeat;
            }
        },
        computed: {
            count(){
                var c = this.improveCount;
                return ++c;
            },
            MarginLeft(){
                return {
                    'margin-left': 40 - this.improveCount * 40 + 'px'
                }
            },
            Box(){
                return {
                    'float': 'right',
                    'padding': '16px'
                }
            },
            ChildrenWidth(){
                return {
                    'width': 90 + '%'
                }
            },
            Color(){
                return {
                    'background-color': '#eaeaec',
                }
            },
            Padding(){
                return {
                    'padding-top': 20 - this.improveCount * 20 + 'px',
                    'margin-top': this.improveCount * 10 + 'px',
                    'border-bottom': this.improveCount+'px solid #d9d9d9'
                }


            }
        }

    }
</script>