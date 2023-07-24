
function toggle_dark_mode(event) {
	if (!event.target.matches('.dark-toggle')) {
		return;
	}

	const hasClass = document.documentElement.classList.contains('darken');
	localStorage.setItem("enable_darkmode", !hasClass);

	if (hasClass) {
		document.documentElement.classList.remove('darken');
	
	} else {
		document.documentElement.classList.add('darken');
	}
}

function check_dark_mode(event) {
	const isDark = localStorage.getItem("enable_darkmode");

	if(isDark) {
		document.documentElement.classList.add('darken');
	}
}

document.addEventListener('DOMContentLoaded', check_dark_mode);
document.addEventListener('click', toggle_dark_mode, false);