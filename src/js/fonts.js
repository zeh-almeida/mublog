const FONT_SELECTOR = "font-selection";
const FONT_SUFFIX = "_font";

function select_font(event) {
  console.log(event.target.value);

  [...document.documentElement.classList]
    .filter((c) => c.endsWith(FONT_SUFFIX))
    .map((c) => document.documentElement.classList.remove(c));

  document.documentElement.classList.add(`${event.target.value}${FONT_SUFFIX}`);
}

document.addEventListener(
  "DOMContentLoaded",
  () => {
    const el = document.getElementById(FONT_SELECTOR);
    el.addEventListener("change", select_font, true);
  },
  true
);
