/**
 * Template Name: FlexStart - v1.9.0
 * Template URL: https://bootstrapmade.com/flexstart-bootstrap-startup-template/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */

window.addEventListener("load", () => {
  document.cookie;
  const navLangLi = document.querySelectorAll("#nav_lang_li");

  if (navLangLi?.length) {
    navLangLi.forEach((li) => {
      const img = li.children[0].children[0];
      const lang = img?.getAttribute("data-lang");
      img.setAttribute("src", navLangOptions[lang]);
      const span = li.children[0].children[1];
      span.innerText = lang === "ky" ? "kg" : lang;

      // ТУТ НИЖЕ ЛОВИТЬСЯ КЛИК НА ЯЗЫК
      li.addEventListener("click", () => {
        const liLang = li?.getAttribute("data-lang");
        // ТУТ НИЖЕ SUBMIT
        window.location = `/${liLang}/${window.location.pathname.slice(4)}`;
      });
    });
  }
});

(function () {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    if (all) {
      select(el, all).forEach((e) => e.addEventListener(type, listener));
    } else {
      select(el, all).addEventListener(type, listener);
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select("#navbar .scrollto", true);
  const navbarlinksActive = () => {
    let position = window.scrollY + 200;
    navbarlinks.forEach((navbarlink) => {
      if (!navbarlink.hash) return;
      let section = select(navbarlink.hash);
      if (!section) return;
      if (
        position >= section.offsetTop &&
        position <= section.offsetTop + section.offsetHeight
      ) {
        navbarlink.classList.add("active");
      } else {
        navbarlink.classList.remove("active");
      }
    });
  };
  window.onload = navbarlinksActive();
  onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select("#header");
    let offset = header.offsetHeight;

    if (!header.classList.contains("header-scrolled")) {
      offset -= 10;
    }

    let elementPos = select(el).offsetTop;
    window.scrollTo({
      top: elementPos - offset,
      behavior: "smooth",
    });
  };

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select("#header");
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 25) {
        selectHeader.classList.add("header-scrolled");
      } else {
        selectHeader.classList.remove("header-scrolled");
      }
    };
    window.onload = headerScrolled();
    onscroll(document, headerScrolled);
  }

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.onload = toggleBacktotop();
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {
    select("#navbar").classList.toggle("navbar-mobile");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /**
   * Mobile nav dropdowns activate
   */
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      if (select("#navbar").classList.contains("navbar-mobile")) {
        e.preventDefault();
        this.nextElementSibling.classList.toggle("dropdown-active");
      }
    },
    true
  );

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on(
    "click",
    ".scrollto",
    function (e) {
      if (select(this.hash)) {
        e.preventDefault();

        let navbar = select("#navbar");
        if (navbar.classList.contains("navbar-mobile")) {
          navbar.classList.remove("navbar-mobile");
          let navbarToggle = select(".mobile-nav-toggle");
          navbarToggle.classList.toggle("bi-list");
          navbarToggle.classList.toggle("bi-x");
        }
        scrollto(this.hash);
      }
    },
    true
  );

  /**
   * Scroll with ofset on page load with hash links in the url
   */

  function scrollByHash() {
    console.log("window.location.hash");
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash);
      }
    }
  }

  window.onload = scrollByHash();

  /**
   * News Slider
   */
  new Swiper(".news-detail-slider", {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  /**
   * Main Page Hero Slider
   */
  new Swiper(".mainPageHeroSlider", {
    speed: 400,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      dynamicBullets: true,
    },
    slidesPerView: "auto",
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  /**
   * Animation on scroll
   */
  function aos_init() {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }
  window.onload = aos_init();
})();

// Reclam slider on main page

new Swiper(".reclamSlider", {
  speed: 400,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  slidesPerView: "auto",
  loop: true,
  breakpoints: {
    480: {
      slidesPerView: 1,
      spaceBetween: 15,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

//??? offices_block_slider

new Swiper(".offices_block_swiper", {
  speed: 400,
  autoplay: {
    delay: 3000,
  },
  loop: true,
  slidesPerView: "auto",
  observer: true,
  breakpoints: {
    480: {
      slidesPerView: 1,
      spaceBetween: 15,
    },
    640: {
      slidesPerView: 2,
      spaceBetween: 15,
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 15,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 15,
    },
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

new Swiper(".clients-slider", {
  speed: 600,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
  slidesPerView: "auto",
  pagination: {
    el: ".swiper-pagination",
    type: "bullets",
    clickable: true,
  },
  breakpoints: {
    480: {
      slidesPerView: 1,
      spaceBetween: 15,
    },
    640: {
      slidesPerView: 3,
      spaceBetween: 25,
    },
    992: {
      slidesPerView: 4,
      spaceBetween: 35,
    },
  },
});

const logoEng = document.getElementById("logoEng");
const logoRu = document.getElementById("logoRu");
const logoEng2 = document.getElementById("logoEng2");
const logoRu2 = document.getElementById("logoRu2");

logoEng.style.display = "none";
logoEng2.style.display = "none";
logoRu.style.display = "none";
logoRu2.style.display = "none";
if (window.location.pathname.includes("/en")) {
  logoRu.remove();
  logoRu2.remove();
  logoEng.style.display = "block";
  logoEng2.style.display = "block";
} else {
  logoEng.remove();
  logoEng2.remove();
  logoRu.style.display = "block";
  logoRu2.style.display = "block";
}
