"use strict";

console.log("Hello World");

// document.querySelector(".btn-link").addEventListener("click", () => {
//   console.log("Helloooooo");
// });

$(".btn-link").click(() => {
  window.location = "/home";
});
