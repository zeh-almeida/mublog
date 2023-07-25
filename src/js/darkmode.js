
const DARKMODE_CLASS_NAME = "darken";
const DARKMODE_TOGGLE = ".dark-toggle";
const DARKMODE_STORAGE_NAME = "enable_darkmode";

function toggle_dark_mode(event) {
	if (!event.target.matches(DARKMODE_TOGGLE)) {
		return;
	}

	const hasClass = document.documentElement.classList.contains(DARKMODE_CLASS_NAME);
	localStorage.setItem(DARKMODE_STORAGE_NAME, !hasClass);

	if (hasClass) {
		document.documentElement.classList.remove(DARKMODE_CLASS_NAME);
	
	} else {
		document.documentElement.classList.add(DARKMODE_CLASS_NAME);
	}
}

function check_dark_mode(event) {
	const isDark = localStorage.getItem(DARKMODE_STORAGE_NAME);

	if (isDark) {
		document.documentElement.classList.add(DARKMODE_CLASS_NAME);
	}
}

document.addEventListener('DOMContentLoaded', check_dark_mode, true);
document.addEventListener('click', toggle_dark_mode, false);