const background = document.querySelector("body");

window.addEventListener("load", function () {
  document.body.style.visibility = "visible";
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      } else {
        entry.target.classList.remove("visible");
      }
    });
  },
  { threshold: 0.1 },
);

const items = document.querySelectorAll(".float-item");
items.forEach((item) => observer.observe(item));

setTimeout(() => {
  const lateItems = document.querySelectorAll(
    ".item, .location-content, .rate-container",
  );
  lateItems.forEach((item) => {
    if (!item.isConnected) return;
    observer.observe(item);
  });
}, 500);
//  control plan btns
function firstChoice() {
  window.sessionStorage.setItem("planChoice", "old");
  document.getElementById("oldPlanBtn").classList.add("active-btn");
  document.getElementById("newPlanBtn").classList.remove("active-btn");
  document.querySelector(".oldPlan").classList.add("activePlan");
  document.querySelector(".newPlan").classList.remove("activePlan");
}
function secondChoice() {
  window.sessionStorage.setItem("planChoice", "new");
  document.getElementById("newPlanBtn").classList.add("active-btn");
  document.getElementById("oldPlanBtn").classList.remove("active-btn");
  document.querySelector(".newPlan").classList.add("activePlan");
  document.querySelector(".oldPlan").classList.remove("activePlan");
}

if (
  decodeURIComponent(window.location.href) ===
  `${window.location.origin}/الخطة-الدراسية-لقسم-الترجمة-جامعة-اليرموك`
) {
  document.getElementById("oldPlanBtn").onclick = firstChoice;
  document.getElementById("newPlanBtn").onclick = secondChoice;
  if (window.sessionStorage.getItem("planChoice")) {
    if (window.sessionStorage.getItem("planChoice") === "old") {
      firstChoice();
    } else {
      secondChoice();
    }
  }
}
