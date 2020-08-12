var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


var about = document.getElementById('about')
var contact = document.getElementById('contact')
var abouttwo = document.getElementById('abouttwo')
var contacttwo = document.getElementById('contacttwo')

var aboutSection = document.getElementById('aboutSection')
var contactSection = document.getElementById('contactSection')

about.addEventListener('click',aboutScroll)
contact.addEventListener('click',contactScroll)
abouttwo.addEventListener('click',aboutScroll)
contacttwo.addEventListener('click',contactScroll)

//Scrolling to the about section
function aboutScroll (e){
  aboutSection.scrollIntoView();
}

//Scrolling to the contact section
function contactScroll (e){
  contactSection.scrollIntoView();
}

//Changing the position of the nav while scrolling
window.onscroll = changePos;

function changePos() {
    var header = document.getElementById("navTwo");
    var nav = document.getElementById("navbartwo");
    //position of navbar1
    if (window.pageYOffset > 500) {
        header.style.position = "absolute";
        header.style.top = pageYOffset + "px";
        
    } else {
        header.style.position = "";
        header.style.top = "";
    }
    //position of navbar2
    if (window.pageYOffset > 550) {
      nav.style.position = "absolute";
      nav.style.top = pageYOffset + "px";
      nav.style.marginTop ="50px"
      nav.style.overflow= "visible"
      
  } else {
      nav.style.position = "";
      nav.style.top = "";
  }
}

//Handling the nav button click
var nav_btn = document.getElementById("dropbtnnav")
nav_btn.addEventListener('click',showDropDown)

function showDropDown(e){
  var x = document.getElementById('navbartwo');
  if (x.style.display === 'none') {
    x.style.display = 'block';
  } else {
    x.style.display = 'none';
  }
}

//removing the second nav by checking the window width
var window_width = window.innerWidth;
function checkWindow(){
  console.log(window_width)
  let nav_two = document.getElementById('navbartwo')
  if (window_width >= 751) {
    nav_two.style.display = 'none';
  }
}
checkWindow()

console.log('heloooooooo world')
