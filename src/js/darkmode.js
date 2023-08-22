const DARKMODE_CLASS_NAME = "dark";
const LIGHTMODE_CLASS_NAME = "light";
const DARKMODE_TOGGLE = ".dark-toggle";
const DARKMODE_STORAGE_NAME = "enable_darkmode";

function toggle_dark_mode(event) {
  const hasClass =
    document.documentElement.classList.contains(DARKMODE_CLASS_NAME);

  localStorage.setItem(DARKMODE_STORAGE_NAME, !hasClass);

  document.documentElement.classList.toggle(LIGHTMODE_CLASS_NAME);
  document.documentElement.classList.toggle(DARKMODE_CLASS_NAME);
}

function check_dark_mode(event) {
  const isDark = localStorage.getItem(DARKMODE_STORAGE_NAME);

  if (isDark) {
    document.documentElement.classList.remove(LIGHTMODE_CLASS_NAME);
    document.documentElement.classList.add(DARKMODE_CLASS_NAME);

  } else {
    document.documentElement.classList.add(LIGHTMODE_CLASS_NAME);
    document.documentElement.classList.remove(DARKMODE_CLASS_NAME);
  }

  const toggles = document.querySelectorAll(DARKMODE_TOGGLE);
  toggles.forEach(el => el.addEventListener('click', toggle_dark_mode, false));
}

document.addEventListener("DOMContentLoaded", check_dark_mode, true);
