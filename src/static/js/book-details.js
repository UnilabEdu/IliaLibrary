const anotationBtn = document.getElementById("anotation");
const searchBtn = document.getElementById("search");
const featureBtn = document.getElementById("feature");
const anotationSection = document.querySelector(".anotation-section");
const featureSection = document.querySelector(".feature-section");
const searchingSection = document.querySelector(".searching-section");
const dots = document.querySelectorAll(".dotted-line");

const buttons = [anotationBtn, featureBtn, searchBtn];
buttons[0].classList.add("focused");

buttons.forEach((button, i) => {
  let keys = ["anotation", "feature", "search"];

  button.addEventListener("click", (e) => {
    buttons.forEach((button) => {
      button.classList.remove("focused");
    });

    e.target.classList.add("focused");
    openBookInfo(keys[i]);
  });
});

function openBookInfo(section) {
  [anotationSection, featureSection, searchingSection].forEach((sec) => {
    if (sec.classList.contains("open")) {
      sec.classList.remove("open");
      // sec.style.maxHeight = "0";
      sec.style.opacity = "0";
    }
  });

  if (section === "anotation") {
    anotationSection.classList.add("open");
    // anotationSection.style.maxHeight = anotationSection.scrollHeight + "px";
    anotationSection.style.opacity = "1";
  } else if (section === "feature") {
    featureSection.classList.add("open");
    // featureSection.style.maxHeight = featureSection.scrollHeight + "px";
    featureSection.style.opacity = "1";
  } else if (section === "search") {
    searchingSection.classList.add("open");
    // searchingSection.style.maxHeight = searchingSection.scrollHeight + "px";
    searchingSection.style.opacity = "1";
  }
}

// ---------- Mobile -------------
const mobileAnotationBtn = document.getElementById("mobile-anotation-btn");
const mobileSearchBtn = document.getElementById("mobile-search-btn");
const mobileFeatureBtn = document.getElementById("mobile-feature-btn");
const mobileAnotationSection = document.querySelector(
  ".mobile-anotation-section"
);
const mobileFeatureSection = document.querySelector(".mobile-feature-section");
const mobileSearchingSection = document.querySelector(
  ".mobile-searching-section"
);
const mobileButtons = [mobileAnotationBtn, mobileFeatureBtn, mobileSearchBtn];
mobileButtons[0].classList.add("focused");

mobileButtons.forEach((button, i) => {
  let keys = ["anotation", "feature", "search"];

  button.addEventListener("click", (e) => {
    const key = keys[i];
    let section = null;

    if (key === "anotation") {
      section = mobileAnotationSection;
    } else if (key === "feature") {
      section = mobileFeatureSection;
    } else {
      section = mobileSearchingSection;
    }

    const isOpen = section.classList.contains("open");

    [
      mobileAnotationSection,
      mobileFeatureSection,
      mobileSearchingSection,
    ].forEach((sec) => {
      sec.classList.remove("open");
      // sec.style.maxHeight = "0";
      sec.style.opacity = "0";
    });

    mobileButtons.forEach((btn) => {
      btn.classList.remove("focused");
      btn.querySelector(".dropdown-icon").classList.remove("rotated");
    });

    if (!isOpen) {
      section.classList.add("open");
      // section.style.maxHeight = section.scrollHeight + "px";
      section.style.opacity = "1";

      e.currentTarget.classList.add("focused");
      e.currentTarget.querySelector(".dropdown-icon").classList.add("rotated");
    }
  });
});
