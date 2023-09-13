const FONT_SELECTOR = "font-selection";
const FONT_SUFFIX = "_font";
const FONT_STORAGE_NAME = "selected-font";

function set_current_font(fontName) {
  if (!fontName) {
    return;
  }

  [...document.documentElement.classList]
    .filter((c) => c.endsWith(FONT_SUFFIX))
    .map((c) => document.documentElement.classList.remove(c));

  document.documentElement.classList.add(`${fontName}${FONT_SUFFIX}`);
  localStorage.setItem(FONT_STORAGE_NAME, fontName);
}

function select_font(event) {
  set_current_font(event.target.value);
}

function check_font_selection() {
  const fontName = localStorage.getItem(FONT_STORAGE_NAME);
  set_current_font(fontName);
}

document.addEventListener(
  "DOMContentLoaded",
  () => {
    const el = document.getElementById(FONT_SELECTOR);
    el.addEventListener("change", select_font, true);
  },
  true
);

document.addEventListener("DOMContentLoaded", check_font_selection, true);
