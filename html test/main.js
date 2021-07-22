var curses;
var randint;
var bad_words = ["fuck", "shit", "nightmare", "dick", "aaahhhhhh"];
var body = document.getElementById("body");
randint = Math.random()*bad_words.length;
window.resizeTo(1500, 700);
curses= document.getElementById('swear');
/*curses.textContent = `${curses.textContent} Inner Width, Height: ${this.innerWidth} ${this.innerHeight} Outer Width, Height: ${this.outerWidth} ${this.outerHeight}`;*/
// curses.textContent = `${curses.textContent} ${bad_words[randint]}!!!! KINKLY STEPS ON DIC*`;

function coordinate(cord, divnumber) {
    x = cord[0]*25;
    y=cord[1]*25;
    var i;
    for (i in divs) {
        if (i.divid == divnumber) {
            var element = document.getElementById(i);
            element.style.position = "absolute";
            element.style.left = x.toString() + "px";
            element.style.top = y.toString() + "px";
        }
    };
};
$(document).ready(function() {
    let num = 0;
    while (num < 100) {
    console.log("I'm ready")
    num = num+1
    }
})
class div {
    constructor(direction, coord, divnumber) {
        var divname = `div` + `${divnumber}`;
        this.divelement = document.createElement("div");
        //var newid = document.createAttribute("id");
        //this.divelement.appendChild(newid);
        this.divelement.setAttribute("id", divname);
        this.divid = divname;
        this.cord = coord;
        this.direction = direction;
        this.divnum = divnumber;
        coordinate(this.cord, this.divnum);
        if (divnumber == 0) {
            curses.textContent = `${divnumber}`;
        } else {
            curses.textContent = `${curses.textContent}` + `${divnumber}`;
        };
    }
};
var divlist = {
    "div1":new div("right", [30, 14], 1),
    "div2":new div("right", [29, 13], 2),
    "div3":new div("right", [28, 12], 3),
    "div4":new div("right", [27, 11], 4),
    "div5":new div("right", [26, 10], 5),
};
var x;
var divs=[];
for (x of Object.keys(divlist)) {
    let d = document.getElementById(divlist[x].divid);
    divs.push(divlist[x].divid);
    d.style.position = "absolute";
};
var a;
for (a in divs) {
    var divelement = document.getElementById(a);
    coordinate(divelement.cord, divelement.divnum)
}
/*divlist[divname] = new div(direction, coord, divnumber) Add this later on when creating snake blocks
console.log() is print() in js*/
