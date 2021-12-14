
function myFunction() {
document.getElementById("demo1").innerHTML = "Hello Dolly!";
document.getElementById("demo2").innerHTML = "How are you?";
}
function click(){
    console.log('Hi function')
        document.getElementById("p1").innerHTML = 'cool';
}
console.log('Yuli Grossman')

var imgs = [
        "images/girl.PNG",
        "images/pug.jpg",
        "images/yuli.png"
];
var i = 0;

function stopMotion(){
    setTimeout(function(){
        document.getElementById("rotate_yuli").src = imgs[i];
        i++;
        if(i<imgs.length){
            stopMotion();
        }
        else {
            i = 0;
        }
    }, 2000);
}








