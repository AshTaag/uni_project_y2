const slideshow = document.querySelector(".slideshow");
const slides = slideshow.querySelectorAll(".slide");
let currentIndex = 0;

function slideshowLoop() {
  slides[currentIndex].classList.remove("active");
  currentIndex = (currentIndex + 1) % slides.length;
  slides[currentIndex].classList.add("active");
}

setInterval(slideshowLoop, 3000);

alert("Your application has been successfully submitted!");