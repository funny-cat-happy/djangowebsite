//快捷访问菜单栏
var WriterInf=document.getElementById('WriterInf');
var ConnectWriter=document.getElementById('ConnectWriter');
ConnectWriter.onclick=function () {
        WriterInf.style.display='block';
};
// 项目展示菜单栏
var oProjectBtn=document.getElementById('ProjectShowBtn');
var oProjectContain=document.getElementById('ProjectShowContain');
var oProjectDiv=oProjectContain.getElementsByTagName('div');
oProjectBtn.onclick=function () {
    oProjectContain.removeChild(oProjectBtn);
    oProjectDiv[0].style.display='none';
    oProjectDiv[1].style.display='block';
};
//暂未开放
var oDiv=document.getElementsByClassName('NoFun');
for(var i=0;i<oDiv.length;i++)
{
    oDiv[i].onclick=function () {
        alert('暂未开放，敬请期待');
    }
}