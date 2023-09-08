const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
}

const navLink = document.querySelectorAll(".nav-link");

navLink.forEach((n) => n.addEventListener("click", closeMenu));

function closeMenu() {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}

const toggleButton = document.getElementById("toggleButton");
const body = document.body;
const image = document.getElementById("image");
let isWhitesmoke = true;

toggleButton.addEventListener("click", function () {
  if (body.classList.contains("whitesmoke-bg")) {
    body.classList.remove("whitesmoke-bg");
    body.classList.add("black-bg");
    console.log("white");
    image.src = "../static/image/black.png"; // Change to the black-themed image
  } else {
    body.classList.remove("black-bg");
    body.classList.add("whitesmoke-bg");
    console.log("black");
    image.src = "../static/image/jump_girl.jpeg"; // Change back to the default image
  }
  isWhitesmoke = !isWhitesmoke;
});
