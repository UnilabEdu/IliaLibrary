pdfjsLib.GlobalWorkerOptions.workerSrc =
  "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.10.377/pdf.worker.min.js";

const state = {
  bookContainer: null,
  loader: null,
  main: null,
  totalPages: null,
  currentPageElement: null,
  currentPageElementMobile: null,
  totalPagesElement: null,
  totalPagesElementMobile: null,
  pageFlip: null,
  currentPage: 0,
  isAnimating: false,
  isMobile: window.innerWidth <= 390,
};

// Initialize DOM elements
function initializeElements() {
  state.bookContainer = document.getElementById("pdf-container");
  state.loader = document.getElementById("loader");
  state.main = document.getElementById("main");
  state.currentPageElement = document.getElementById("current-page");
  state.currentPageElementMobile = document.getElementById(
    "current-page-mobile"
  );
  state.totalPagesElement = document.getElementById("total-pages");
  state.totalPagesElementMobile = document.getElementById("total-pages-mobile");
  state.flipHeader = document.getElementById("flip-page-header");
}

async function loadVisiblePages(pdf, currentPage) {
  const pagesToLoad = [
    currentPage - 3,
    currentPage - 2,
    currentPage - 1,
    currentPage,
    currentPage + 1,
    currentPage + 2,
    currentPage + 3,
  ];

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
  const scale = state.isMobile ? 4 : 3;
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
        img.style.height = state.isMobile ? "85%" : "100%"; //temp number
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

  // Load only the first 2 pages
  await loadVisiblePages(pdf, 1);

  // Init PageFlip
  state.pageFlip.loadFromHTML(document.querySelectorAll(".my-page"));
  state.pageFlip.flip(0);

  // Add lazy loading for future pages
  state.pageFlip.on("flip", async () => {
    await loadVisiblePages(pdf, state.currentPage + 3);
    await loadVisiblePages(pdf, state.currentPage - 2);
    document.querySelector(".current-page").value = state.currentPage;
  });
}

function changeChapterHeaderText(page, obj) {
  const chapterHeader = Object.entries(obj)
    .reverse()
    .find(([k, v]) => k <= page)?.[1];

  const chapterTitle = document.getElementById("main-chapter");
  chapterHeader
    ? (chapterTitle.textContent = chapterHeader)
    : (chapterTitle.textContent = "დასაწყისი");
}

function setupNavigation() {
  const nextBtn = document.getElementById("next");
  const nextBtnMobile = document.getElementById("next-mobile");
  const prevBtn = document.getElementById("prev");
  const prevBtnMobile = document.getElementById("prev-mobile");

  const handleNext = () => {
    const totalPages = state.pageFlip.getPageCount();
    const isLastPage = state.currentPage > totalPages - 1;

    if (isLastPage) return;

    if (state.isMobile) {
      state.currentPage += 1;
    } else {
      state.currentPage += 2;
    }

    state.pageFlip.flip(state.currentPage);
    changeChapterHeaderText(state.currentPage, pageToChapter);
    // updatePageCountUI();
  };

  const handlePrev = () => {
    if (state.currentPage <= 0) return;

    if (!state.isMobile) {
      state.currentPage = Math.max(0, state.currentPage - 2);
    } else {
      state.currentPage = Math.max(0, state.currentPage - 1);
    }

    state.pageFlip.flip(state.currentPage);
    changeChapterHeaderText(state.currentPage, pageToChapter);
    // updatePageCountUI();
  };

  function updatePageCountUI() {
    state.currentPageElement.innerText = state.currentPage;
    state.currentPageElementMobile.innerText = state.currentPage;

    document.querySelector(".current-page").value = state.currentPage;
  }

  nextBtn.addEventListener("click", handleNext, { passive: true });
  nextBtnMobile.addEventListener("click", handleNext, { passive: true });
  prevBtn.addEventListener("click", handlePrev, { passive: true });
  prevBtnMobile.addEventListener("click", handlePrev, { passive: true });

  state.pageFlip.on("flip", (event) => {
    state.currentPage = event.data;

    changeChapterHeaderText(state.currentPage, pageToChapter);
    updatePageCountUI();
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

      if (i === 0) {
        li.textContent = "დასაწყისი";
      } else {
        li.textContent = Object.values(pageToChapter)[i];
      }

      li.addEventListener("click", () => changeChapter(li, i, ul), {
        passive: true,
      });
      li.addEventListener("touchstart", () => changeChapter(li, i, ul), {
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
    { passive: true }
  );

  // menu.addEventListener(
  //   "touchstart",
  //   () => {
  //     if (!menuList) {
  //       menuList = createChapterList();
  //       menu.parentElement.appendChild(menuList);
  //     }
  //     menuList.style.display =
  //       menuList.style.display === "none" ? "block" : "none";
  //   },
  //   { passive: true }
  // );
}

async function changeChapter(chapter, index, ul) {
  const chapterTitle = document.getElementById("main-chapter");
  chapterTitle.textContent = chapter.textContent;

  const active = ul.querySelector(".menu-li.hover");
  if (active && active !== chapter) {
    active.classList.remove("hover");
  }
  chapter.classList.toggle("hover");

  ul.style.display = "none";

  if (!state.isAnimating) {
    const targetPage = Object.values(indexToPage)[index];

    if (targetPage === undefined) {
      state.pageFlip.flip(0, true);
    }
    if (targetPage !== undefined) {
      state.currentPage = targetPage;
      state.currentPageElement.innerText = state.currentPage;
      state.currentPageElementMobile.innerText = state.currentPage;
      state.pageFlip.flip(state.currentPage, true);
    } else {
      console.error("Chapter-to-page mapping is missing for chapter:", index);
    }
  }
}

// -------------------------
document.querySelector(".current-page").addEventListener("change", function () {
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

  state.currentPage = inputPage;
  state.pageFlip.flip(inputPage, true);
  changeChapterHeaderText(state.currentPage, pageToChapter);
});
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

    // Initialize PageFlip with optimized settings
    state.pageFlip = new St.PageFlip(state.bookContainer, {
      width: state.isMobile ? 352 : 600,
      showCover: true,
      drawShadow: true,
      flippingTime: 600, // Reduced flip animation time
      usePortrait: state.isMobile,
      startZIndex: 0,
      minWidth: 300,
      height: !state.isMobile ? window.innerHeight - 250 : 1000,
      maxWidth: 1000,
      useMouseEvents: true,
      swipeDistance: 30,
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
      state.pageFlip.flip(page);
    }
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
    ? (document.getElementById("pdf-container").style.overflow = "scroll")
    : (document.getElementById("pdf-container").style.overflow = null);

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
