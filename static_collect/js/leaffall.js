var container = document.getElementById('leaf');
var nMaxWidth = window.innerWidth;
var nMaxHeigh = window.innerHeight;
for (let i = 0; i < 20; i++) {
    let odiv = document.createElement('div');
    odiv.style.top = Math.random() * nMaxHeigh + 'px';
    odiv.style.left = Math.random() * nMaxWidth + 'px';
    odiv.style.transform='rotate('+Math.random()*360+'deg)';
    let oimg=document.createElement('img');
    oimg.src='./static/image/leaf.png';
    odiv.appendChild(oimg);
    odiv = container.appendChild(odiv);
}
function ElementMove(elem) {
    for (let i = 0; i < elem.length; i++) {
        if (parseInt(elem[i].style.top) > nMaxHeigh*0.8 || parseInt(elem[i].style.left) > nMaxWidth*0.8||parseInt(elem[i].style.left) <0) {
            elem[i].style.top = Math.random() * nMaxHeigh + 'px';
            elem[i].style.left = Math.random() * nMaxWidth + 'px';
        } else {
            elem[i].style.top = elem[i].offsetTop + 1 + 'px';
            if (i<elem.length/2) {
                elem[i].style.left = elem[i].offsetLeft + 1 + 'px';
            } else {
                elem[i].style.left = elem[i].offsetLeft - 1 + 'px';
            }
        }
    }
}
var odiv = container.getElementsByTagName('div');
setInterval(function () {
    ElementMove(odiv);
}, 60)