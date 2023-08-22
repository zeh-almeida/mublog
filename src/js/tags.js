const POST_CLASS_SELECTOR = '.post-item';

function get_tag_parameter() {
	const urlParams = new URLSearchParams(window.location.search);
	const tag = urlParams.get('tag');
   
	if (!tag) {
        return;
	}

    const posts = document.querySelectorAll(POST_CLASS_SELECTOR);

    for (const post of posts) {
        const tags = JSON.parse(post.dataset.tags);

        if (!tags.includes(tag)) {
            post.style.display = 'none';
        }
    }
}

document.addEventListener('DOMContentLoaded', get_tag_parameter, true);
