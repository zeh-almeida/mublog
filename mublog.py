import configparser
import email.utils
import glob
import logging
import os
import time
import shutil
import subprocess
import re
import html
import urllib.parse
import uuid
from datetime import datetime
from string import Template
from urllib.parse import urljoin

import minify_html

class PathConfig:
    def __init__(self):
        # Define each individual directory name
        self.dst_dir_name = "dst"
        self.src_dir_name = "src"
        self.post_dir_name = "posts"
        self.page_dir_name = "pages"
        self.assets_dir_name = "assets"
        self.files_dir_name = "files"
        self.meta_dir_name = "meta"
        self.js_dir_name = "js"
        self.css_dir_name = "css"
        self.templates_dir_name = "templates"

        # Construct local src directory paths
        self.src_dir_path = self.src_dir_name
        self.src_page_dir_path = os.path.join(self.src_dir_path, self.page_dir_name)
        self.src_posts_dir_path = os.path.join(self.src_dir_path, self.post_dir_name)
        self.src_assets_dir_path = os.path.join(self.src_dir_path, self.assets_dir_name)
        self.src_files_dir_path = os.path.join(self.src_assets_dir_path, self.files_dir_name)
        self.src_meta_dir_path = os.path.join(self.src_dir_path, self.meta_dir_name)
        self.src_css_dir_path = os.path.join(self.src_dir_path, self.css_dir_name)
        self.src_js_dir_path = os.path.join(self.src_dir_path, self.js_dir_name)
        self.src_templates_dir_path = os.path.join(self.src_dir_path, self.templates_dir_name)

        # Construct local dst directory paths
        self.dst_dir_path = self.dst_dir_name
        self.dst_posts_dir_path = os.path.join(self.dst_dir_path, self.post_dir_name)
        self.dst_assets_dir_path = os.path.join(self.dst_dir_path, self.assets_dir_name)
        self.dst_files_dir_path = os.path.join(self.dst_assets_dir_path, self.files_dir_name)
        self.dst_meta_dir_path = os.path.join(self.dst_dir_path, self.meta_dir_name)
        self.dst_css_dir_path = os.path.join(self.dst_dir_path, self.css_dir_name)
        self.dst_js_dir_path = os.path.join(self.dst_dir_path, self.js_dir_name)

    def language_source(self, language_key: str) -> str:
        return os.path.join(self.src_page_dir_path, language_key)


class BlogConfig:
    def __init__(self):
        self.blog_url = ""
        self.blog_title = ""
        self.blog_description = ""
        self.blog_author_name = ""
        self.blog_author_mail = ""
        self.blog_author_contact = ""
        self.post_ignore_prefix = ""
        self.blog_author_copyright = ""

        self.preferred_language = ""
        self.available_languages: list[str] = []

        self.blog_title = ""
        self.blog_description = ""
        self.label_about = ""
        self.label_article = ""
        self.label_home = ""
        self.label_mail = ""
        self.label_tags = ""
        self.label_rss = ""
        self.label_dark_mode = ""
        self.label_contact = ""

        self.blog_version = uuid.uuid4().hex


class LogFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: "\033[34m[*]\033[0m %(message)s",
        logging.INFO: "\033[32m[+]\033[0m %(message)s",
        logging.WARNING: "\033[33m[!]\033[0m %(message)s",
        logging.ERROR: "\033[31m[x]\033[0m %(message)s",
        logging.CRITICAL: "\033[31m[x]\033[0m %(message)s",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Helper:

    @staticmethod
    def pandoc_md_to_html(src_path: str) -> str:
        """
        Convert a markdown file to html using pandoc
        :param src_path: The path to the markdown file
        :return: The html content of the markdown file
        """
        command = [
            "pandoc",
            src_path,
            "--no-highlight",
            "-f",
            "markdown+markdown_in_html_blocks",
            "-t",
            "html"]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8")
            return result.stdout
        except subprocess.CalledProcessError as ex:
            logger.error(f"Pandoc failed while processing {src_path}: {ex.stderr}")
            exit(1)

    @staticmethod
    def strip_top_directory_in_path(path: str) -> str:
        """
        Strip the top directory in a path
        :param path: The path to strip
        :return: The stripped path
        """
        parts = path.split(os.sep)
        return "/".join(parts[1:]) if len(parts) > 1 else path

    @staticmethod
    def copy_files(src_path: str, dst_path: str) -> None:
        """
        Copy all files from a source directory to a destination directory
        :param src_path: The source directory
        :param dst_path: The destination directory
        """
        try:
            for f in glob.glob(f"{src_path}/*"):
                if os.path.isfile(f):
                    shutil.copy(f, dst_path)
        except Exception as e:
            logger.error(f"Failed to copy files: {str(e)}")
            exit(1)

    @staticmethod
    def post_src_to_dst_path(src_file_path: str, dst_dir: str, dst_ext: str) -> str:
        """
        Convert a source file path to a destination file path by joining the destination directory with the
        filename and the destination extension.
        :param src_file_path: The source file path
        :param dst_dir: The destination directory
        :param dst_ext: The destination extension
        :return: The converted destination file path as a string
        """
        file_name = os.path.basename(src_file_path)
        base_name, _ = os.path.splitext(file_name)
        return os.path.join(dst_dir, base_name + dst_ext)

    @staticmethod
    def replace_relative_url_with_abs_url(match: re.Match, base_url: str, folder_name: str) -> str:
        """
        Converts a relative url to an absolute url, prefixed with the base url
        :param match: The match object
        :param base_url: The base url which the other urls come from
        :param folder_name: The name of the folder which sits between the base url and the partial
        :return: The absolute url, prefixed with the base url
        """
        if match.group(1).startswith('/'):
            return urljoin(base_url, match.group(1).lstrip('/'))
        elif match.group(1).startswith('../'):
            return urljoin(base_url, match.group(1))
        else:
            return urljoin(base_url, urljoin(folder_name, match.group(1)))

    @staticmethod
    def make_urls_absolute(content: str, base_url: str, folder_name: str) -> str:
        """
        Converts all relative urls in the content to absolute urls, prefixed with the blog url
        :param content: The content in which to convert the urls
        :param base_url: The base url which the other urls come from
        :param folder_name: The name of the folder which sits between the base url and the partial
        :return: The content with all relative urls converted to absolute urls
        """
        if not content:
            return ""

        regex_pattern = r'''(?:url\(|<(?:link|a|script|img)[^>]+(?:src|href)\s*=\s*)(?!['"]?(?:data|http|https))['"]?([^'"\)\s>#]+)'''
        return re.sub(regex_pattern, lambda match: Helper.replace_relative_url_with_abs_url(match, base_url, folder_name), content)

    @staticmethod
    def build_language_selector(config: BlogConfig) -> str:
        options = []

        for lang in config.available_languages:
            options.append(f'<a class="tag-bubble" href="/{lang}/index.html" title="{lang}"><span class="fi fi-{lang[-2:]}"></span>{lang}</a>')

        return "".join(options)

    @staticmethod
    def common_substitutions(config: BlogConfig, paths: PathConfig) -> dict[str, str]:
        """
        Maps common substitutions in blog templates
        :return: Map of known substitutions to make in templates
        """
        return {
            "blog_url": config.blog_url,
            "blog_title": config.blog_title,
            "blog_version": config.blog_version,
            "blog_description": config.blog_description,

            "author_name": config.blog_author_name,
            "author_mail": config.blog_author_mail,
            "author_contact": config.blog_author_contact,
            "label_contact": config.label_contact,
            "author_copyright": config.blog_author_copyright,

            "label_about": config.label_about,
            "label_article": config.label_article,
            "label_home": config.label_home,
            "label_mail": config.label_mail,
            "label_tags": config.label_tags,
            "label_rss": config.label_rss,
            "label_dark_mode": config.label_dark_mode,
            "label_contact": config.label_contact,

            "languages": Helper.build_language_selector(config),

            "js_dir": Helper.strip_top_directory_in_path(paths.dst_js_dir_path),
            "css_dir": Helper.strip_top_directory_in_path(paths.dst_css_dir_path),
            "meta_dir": Helper.strip_top_directory_in_path(paths.dst_meta_dir_path),
            "assets_dir": Helper.strip_top_directory_in_path(paths.dst_assets_dir_path),
        }


class Page:

    def __init__(self, config: BlogConfig, paths: PathConfig, current_lang: str, src_page_path: str, template: str="page.html.template"):
        self.config = config
        self.paths = paths
        self.template = template
        self.current_lang = current_lang

        self.html_content = ""

        self.title = ""
        self.description = ""
        self.date = ""
        self.modified = ""
        self.tags: list[str] = []

        self.src_path = src_page_path
        self.dst_path = Helper.post_src_to_dst_path(src_page_path, os.path.join(self.paths.dst_dir_path, self.current_lang), ".html")
        self.remote_path = Helper.strip_top_directory_in_path(self.dst_path)
        self.file_name = os.path.basename(src_page_path).split('.')[0]

    def load_template(self) -> str:
        with open(os.path.join(self.paths.src_templates_dir_path, self.template), mode="r", encoding="utf-8") as f:
            page_template = f.read()

        return page_template

    def page_substitutions(self) -> dict[str, str]:
        """
        Maps common substitutions in blog templates
        :return: Map of known substitutions to make in templates
        """
        common_subs = Helper.common_substitutions(self.config, self.paths)

        page_subs = {
            "file_name": self.file_name,
            "current_lang": self.current_lang,

            "page_title": self.title,
            "page_description": self.description,
            "page_date": self.date,
            "page_modified": self.modified,
        }

        return {**common_subs, **page_subs}

    def get_page_substitutions(self) -> dict[str, str]:
        """
        Loads the common substitutions used in any page.
        :return: The common content substitutions
        """
        common_subs = self.page_substitutions()

        page_subs = {
            "page_content": Template(self.html_content).safe_substitute(common_subs),
        }

        return {**common_subs, **page_subs}

    def process_content(self) -> tuple[str, dict[str, str]]:
        """
        Converts the markdown page to html and generates and wraps the html content in the page template
        :return: The generated page in html format
        """
        self.html_content = Helper.pandoc_md_to_html(self.src_path)
        page_template = self.load_template()
        substitutions = self.get_page_substitutions()

        return (page_template, substitutions)

    def generate(self) -> str:
        """
        Converts the markdown page to html and generates and wraps the html content in the page template
        :return: The generated page in html format
        """
        page_template, substitutions = self.process_content()
        return Template(page_template).substitute(substitutions)

    def validate_starting_marker(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the starting marker of a markdown post
        :param md_data: The full content of the markdown post file
        :return: True if the starting marker is valid, False otherwise
        """
        if md_data.strip() != "---":
            logger.error(
                f"Failed to validate header of {self.src_path} - the starting marker \"---\" is missing or incorrect.")
            return False

        return True

    def validate_title_field(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the title field of a markdown post
        :param md_data: The full content of the markdown post file
        :return: True if the title field is valid, False otherwise
        """
        matched = re.match(r'^title:\s*(.*?)\s*$', md_data)

        if not matched:
            logger.error(
                f"Failed to validate header of {self.src_path} - the title field is missing, empty, or incorrect.")
            return False

        self.title = matched.group(1)
        return True

    def validate_description_field(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the description field of a markdown post
        :param md_data: The full content of the markdown post file
        :return: True if the description field is valid, False otherwise
        """
        matched = re.match(r'^description:\s*(.*?)\s*$', md_data)

        if not matched:
            logger.error(
                f"Failed to validate header of {self.src_path} - the description field is missing, empty, or incorrect.")
            return False

        self.description = matched.group(1)
        return True

    def validate_date_field(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the date field of a markdown post.
        The date field must be in the format YYYY-MM-DD.
        :param md_data: The full content of the markdown post file
        :return: True if the date field is valid, False otherwise
        """
        matched = re.match(r'^date:\s*([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$)', md_data)

        if not matched:
            logger.error(
                f"Failed to validate header of {self.src_path} - the date field is missing, empty, or incorrect.")
            return False

        self.date = matched.group(1)
        return True

    def validate_modified_field(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the modified field of a markdown post.
        The date field must be in the format YYYY-MM-DD.
        :param md_data: The full content of the markdown post file
        :return: True if the date field is valid, False otherwise
        """
        matched = re.match(r'^modified:\s*([0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$)', md_data)

        if not matched:
            logger.error(
                f"Failed to validate header of {self.src_path} - the modified field is missing, empty, or incorrect.")
            return False

        self.modified = matched.group(1)
        return True

    def validate_tags_field(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the tags field of a markdown post
        The tags field must be a comma-separated list of strings.
        :param md_data: The full content of the markdown post file
        :return: True if the tags field is valid, False otherwise
        """
        matched = re.match(r'^tags:\s*(.*?)\s*$', md_data)

        if not matched:
            logger.error(
                f"Failed to validate header of {self.src_path} - the tags field is missing, empty, or incorrect.")
            return False

        self.tags = sorted((tag for tag in re.findall(r'[^,\s][^,]*[^,\s]|[^,\s]', matched.group(1))), key=lambda tag: tag.casefold())
        return True

    def validate_end_marker(self, md_data: str) -> bool:
        """
        Validate the presence and correctness of the end marker of a markdown post
        :param md_data: The full content of the markdown post file
        :return: True if the end marker is valid, False otherwise
        """
        if md_data.strip() != "---":
            logger.error(
                f"Failed to validate header of {self.src_path} - the end marker \"---\" is missing or incorrect.")
            return False

        return True

    def validate_header(self) -> bool:
        """
        Validates all fields in the header of a markdown post
        :return: True if the header is valid, False otherwise
        """
        logger.debug(f"Processing {self.src_path} ...")
        with open(self.src_path, mode="r", encoding="utf-8") as f:
            md_data = f.readlines()

        # Validate all fields in the header
        return self.validate_starting_marker(md_data[0]) and \
                self.validate_title_field(md_data[1]) and \
                self.validate_description_field(md_data[2]) and \
                self.validate_date_field(md_data[3]) and \
                self.validate_modified_field(md_data[4]) and \
                self.validate_tags_field(md_data[5]) and \
                self.validate_end_marker(md_data[6])

    def raise_when_invalid(self) -> None:
        if not self.validate_header():
            raise Exception(f"page '{self.src_path}' is not valid")


class Post(Page):

    def __init__(self, config: BlogConfig, paths: PathConfig, current_lang: str, src_file_path: str):
        super().__init__(config, paths, current_lang, src_file_path, "post.html.template")

        self.dst_path = Helper.post_src_to_dst_path(self.src_path, os.path.join(self.paths.dst_dir_path, self.current_lang, self.paths.post_dir_name), ".html")
        self.remote_path = Helper.strip_top_directory_in_path(self.dst_path)
        self.file_name = os.path.basename(self.dst_path)

    def get_tags_as_html(self) -> str:
        """
        Wraps the tags of the post in html divs
        :return: The tags wrapped in html divs
        """
        tags: list[str] = []

        for tag in self.tags:
            tag_name = urllib.parse.urlencode({"tag": tag})
            tags.append(f'<a class="tag-bubble" href="../articles.html?{tag_name}" title="{tag}">{tag}</a>')

        return f'<div class="tags">{"".join(tags)}</div>'

    def get_tags_as_meta(self) -> str:
        """
        Wraps the tags of the post in header meta tags
        :return: The tags wrapped in header meta tags
        """
        tags: list[str] = []

        for tag in self.tags:
            tag_name = urllib.parse.urlencode({"tag": tag})
            tags.append(f"<meta property=\"og:article:tag\" content=\"{tag_name}\"/>")

        return "".join(tags)

    def process_content(self) -> tuple[str, dict[str, str]]:
        page_template, common_subs = super().process_content()

        post_subs = {
            "posts_url": self.config.blog_url + self.paths.post_dir_name,

            "post_tags": self.get_tags_as_html(),
            "post_meta_tags": self.get_tags_as_meta(),
        }

        substitutions = {**common_subs, **post_subs}
        return (page_template, substitutions)


class TagsPage(Page):

    def __init__(self, config: BlogConfig, paths: PathConfig, current_lang: str, src_page_path: str, posts: list[Post]):
        super().__init__(config, paths, current_lang, src_page_path)
        self.posts = posts

    def get_post_tags_with_count_as_html(self) -> str:
        """
        Obtains all unique tags from all posts, sorts them by count and wraps them in html divs
        :return: The unique, sorted tags wrapped in html divs
        """
        unique_tags = list(set(tag for post in self.posts for tag in post.tags))
        tag_counts = {tag: sum(tag in post.tags for post in self.posts) for tag in unique_tags}
        sorted_tags = sorted(unique_tags, key=lambda tag: (tag_counts[tag], tag.casefold()))

        tags = ["<div class=\"tags\">"]

        for tag in sorted_tags:
            tag_count = tag_counts[tag]
            tag_param = urllib.parse.urlencode({"tag": tag})

            tags.append(f'<a class="tag-bubble" href="articles.html?{tag_param}" title="{tag_param}">'
                     f"{tag}<span>({tag_count})</span></a>")

        tags.append("</div>")
        return "".join(tags)

    def process_content(self) -> tuple[str, dict[str, str]]:
        page_template, common_subs = super().process_content()
        tags_html = self.get_post_tags_with_count_as_html()

        common_subs["page_content"] = Template(common_subs["page_content"]).safe_substitute({
            "tags_content": tags_html,
        })

        return (page_template, common_subs)


class ArticlesPage(Page):
    def __init__(self, config: BlogConfig, paths: PathConfig, current_lang: str, src_page_path: str, posts: list[Post]):
        super().__init__(config, paths, current_lang, src_page_path, "page.html.template")

        self.title = self.config.label_article
        self.posts = posts

    def get_article_listing_as_html(self) -> str:
        """
        Generates the html for the article listing of all posts
        :return: The html for the article listing
        """
        article_listing = ["<article>"]
        article_listing.append("<ul class=\"articles\">")

        article_posts = sorted(self.posts, key=lambda p: p.date, reverse=True)

        for post in article_posts:
            article_listing.append(f'<li id=\"{post.file_name}\">')
            article_listing.append(f'<b>[{post.date}]</b> ')
            article_listing.append(f'<a href=\"/{post.remote_path}\" title=\"{post.title}\">{post.title}</a>')
            article_listing.append(f'</li>')

        article_listing.append("</ul>")
        article_listing.append("</article>")

        return "".join(article_listing)

    def process_content(self) -> tuple[str, dict[str, str]]:
        page_template, common_subs = super().process_content()
        articles_html = self.get_article_listing_as_html()

        common_subs["page_content"] = Template(common_subs["page_content"]).safe_substitute({
            "articles_content": articles_html,
        })

        return (page_template, common_subs)


class RSSFeed:

    def __init__(self, config: BlogConfig, paths: PathConfig, current_lang: str, posts: list[Post]):
        self.config = config
        self.paths = paths
        self.posts = posts
        self.current_lang = current_lang

    def generate(self) -> None:
        """
        Formats all posts as RSS feed entries and writes the feed to a file
        """

        # Load RSS template
        template_path = os.path.join(self.paths.src_templates_dir_path, "feed.xml.template")
        logger.debug(f"Processing {template_path} ...")

        with open(template_path, mode="r", encoding="utf-8") as f:
            rss_template = f.read()

        feed_data = []
        filtered_posts = [post for post in self.posts if post.current_lang == self.current_lang]

        # Create a feed entry for each post
        for post in filtered_posts:
            post_title = html.escape(post.title)
            post_description = html.escape(post.description)
            post_link = urljoin(self.config.blog_url, post.remote_path)

            pub_date = email.utils.format_datetime(datetime.strptime(post.date, "%Y-%m-%d"))
            updated = email.utils.format_datetime(datetime.strptime(post.modified, "%Y-%m-%d"))

            feed_data.append(f"<item>")
            feed_data.append(f"<pubDate>{pub_date}</pubDate>")
            feed_data.append(f"<updated>{updated}</updated>")

            feed_data.append(f"<title>{post_title}</title>")
            feed_data.append(f"<link>{post_link}</link>")
            feed_data.append(f"<description>{post_description}</description>")
            feed_data.append(f"</item>")

        common_subs = Helper.common_substitutions(self.config, self.paths)

        # Substitute the placeholders with the actual values
        rss_subs = {
            "current_lang": self.current_lang,
            "rss_items": "".join(feed_data),
        }

        substitutions = {**common_subs, **rss_subs}
        rss_template = Template(rss_template).substitute(substitutions)

        # Write substituted template to file
        feed_path = os.path.join(self.paths.dst_dir_path, f"{self.current_lang}_feed.xml")
        with open(feed_path, mode="w", encoding="utf-8") as f:
            f.write(rss_template)


class Sitemap:

    def __init__(self, config: BlogConfig, paths: PathConfig, posts: list[Post], pages: list[Page]):
        self.config = config
        self.paths = paths
        self.posts = posts
        self.pages = pages

    def generate(self) -> None:
        """
        Formats all posts and pages as Sitemap entries and writes the feed to a file
        """

        # Load Sitemap template
        template_path = os.path.join(self.paths.src_templates_dir_path, "sitemap.xml.template")
        logger.debug(f"Processing {template_path} ...")

        with open(template_path, mode="r", encoding="utf-8") as f:
            sitemap_template = f.read()

        feed_data = []

        # Create a feed entry for each page
        for page in self.pages:
            feed_data.append(f"<url>")
            feed_data.append(f"<loc>{urljoin(self.config.blog_url, page.remote_path)}</loc>")
            feed_data.append(f"<lastmod>{page.modified}</lastmod>")
            feed_data.append(f"<changefreq>daily</changefreq>")
            feed_data.append(f"</url>")

        for post in self.posts:
            feed_data.append(f"<url>")
            feed_data.append(f"<loc>{urljoin(self.config.blog_url, post.remote_path)}</loc>")
            feed_data.append(f"<lastmod>{post.modified}</lastmod>")
            feed_data.append(f"<changefreq>daily</changefreq>")
            feed_data.append(f"</url>")

        common_subs = Helper.common_substitutions(self.config, self.paths)

        # Substitute the placeholders with the actual values
        sitemap_subs = {
            "sitemap_items": "".join(feed_data),
        }

        substitutions = {**common_subs, **sitemap_subs}
        sitemap_template = Template(sitemap_template).substitute(substitutions)

        # Write substituted template to file
        sitemap_path = os.path.join(self.paths.dst_dir_path, "sitemap.xml")
        with open(sitemap_path, mode="w", encoding="utf-8") as f:
            f.write(sitemap_template)


class Robots:

    def __init__(self, config: BlogConfig, paths: PathConfig):
        self.config = config
        self.paths = paths

    def generate(self) -> None:
        """
        Generates a robots.txt file in the destination
        """

        # Load Robots template
        template_path = os.path.join(self.paths.src_templates_dir_path, "robots.txt.template")
        logger.debug(f"Processing {template_path} ...")

        with open(template_path, mode="r", encoding="utf-8") as f:
            robots_template = f.read()

        # Substitute the placeholders with the actual values
        substitutions = Helper.common_substitutions(self.config, self.paths)
        robots_template = Template(robots_template).substitute(substitutions)

        # Write substituted template to file
        sitemap_path = os.path.join(self.paths.dst_dir_path, "robots.txt")

        with open(sitemap_path, mode="w", encoding="utf-8") as f:
            f.write(robots_template)


class Blog:

    def __init__(self, config: BlogConfig, paths: PathConfig):
        self.config = config
        self.paths = paths

        self.posts: list[Post] = []
        self.pages: list[Page] = []

        self.processed_posts = 0
        self.skipped_posts = 0

        self.current_lang=""

        if not shutil.which("pandoc"):
            logger.error("Pandoc is not installed. Exiting...")

    def generate(self) -> None:
        """
        Generates the blog, i.e. creates the build directory, copies all files to the build directory, processes all
        posts and pages and generates the rss feed
        """
        logger.debug("Loading base configurations...")
        self.load_base_configuration()

        logger.debug("Creating build directories and copying files...")
        self.clean_build_directory()
        self.create_build_directories()
        self.copy_files_to_build_directories()

        for lang in self.config.available_languages:
            self.current_lang = lang
            logger.info(f"Processing language '{self.current_lang}'...")
            logger.debug("Loading language configurations...")
            self.load_lang_configuration(self.current_lang)

            logger.info("Processing posts...")
            self.process_posts()
            logger.info("Processing pages...")
            self.process_pages()
            logger.info("Processing scripts...")
            self.process_scripts()
            logger.info("Processing rss feed...")
            self.process_rss_feed()

        logger.debug("Loading default language...")
        self.load_lang_configuration(self.config.preferred_language)

        logger.info("Processing root index...")
        self.process_index()
        logger.info("Processing favicon...")
        self.process_favicon()
        logger.info("Processing manifest...")
        self.process_manifest()
        logger.info("Processing sitemap...")
        self.process_sitemap()
        logger.info("Processing robots...")
        self.process_robots()
        logger.info("Processing minification...")
        self.minify_files()

    def load_base_configuration(self)->None:
        path = "mublog.ini"

        parser = configparser.ConfigParser()
        _ = parser.read(path, encoding="utf-8")

        if len(parser.sections()) == 0:
            logger.error("No configuration sections were loaded")
            raise FileNotFoundError(path)

        if "mublog" not in parser:
            logger.error("mublog configuration section was not found")
            raise FileNotFoundError(path)

        section = parser["mublog"]

        self.config.blog_url = section["blog_url"]
        self.config.blog_author_name = section["blog_author_name"]
        self.config.blog_author_mail = section["blog_author_mail"]
        self.config.blog_author_contact = section["blog_author_contact"]
        self.config.post_ignore_prefix = section["post_ignore_prefix"]
        self.config.blog_author_copyright = section["blog_author_copyright"]

        self.config.preferred_language = section["preferred_language"]
        self.config.available_languages = section["available_languages"].split(",")

    def load_lang_configuration(self, lang: str)->None:
        path = "mublog.ini"

        parser = configparser.ConfigParser()
        _ = parser.read(path, encoding="utf-8")

        if len(parser.sections()) == 0:
            logger.error("No configuration sections were loaded")
            raise FileNotFoundError(path)

        if lang not in parser:
            logger.error(f"language configuration section '{lang}' was not found")
            raise FileNotFoundError(path)

        section = parser[lang]

        self.config.blog_title = section["blog_title"]
        self.config.blog_description = section["blog_description"]

        self.config.label_about = section["label_about"]
        self.config.label_article = section["label_article"]
        self.config.label_home = section["label_home"]
        self.config.label_mail = section["label_mail"]
        self.config.label_tags = section["label_tags"]
        self.config.label_rss = section["label_rss"]
        self.config.label_dark_mode = section["label_dark_mode"]
        self.config.label_contact = section["label_contact"]

    def clean_build_directory(self) -> None:
        """
        Removes the build directory and all its contents
        """
        try:
            shutil.rmtree(self.paths.dst_dir_path, ignore_errors=True)

        except Exception as e:
            logger.error(f"Failed to remove old build directory: {str(e)}")

    def create_build_directories(self) -> None:
        """
        Creates the build directory and all subdirectories
        """
        directories = [
            self.paths.dst_dir_path,
            self.paths.dst_css_dir_path,
            self.paths.dst_assets_dir_path,
            self.paths.dst_files_dir_path,
            self.paths.dst_meta_dir_path,
            self.paths.dst_js_dir_path,
        ]

        for lang in self.config.available_languages:
            lang_dir = os.path.join(self.paths.dst_dir_path, lang)
            post_dir = os.path.join(self.paths.dst_dir_path, lang, self.paths.post_dir_name)

            directories.append(lang_dir)
            directories.append(post_dir)

        for directory in directories:
            try:
                os.makedirs(directory, exist_ok=True)

            except Exception as e:
                logger.error(f"Failed to create directory: {str(e)}")
                exit(1)

    def copy_files_to_build_directories(self) -> None:
        """
        Copies css and assets from the src directory to the build directory
        """
        Helper.copy_files(self.paths.src_js_dir_path, self.paths.dst_js_dir_path)
        Helper.copy_files(self.paths.src_css_dir_path, self.paths.dst_css_dir_path)
        Helper.copy_files(self.paths.src_meta_dir_path, self.paths.dst_meta_dir_path)
        Helper.copy_files(self.paths.src_assets_dir_path, self.paths.dst_assets_dir_path)
        Helper.copy_files(self.paths.src_files_dir_path, self.paths.dst_files_dir_path)

    def process_posts(self) -> None:
        """
        Processes all posts, i.e. validates the post header, generates the post html and writes the post to a file
        """
        source_path = os.path.join(self.paths.language_source(self.current_lang), self.paths.post_dir_name)

        for file_path in glob.glob(os.path.join(source_path, "*.md")):
            # Skip posts that start with the ignore prefix
            if os.path.basename(file_path).startswith(self.config.post_ignore_prefix):
                logger.warning(f"Skipping {file_path} ...")
                self.skipped_posts += 1
                continue

            # Validate and generate the post
            post = Post(self.config, self.paths, self.current_lang, file_path)
            post.raise_when_invalid()

            with open(post.dst_path, mode="w", encoding="utf-8") as f:
                f.write(post.generate())

            self.processed_posts += 1
            self.posts.append(post)

    def process_pages(self) -> None:
        """
        Processes all pages, generates the page html and writes the page to a file
        """

        filtered_posts = [post for post in self.posts if post.current_lang == self.current_lang]
        source_path = self.paths.language_source(self.current_lang)

        for file_path in glob.glob(os.path.join(source_path, "*.md")):
            logger.debug(f"Processing {file_path} ...")

            # Create page of the appropriate type
            if os.path.basename(file_path) == "articles.md":
                page = ArticlesPage(self.config, self.paths, self.current_lang, file_path, filtered_posts)
            elif os.path.basename(file_path) == "tags.md":
                page = TagsPage(self.config, self.paths, self.current_lang, file_path, filtered_posts)
            else:
                page = Page(self.config, self.paths, self.current_lang, file_path)

            page.raise_when_invalid()
            with open(page.dst_path, mode="w", encoding="utf-8") as f:
                f.write(page.generate())

            self.pages.append(page)

    def process_index(self) -> None:
        """
        Processes the main index page regardless of languages
        """
        for file_path in glob.glob(os.path.join(self.paths.src_page_dir_path, "*.md")):
            logger.debug(f"Processing {file_path} ...")
            page = Page(self.config, self.paths, "", file_path, "index.html.template")

            page.raise_when_invalid()
            with open(page.dst_path, mode="w", encoding="utf-8") as f:
                f.write(page.generate())

            self.pages.append(page)

    def process_rss_feed(self) -> None:
        """
        Generates the rss feed
        """
        feed = RSSFeed(self.config, self.paths, self.current_lang, self.posts)
        feed.generate()

    def process_scripts(self) -> None:
        """
        Processes all scripts, i.e. generates the tag mapping script
        """
        # Load the JavaScript template
        tags_template_path = os.path.join(self.paths.src_templates_dir_path, "tags.js.template")
        logger.debug(f"Processing {tags_template_path} ...")
        with open(tags_template_path, mode="r", encoding="utf-8") as f:
            js_template = f.read()

        # Create a mapping of post filenames to tags and substitute the template placeholders with the actual values
        with open(os.path.join(self.paths.dst_js_dir_path, f"tags_{self.current_lang}.js"), mode="w", encoding="utf-8") as f:
            entries = [f'"{post.file_name}": [{",".join(map(repr, post.tags))}]' for post in self.posts]
            substitutions = {
                "tag_mapping": ",".join(entries)
            }
            f.write(Template(js_template).substitute(substitutions))

    def minify_files(self) -> None:
        """
        Minifies all files in the destination
        """
        files = []
        targets = ['**/*.js', '**/*.html', '**/*.css', '**/*.webmanifest']

        for target in targets:
            files += glob.glob(os.path.join(self.paths.dst_dir_path, target), recursive=True)

        for item in files:
            with open(item, mode="r+", encoding="utf-8") as file:
                contents = file.read()
                file.seek(0)

                minified = minify_html.minify(
                    code=contents,
                    minify_js=True,
                    minify_css=True,
                    remove_bangs=True,
                    keep_comments=False,
                    keep_closing_tags=True,
                    do_not_minify_doctype=True,
                    keep_spaces_between_attributes=True,
                    remove_processing_instructions=True,
                    keep_html_and_head_opening_tags=True,
                    ensure_spec_compliant_unquoted_attribute_values=True)

                file.write(minified)
                file.truncate()

    def process_favicon(self) -> None:
        """
        Processes the site's Favicon, if present.
        """
        icon_path = os.path.join(self.paths.src_meta_dir_path, "favicon.ico")
        icon_exists = os.path.isfile(icon_path)

        if icon_exists:
            destination_path = os.path.join(self.paths.dst_dir_name, "favicon.ico")
            shutil.copy(icon_path, destination_path)

    def process_manifest(self) -> None:
        """
        Processes the site's manifest, if present.
        """

        manifest_path = os.path.join(self.paths.src_templates_dir_path, "site.webmanifest.template")
        manifest_exists = os.path.isfile(manifest_path)

        if manifest_exists:
            with open(manifest_path, mode="r", encoding="utf-8") as f:
                manifest_template = f.read()

            substitutions = Helper.common_substitutions(self.config, self.paths)

            with open(os.path.join(self.paths.dst_dir_name, "site.webmanifest"), mode="w", encoding="utf-8") as f:
                manifest_template = Template(manifest_template).substitute(substitutions)
                f.write(manifest_template)

    def process_sitemap(self) -> None:
        """
        Generates the Sitemap.xml file
        """
        sitemap = Sitemap(self.config, self.paths, self.posts, self.pages)
        sitemap.generate()

    def process_robots(self) -> None:
        """
        Generates the Robots.txt file
        """
        sitemap = Robots(self.config, self.paths)
        sitemap.generate()


if __name__ == '__main__':
    # Configure logging
    start_time = time.time()
    logger = logging.getLogger('mublog')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(LogFormatter())
    logger.addHandler(ch)

    # Start blog generation
    blog_conf = BlogConfig()
    path_conf = PathConfig()
    blog = Blog(blog_conf, path_conf)
    blog.generate()

    # Build summary
    end_time = time.time()
    print("---------------------------------------------------------")
    logger.info(f"Posts Processed: {blog.processed_posts} | Posts Skipped: {blog.skipped_posts}")
    logger.info(f"Elapsed Time: {round(end_time - start_time, 1)} seconds.")
    logger.info("Blog generation complete.")
