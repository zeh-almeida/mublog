
const LANG_TARGET = ".language-button";

function go_to_lang(event) {
	if (!event.target.matches(LANG_TARGET)) {
		return;
	}

    const link = event.target.dataset.link;
	window.location.href = `${window.location.origin}${link}`;
}

document.addEventListener('click', go_to_lang, false);