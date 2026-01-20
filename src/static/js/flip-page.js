pdfjsLib.GlobalWorkerOptions.workerSrc =
  "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.10.377/pdf.worker.min.js";

const state = {
  bookContainer: null,
  loader: null,
  main: null,
  totalPages: null,
  currentPageElement: null,
  totalPagesElement: null,
  totalPagesElementMobile: null,
  pageFlip: null,
  currentPage: 0,
  bookId: (() => {
    const match = window.location.pathname.match(/\/read_book\/(\d+)/);
    return match ? parseInt(match[1], 10) : null;
  })(),
  isAnimating: false,
  isMobile: window.innerWidth <= 428,
  isSmallScreen: window.innerWidth <= 1060,
};

// Initialize DOM elements
function initializeElements() {
  state.bookContainer = document.getElementById("pdf-container");
  state.loader = document.getElementById("loader");
  state.main = document.getElementById("main");
  state.currentPageElement = state.isMobile
    ? document.getElementById("current-page-mobile")
    : state.isSmallScreen
      ? document.querySelector(".current-page-tablet")
      : document.querySelector(".current-page");
  state.totalPagesElement = state.isSmallScreen
    ? document.querySelector(".tablet-total-pages")
    : document.getElementById("total-pages");
  state.totalPagesElementMobile = document.getElementById("total-pages-mobile");
  state.flipHeader = document.getElementById("flip-page-header");
}

async function loadVisiblePages(pdf, currentPage) {
  const pagesToLoad = !state.isSmallScreen
    ? [
        currentPage - 2,
        currentPage - 1,
        currentPage,
        currentPage + 1,
        currentPage + 2,
        currentPage + 3,
        currentPage + 4,
        currentPage + 5,
      ]
    : [currentPage - 1, currentPage, currentPage + 1, currentPage + 2];

  const pageElements = document.querySelectorAll(".my-page");

  for (const el of pageElements) {
    const pageNum = parseInt(el.dataset.pageNum);

    // Load only if not already loaded
    if (pagesToLoad.includes(pageNum) && el.childNodes.length === 0) {
      const img = await createPage(pdf, pageNum);
      el.appendChild(img);
    }

    //removing old pages
    // if (!pagesToLoad.includes(pageNum) && el.childNodes.length > 0) {
    //   el.innerHTML = ""; // Clear to free memory
    // }
  }
}

// Optimized page creation with proper cleanup
async function createPage(pdf, pageNum) {
  const page = await pdf.getPage(pageNum);
  const scale = state.isSmallScreen ? 4 : 3;
  const viewport = page.getViewport({ scale });

  const canvas = document.createElement("canvas");
  const context = canvas.getContext("2d", { alpha: false }); // Optimize canvas

  canvas.width = viewport.width;
  canvas.height = viewport.height;

  const pageContainer = document.createElement("div");
  await page.render({
    canvasContext: context,
    viewport: viewport,
    intent: "display",
  }).promise;

  const img = new Image();
  return new Promise((resolve) => {
    img.onload = () => {
      if (pageNum === 1) {
        img.style.width = "100%";
        img.style.height = "100%";
      } else {
        img.style.width = "100%";
        img.style.height = state.isSmallScreen ? "90%" : "100%"; //temp number
      }
      pageContainer.appendChild(img);
      canvas.remove();
      resolve(pageContainer);
    };
    img.src = canvas.toDataURL("image/png");
  });
}

async function setupPages(pdf) {
  const numPages = pdf.numPages;
  state.totalPages = numPages;
  state.totalPagesElement.innerText = numPages - 1;
  state.totalPagesElementMobile.innerText = numPages - 1;

  // Create empty page containers
  for (let i = 1; i <= numPages; i++) {
    const pageContainer = document.createElement("div");
    pageContainer.className = "my-page";
    pageContainer.dataset.pageNum = i; // for tracking
    state.bookContainer.appendChild(pageContainer);
  }

  await loadVisiblePages(pdf, 1);

  // Init PageFlip
  state.pageFlip.loadFromHTML(document.querySelectorAll(".my-page"));
  state.pageFlip.flip(0, true);

  // Add lazy loading for future pages
  state.pageFlip.on("flip", async () => {
    await loadVisiblePages(pdf, state.currentPage + 1);
    await loadVisiblePages(pdf, state.currentPage - 1);
  });
}

function changeChapterHeaderText(page, obj) {
  const chapterTitle = state.isSmallScreen
    ? document.getElementById("main-chapter-small-screen")
    : document.getElementById("main-chapter");

  if (page === 0) {
    chapterTitle.textContent = `ყდა`;
    return;
  }

  const headerFromPageMap = obj[page];
  if (headerFromPageMap) {
    chapterTitle.textContent = `${bookTitle} - ${headerFromPageMap}`;
    return;
  }

  // closest preceding chapter
  const chapterHeader = Object.entries(obj)
    .reverse()
    .find(([chapterPage]) => Number(chapterPage) <= page)?.[1];

  if (chapterHeader) {
    chapterHeader !== "ყდა"
      ? (chapterTitle.textContent = `${bookTitle} - ${chapterHeader}`)
      : (chapterTitle.textContent = `ყდა`);
  }
}

function setupNavigation() {
  const nextBtn = state.isSmallScreen
    ? document.getElementById("tablet-next")
    : document.getElementById("next");
  const nextBtnMobile = document.getElementById("next-mobile");
  const prevBtn = state.isSmallScreen
    ? document.getElementById("tablet-prev")
    : document.getElementById("prev");
  const prevBtnMobile = document.getElementById("prev-mobile");

  const handleNext = () => {
    if (state.isSmallScreen) {
      state.pageFlip.flip(state.currentPage + 1, true);
      changeChapterHeaderText(state.currentPage + 1, pageToChapter);
    } else {
      state.pageFlip.flip(state.currentPage + 2, true);
      changeChapterHeaderText(state.currentPage + 2, pageToChapter);
    }
  };

  const handlePrev = () => {
    if (state.isSmallScreen) {
      state.pageFlip.flip(state.currentPage - 1, true);
      changeChapterHeaderText(state.currentPage - 1, pageToChapter);
    } else {
      state.pageFlip.flip(state.currentPage - 2, true);
      changeChapterHeaderText(state.currentPage - 2, pageToChapter);
    }
  };

  function updatePageCountUI() {
    if (state.currentPage === 0) {
      // state.isSmallScreen
      state.isMobile
        ? (state.currentPageElement.textContent = 0)
        : (state.currentPageElement.value = 0);
      return;
    }

    if (state.currentPage === state.totalPages - 1 && !state.isSmallScreen) {
      state.currentPageElement.value = state.currentPage;
    } //edge case

    if (state.isMobile) {
      state.currentPageElement.textContent = state.currentPage;
    } else {
      state.currentPageElement.value = state.currentPage;
    }
  }

  nextBtn.addEventListener("click", handleNext, { passive: true });
  nextBtnMobile.addEventListener("click", handleNext, { passive: true });
  prevBtn.addEventListener("click", handlePrev, { passive: true });
  prevBtnMobile.addEventListener("click", handlePrev, { passive: true });

  state.pageFlip.on("flip", (event) => {
    state.currentPage = event.data;

    updatePageCountUI();

    if (state.isSmallScreen) {
      changeChapterHeaderText(event.data, pageToChapter);
    }

    localStorage.setItem(
      "lastRead",
      JSON.stringify({ bookId: state.bookId, page: state.currentPage }),
    );
  });
}

function setupChapterMenu() {
  const menu = document.getElementById("menu");
  let menuList = null;

  function createChapterList() {
    const ul = document.createElement("ul");
    ul.className = "menu-ul";
    ul.style.display = "none";
    const chapters = Object.values(pageToChapter).length; // Total number of chapters + დასაწყისი
    Array.from({ length: chapters }, (_, i) => {
      const li = document.createElement("li");
      li.className = "menu-li";

      li.textContent = Object.values(pageToChapter)[i];

      li.addEventListener("click", () => changeChapter(li, i, ul), {
        passive: true,
      });

      ul.appendChild(li);
    });

    return ul;
  }

  menu.addEventListener(
    "click",
    () => {
      if (!menuList) {
        menuList = createChapterList();
        menu.parentElement.appendChild(menuList);
      }
      menuList.style.display =
        menuList.style.display === "none" ? "block" : "none";
    },
    { passive: true },
  );
}

async function changeChapter(chapter, index, ul) {
  // const chapterTitle = document.getElementById("main-chapter");
  const chapterName = chapter.textContent.trim().toLowerCase();
  // chapterTitle.textContent = `${bookTitle} - ${chapterName}`;

  const active = ul.querySelector(".menu-li.hover");

  const entry = Object.entries(pageToChapter).find(
    ([, name]) => name.trim().toLowerCase() === chapterName,
  );

  let targetPage = entry ? Number(entry[0]) : undefined;

  if (active && active !== chapter) {
    active.classList.remove("hover");
  }
  chapter.classList.toggle("hover");

  ul.style.display = "none";

  if (!state.isAnimating) {
    if (targetPage === undefined) {
      state.pageFlip.flip(0, true);
    }
    if (targetPage !== undefined) {
      state.currentPage = targetPage;
      // state.currentPageElement.innerText = state.currentPage;
      state.pageFlip.flip(state.currentPage, true);
    } else {
      console.error("Chapter-to-page mapping is missing for chapter:", index);
    }
  }

  changeChapterHeaderText(state.currentPage, pageToChapter);
}

// -------------------------
window.addEventListener("DOMContentLoaded", function () {
  document.querySelector(".current-page").value = state.currentPage;
});

window.addEventListener("keydown", (e) => {
  if (state.isSmallScreen) return;

  if (e.key === "ArrowRight") {
    state.pageFlip.flip(state.currentPage + 2, true);
    changeChapterHeaderText(state.currentPage + 2, pageToChapter);
  }
  if (e.key === "ArrowLeft") {
    state.pageFlip.flip(state.currentPage - 2, true);
    changeChapterHeaderText(state.currentPage - 2, pageToChapter);
  }
});

function getPageInput() {
  const maxPage = state.totalPages;
  const inputValue = this.value.trim();

  if (!/^\d+$/.test(inputValue)) {
    alert("გთოვთ შეიყვანეთ რიცხვი");
    this.value = state.currentPage;
    return;
  }
  const inputPage = parseInt(inputValue, 10);

  if (inputPage < 0 || inputPage >= maxPage) {
    alert(`გვერდი უნდა იყოს 0-სა და ${maxPage - 1}-ს შორის`);
    this.value = state.currentPage;
    return;
  }
  state.pageFlip.flip(inputPage, true);

  // if (inputPage % 2 === 0)
  //   document.querySelector(".current-page").value = inputPage;
}

state.isSmallScreen
  ? document
      .querySelector(".current-page-tablet")
      .addEventListener("change", getPageInput)
  : document
      .querySelector(".current-page")
      .addEventListener("change", getPageInput);

// -------------------------

function showLoader() {
  state.loader.style.display = "flex";
  state.main.style.display = "none";
  state.flipHeader.style.display = "none";
}

function hideLoader() {
  state.loader.style.display = "none";
  state.main.style.display = "block";
  state.flipHeader.style.display = "flex";
  state.bookContainer.style.visibility = "visible";
}

// Main initialization function with performance optimizations
async function initializeViewer(pdfUrl) {
  try {
    initializeElements();
    showLoader();

    function getScreenDimensions(ratio = 3 / 4) {
      const parsePx = (val) => parseFloat(val) || 0;

      const headerEl = document.querySelector(".flip-page-header");
      const chapterEl = document.querySelector(".main-chapter");
      const mainContentEl = document.querySelector("#main-content");

      const headerStyles = window.getComputedStyle(headerEl);
      const mainContentStyles = window.getComputedStyle(mainContentEl);

      const headerHeight = parsePx(headerStyles.height);
      const contentPaddingTop = parsePx(mainContentStyles.paddingTop);

      let chapterHeight = 0;

      if (chapterEl) {
        const chapterStyles = window.getComputedStyle(chapterEl);

        if (chapterStyles.display !== "none") {
          chapterHeight =
            parsePx(chapterStyles.marginTop) +
            parsePx(chapterStyles.lineHeight) +
            parsePx(chapterStyles.marginBottom);
        }
      }

      let maxWidth = !state.isSmallScreen
        ? window.innerWidth * 0.5 - 8
        : window.innerWidth; // bit of padding 4 & 8 are just bit of padding

      let height = maxWidth / ratio;

      let size;

      if (maxWidth >= 860) size = "xlarge";
      else if (maxWidth >= 770) size = "large";
      else if (maxWidth >= 700) size = "medium";
      else if (maxWidth >= 635) size = "small";
      else if (maxWidth >= 550) size = "xsmall";
      else if (maxWidth <= 550) size = "xxsmall";

      const heightToConsider =
        headerHeight + chapterHeight + contentPaddingTop * 2;

      const maxHeight =
        size === "xxsmall" ? 500 : window.innerHeight - heightToConsider;

      if (height > maxHeight) {
        //big screen case
        height = maxHeight;
        maxWidth = height * ratio;
      }

      return { maxHeight, maxWidth, size, heightToConsider };
    }

    const { maxHeight, maxWidth, size, heightToConsider } =
      getScreenDimensions();

    function assignWidth() {
      if (state.isMobile) return maxWidth - 12;

      //tablet cases
      if (state.isSmallScreen) {
        console.log(size, maxWidth >= 550);
        switch (size) {
          case "xlarge":
            return 690;
          case "large":
            return 670;
          case "medium":
            return 580;
          case "small":
            return 540;
          case "xsmall":
            return 490;
          case "xxsmall":
            return 410;
        }
      }

      return maxWidth;
    }

    // Initialize PageFlip with optimized settings
    state.pageFlip = new St.PageFlip(state.bookContainer, {
      // width: state.isMobile ? (width <= 170 ? 318 : 360) : width,
      width: assignWidth(),

      showCover: true,
      drawShadow: true,
      flippingTime: 600, // Reduced flip animation time
      usePortrait: state.isSmallScreen,
      startZIndex: 0,
      // height: state.isSmallScreen ? height * 1.8 : height, //v.0
      height: window.innerHeight - heightToConsider, //v.1
      // height: maxHeight, // v1.1

      useMouseEvents: true,
      // useMouseEvents: !state.isMobile,
      swipeDistance: !state.isSmallScreen ? 30 : 100,
      preventTouchEvents: false,
    });

    const pdf = await pdfjsLib.getDocument(pdfUrl).promise;
    await setupPages(pdf);
    setupNavigation();
    setupChapterMenu();
    hideLoader();

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams) {
      const page = parseInt(urlParams.get("page"));
      state.pageFlip.flip(page, true);
    }

    //see if read
    const lastRead = JSON.parse(localStorage.getItem("lastRead"));
    if (lastRead.bookId === state.bookId) {
      state.pageFlip.flip(lastRead.page);
      state.currentPage = lastRead.page;
    }

    changeChapterHeaderText(state.currentPage, pageToChapter);
  } catch (error) {
    console.error("Error initializing book viewer:", error);
    hideLoader();
  }
}

// if (typeof pdfjsLib !== "undefined") {
//   const pdfPath = "/static/book/gandegili-1957.pdf";

//   initializeViewer(window.location.origin + pdfPath);
// } else {
//   console.error("PDF.js is not available");
// }

// ------ zoom ----------
const zoomInBTN = document.getElementById("zoom_in");
const zoomOutBTN = document.getElementById("zoom_out");
let zoomLevel = 1;

function updateZoom() {
  zoomLevel > 1
    ? (document.getElementById("main-content").style.overflowY = "scroll")
    : (document.getElementById("main-content").style.overflow = "hidden");

  document.querySelector(".stf__block").style.transform = `scale(${zoomLevel})`;

  document.querySelector(".stf__block").style.transformOrigin = "top center";
}

zoomInBTN.addEventListener("click", () => {
  if (zoomLevel >= 1.15) return;

  zoomLevel += 0.05;
  updateZoom();
});
zoomOutBTN.addEventListener("click", () => {
  if (zoomLevel <= 0.85) return;

  zoomLevel -= 0.05;
  updateZoom();
});
