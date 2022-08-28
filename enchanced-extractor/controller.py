from extractor import Extractor
import argparse

# Constants for forum supportability
PHPBB_TARGET_ELEMENT = "div"
PHPBB_TARGET_CLASS = "content"

VBULLETIN_TARGET_ELEMENT = "div"
VBULLETIN_TARGET_CLASS = "js-post__content-text restore h-wordwrap"

REDDIT_TARGET_ELEMENT = "p"
REDDIT_TARGET_CLASS = "_1qeIAgB0cPwnLhDF9XSiJM"


def main():
    # Parsing the command line arguments
    args = parse_arguments()

    # Check if user want to execute the program interactively or by providing CLI arguments
    if all(value == None for value in args.values()):
        # Executing the program interactively
        interactive_mode()
    else:
        # Executing the program based on CLI arguments
        cli_mode(args)


def parse_arguments():
    """
    Command line arguments parser
    :return: the arguments which indicates the forums, and the url provided for the forum
    :rtype: dict
    """

    # Create CLI argument parser
    parser = argparse.ArgumentParser(description='Extracting forums posts, provide the flag of the forum you want extract data from and the url of the post')
    group = parser.add_mutually_exclusive_group()
    # Add arguments
    group.add_argument('-ph', '--phpbb', type=str, help="phpBB")
    group.add_argument('-vb', '--vbulletin', type=str, help="vBulletin")
    group.add_argument('-r', '--reddit', type=str, help="Reddit")
    # Parse the argument
    args = vars(parser.parse_args())
    return args


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


def cli_input_validation(forum, url):
    forum = forum.lower()
    url = url.lower()
    if forum in url:
        return True
    else:
        return False


def interactive_mode():
    """
    Executing the extractor interactively by gathering input from user
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


def cli_mode(args):
    """
    Executing the extractor by provided input in CLI
    """
    for key, value in args.items():
        if value != None:
            forum = key
            url = value
            break
    if not cli_input_validation(forum, url):
        print(f"You insered invalid url for {forum} forum")
        return
    if forum == "phpbb":
        extractor = Extractor(url, PHPBB_TARGET_ELEMENT, PHPBB_TARGET_CLASS)
        extractor.extract()
    elif forum == "vbulletin":
        extractor = Extractor(url, VBULLETIN_TARGET_ELEMENT, VBULLETIN_TARGET_CLASS)
        extractor.extract()
    else:
        extractor = Extractor(url, REDDIT_TARGET_ELEMENT, REDDIT_TARGET_CLASS)
        extractor.extract()


if __name__ == "__main__":
    main()
