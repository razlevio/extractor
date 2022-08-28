from extractor import Extractor
from urllib.parse import urlparse
import argparse

# Constants for forum supportability
PHPBB_TARGET_ELEMENT = "div"
PHPBB_TARGET_CLASS = "content"

VBULLETIN_TARGET_ELEMENT = "div"
VBULLETIN_TARGET_CLASS = "js-post__content-text restore h-wordwrap"

REDDIT_TARGET_ELEMENT = "p"
REDDIT_TARGET_CLASS = "_1qeIAgB0cPwnLhDF9XSiJM"

# phpBB_url = "https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437"
# vBulletin_url = "https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login"
# reddit_url = "https://www.reddit.com/r/funkopop/comments/wyd4ht/next_nft_drop_is_dc_series_2_dang_they_really/"

def main():
    interactive_mode()


def get_input():
    """
    Getting target forum and post url from user
    :return: Forum identifier and url for post
    :rtype: list
    """
    print("Target forum (INSERT NUMBER): ")
    forum = input(f"1. phpBB\n2. vBulletin\n3. Reddit\n$ ").strip()
    while forum != "1" and forum != "2" and forum != "3":
        print("WRONG ARGUMENT")
        print("===============")
        print("Target forum (INSERT NUMBER): ")
        forum = input(f"1. phpBB\n2. vBulletin\n3. Reddit\n$ ").strip()
    if forum == "1":
        url = input(f"Insert phpBB forum post URL: ").strip()
        validation = url.lower()
        while "phpbb" not in validation:
            print("You insered invalid url for phpBB forum")
            url = input(f"Insert phpBB forum post URL: ").strip()
            validation = url.lower()
        return ["phpbb", url]
    elif forum == "2":
        url = input(f"Insert vBulletin forum post URL: ").strip()
        validation = url.lower()
        while "vbulletin" not in validation:
            print("You insered invalid url for vBulletin forum")
            url = input(f"Insert vBulletin forum post URL: ").strip()
            validation = url.lower()
        return ["vbulletin", url]
    elif forum == "3":
        url = input(f"Insert Reddit forum post URL: ").strip()
        validation = url.lower()
        while "reddit" not in validation:
            print("You insered invalid url for Reddit forum")
            url = input(f"Insert Reddit forum post URL: ").strip()
            validation = url.lower()
        return ["reddit", url]


def interactive_mode():
    """
    Executing interactive input gathering from user
    """
    forum = get_input()
    if forum[0] == "phpbb":
        extractor = Extractor(forum[1], PHPBB_TARGET_ELEMENT, PHPBB_TARGET_CLASS)
        extractor.extract()
    elif forum[0] == "vbulletin":
        extractor = Extractor(forum[1], VBULLETIN_TARGET_ELEMENT, VBULLETIN_TARGET_CLASS)
        extractor.extract()
    else:
        extractor = Extractor(forum[1], REDDIT_TARGET_ELEMENT, REDDIT_TARGET_CLASS)
        extractor.extract()


if __name__ == "__main__":
    main()
