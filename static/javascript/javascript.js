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

// const toggleButton = document.getElementById("toggleButton");
// const body = document.body;
// let isWhitesmoke = true;

// toggleButton.addEventListener("click", function () {
//   if (body.classList.contains("whitesmoke")) {
//     body.classList.remove("whitesmoke");
//     body.classList.add("black");
//     // console.log("white");
//   } else {
//     body.classList.remove("black");
//     body.classList.add("whitesmoke");
//     //console.log("black");
//   }
//   isWhitesmoke = !isWhitesmoke;
// });
