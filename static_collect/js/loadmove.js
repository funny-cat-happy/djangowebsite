var nMaxHeigh=window.innerHeight;
var nMaxWidth=window.innerWidth;
var canvas=document.querySelector('#rain');
var fillcolor='#76f8ff';
var RainTimer='';
var WaitTimer='';
canvas.height=nMaxHeigh;
canvas.width=nMaxWidth;
window.onresize=function () {
    nMaxHeigh=window.innerHeight;
    nMaxWidth=window.innerWidth;
    canvas.height=nMaxHeigh;
    canvas.width=nMaxWidth;
};
var cancon=canvas.getContext('2d');
var nRainNum=15;
function WaterFall(initX,y) {
    var r=0;
    cancon.beginPath();
    cancon.fillStyle=fillcolor;
    cancon.arc(initX,y,r++,0,Math.PI*2);
    cancon.stroke()
}
function RainDrop() {
    var y=0;
    var r=0;
    var initX=Math.random()*nMaxWidth;
    var maxWater=nMaxHeigh*0.6+nMaxHeigh*0.2*Math.random();
    setInterval(function () {
        cancon.fillStyle=fillcolor;
        if(y>maxWater)
        {
            if(r<50)
            {
                cancon.beginPath();
                cancon.strokeStyle=fillcolor;
                cancon.arc(initX,y,r++,0,Math.PI*2);
                cancon.stroke()
            }
            else
            {
                y=0;
                r=0;
                maxWater=nMaxHeigh*0.6+nMaxHeigh*0.2*Math.random();
            }
        }
        else
        {
            cancon.beginPath();
            cancon.fillRect(initX,y=y+5,10,10);
        }
    },1000/60)
}
setInterval(function () {
        cancon.beginPath();
        cancon.fillStyle='rgba(0,0,0,0.02)';
        cancon.fillRect(0,0,nMaxWidth,nMaxHeigh);
    });
for(let i=0;i<nRainNum;i++)
{
    RainTimer=setTimeout(RainDrop,800*i);
}
// 绘制字体
cancon.font = "30px 黑体";
cancon.fillStyle = fillcolor;
cancon.textAlign = "center";
cancon.textBaseline = "middle";
cancon.fillText("冒雨加载中请稍后......", nMaxWidth*0.5, nMaxHeigh*0.9);
WaitTimer=setInterval(function () {
    cancon.fillText("冒雨加载中请稍后......", nMaxWidth*0.5, nMaxHeigh*0.9);
},1500);
document.onreadystatechange=function () {
    if(document.readyState==='complete')
    {
        clearTimeout(RainTimer);
        clearInterval(WaitTimer);
        var canvas=document.querySelector('#rain');
        document.body.removeChild(canvas);
        var left=document.getElementById('LoadingLeft');
        var right=document.getElementById('LoadingRight');
        left.style.animation='LeftMove 5s';
        left.style.animationFillMode='forwards';
        right.style.animation='RightMove 5s';
        right.style.animationFillMode='forwards';
        setTimeout(function () {
            left.style.display='none';
            right.style.display='none';
        },5000);
    }
};