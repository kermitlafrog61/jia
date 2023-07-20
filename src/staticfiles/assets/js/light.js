//?? NAV LOCALIZATION

const navLangOptions = {
  ky: "https://www.svgrepo.com/show/401669/flag-for-kyrgyzstan.svg",
  ru: "https://www.svgrepo.com/show/401732/flag-for-russia.svg",
  en: "https://www.svgrepo.com/show/401791/flag-for-united-states.svg",
};

function getReadyNavs() {
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
}

window.onload = getReadyNavs();
