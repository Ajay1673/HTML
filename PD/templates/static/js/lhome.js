const myorder = document.getElementById("myorder");
const content = document.querySelector(".content");
const master = document.querySelector(".master");

myorder.addEventListener("click", function () {
  master.style.display = "flex";
  content.style.display = "none";
});

document.querySelector(".trashButn").addEventListener("click", function () {
  master.style.display = "none";
  content.style.display = "flex";
});

const bookord = document.getElementById("bookord");
const book = document.querySelector(".book");
bookord.addEventListener("click", function () {
  book.style.display = "flex";
  content.style.display = "none";
});

document.querySelector(".cancel-btn").addEventListener("click", function () {
  book.style.display = "none";
  content.style.display = "flex";
});
