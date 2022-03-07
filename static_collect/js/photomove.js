 var app = new Vue({
        el: '.name',
        data: {
            ImgSrc: ['./static/image/djangoLogo.jpg','./static/image/hack.jpg','./static/image/nonebot.png','./static/image/VueLogo.jpg'],
            Index: 0,
            timer: ''
        },
        methods: {
            ImgAutoMove: function () {
                this.Index++;
                if (this.Index > (this.ImgSrc.length-1)) {
                    this.Index = 0;
                }
            },
        },
        mounted() {
            this.timer = setInterval(this.ImgAutoMove, 5000);
        }
    });