const bookCards = document.querySelectorAll(".card");

const dropdownBTN = document.querySelector(".dropdown-button");
const dropdownOptionsEl = document.querySelector(".dropdown-options");
const dropdownTextEl = document.querySelector(".dropdown-text");
const dropdownOptions = document.querySelectorAll(".option");
const hiddenDropdownSelector = document.getElementById("sortSelector");

dropdownBTN?.addEventListener("click", () => {
  dropdownOptionsEl.classList.toggle("displayed");
  dropdownBTN.classList.toggle("active-btn");

  if (dropdownBTN.classList.contains("active-btn")) {
    dropdownBTN
      .querySelector("img")
      // .setAttribute("src", "./assets/white-arrow.svg");
      .setAttribute("src", "static/assets/white-arrow.svg");
  } else {
    dropdownBTN
      .querySelector("img")
      // .setAttribute("src", "./assets/");
      .setAttribute("src", "static/assets/green-dropdown-icon.svg");
  }
});

dropdownOptions.forEach((option) => {
  option.addEventListener("click", (option) => {
    const selectedOption = option.target.textContent;
    //----
    const value = option.target.getAttribute("data-value");
    hiddenDropdownSelector.value = value;
    //----

    //for ui
    if (value === "year-desc") {
      dropdownTextEl.innerHTML = `<p class="dropdown-text">
                                      გამოცემის წელი <br/> (კლებადი)
                                  </p>`;
    } else if (value === "year-asc") {
      dropdownTextEl.innerHTML = `<p class="dropdown-text">
                                      გამოცემის წელი <br/> (ზრდადი)
                                  </p>`;
    } else {
      dropdownTextEl.textContent = selectedOption;
    }

    dropdownOptionsEl.classList.remove("displayed");
    dropdownBTN.classList.remove("active-btn");
    dropdownBTN
      .querySelector("img")
      .setAttribute("src", "static/assets/green-dropdown-icon.svg");
    // dropdownTextEl.style.fontSize = "18px";
  });
});

window.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);
  const sortedBy = params.get("sortedBy");

  const sortTexts = {
    "year-desc": "გამოცემის წელი <br/> (კლებადი)",
    "year-asc": "გამოცემის წელი <br/> (ზრდადი)",
    "name-asc": "დასახელება (ა-ჰ)",
    "name-desc": "დასახელება (ჰ-ა)",
  };

  if (sortTexts[sortedBy]) {
    dropdownTextEl.innerHTML = `<p class="dropdown-text">${sortTexts[sortedBy]}</p>`;
  }
});

document.querySelector(".burger_menu").addEventListener("click", () => {
  document.querySelector(".burger_menu_dropdown").classList.toggle("open");

  if (
    document.querySelector(".burger_menu_dropdown").classList.contains("open")
  ) {
    document.documentElement.style.overflow = "hidden"; // <html>
    document.body.style.overflow = "hidden"; // <body>
  } else {
    document.documentElement.style.overflow = "";
    document.body.style.overflow = "";
  }
});
