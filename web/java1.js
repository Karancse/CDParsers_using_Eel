var z=-1;
var x=document.getElementById("button2");


/*

-1 - not set
1 - ll(0)
2 - ll(1)
3 - lr(1)
4 - slr(1)
5 - clr(1)
6 - lalr(1)

*/


async function GenerateLR0()
{
    //alert("Hi");
    console.log(z);
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.ll0parser(zx,xz)();
    //document.getElementById('outbox').innerHTML="1234";
    //document.getElementById('outbox').innerHTML=q;
}


function GenerateENTER(){
    document.getElementById('outbox').innerHTML="<h3>Choose any parser</h3>";
}


async function GenerateLL0()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.ll0parser(zx,xz)();
}

async function GenerateLL1()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.ll1parser(zx,xz)();
}

async function GenerateLR0()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.lr0parser(zx,xz)();
}

async function GenerateLR1()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.lr1parser(zx,xz)();
}

async function GenerateSLR1()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.slr1parser(zx,xz)();
}

async function GenerateCLR1()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.clr1parser(zx,xz)();
}

async function GenerateLALR1()
{
    s="";
    let zx=document.getElementById('z1').value;
    let xz=document.getElementById('z2').value;
    document.getElementById('outbox').innerHTML=await eel.lalr1parser(zx,xz)();
}

async function Generate(){
    switch(z){
        case(-1):
            GenerateENTER();
            break;
        case (1):
            GenerateLL0();
            break;
        case (2):
            GenerateLL1();
            break;
        case (3):
            GenerateLR0();
            break;
        case (4):
            GenerateLR1();
            break;
        case (5):
            GenerateSLR1();
            break;
        case (6):
            GenerateCLR1();
            break;
        case (7):
            GenerateLALR1();
            break;
    }
}

function setzll0(){
    z=1;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#ll0");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzll1(){
    z=2;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#ll1");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzlr0(){
    z=3;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#lr0");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzlr1(){
    z=4;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#lr1");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzslr1(){
    z=5;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#slr1");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzclr1(){
    z=6;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#clr1");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
function setzlalr1(){
    z=7;
    let q=document.getElementsByClassName(".button3");
    q.style.background= "radial-gradient(circle,rgb(1, 0, 54),rgb(12, 0, 180))";
    q.style.color= "white";
    q=document.querySelector("#lalr1");
    q.style.background="radial-gradient(circle,rgb(12, 0, 180),rgb(1, 0, 54))";
    q.style.color="rgb(0, 255, 0)";
}
