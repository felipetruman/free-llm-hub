"""Resolve repository-only language links when rendering the public site."""
import re

LANGUAGE_LINK = re.compile(r"(?<=\]\()\.github/i18n/README\.[\w-]+\.md(?=\))")


def on_page_markdown(markdown, *, page, config, **kwargs):
    # The home page is copied from the repository README. Translations live in
    # GitHub, not in docs/; keep the original links relative in the README.
    if page.file.src_uri != "index.md" or not config.repo_url:
        return markdown
    repo = config.repo_url.rstrip("/")
    return LANGUAGE_LINK.sub(lambda match: f"{repo}/blob/main/{match.group()}", markdown)
