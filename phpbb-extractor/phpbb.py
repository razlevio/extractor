import requests
import re

def main():
    phpBB = "https://www.phpbb.com/community/viewtopic.php?f=46&t=2159437"
    posts = extract_posts(phpBB)
    output_proccesing(posts)


def extract_posts(url):
    """
    Extracts posts and comments from provided phpBB forum post
    :param url: The link of the forum post
    :type url: str
    :return: List that holds the posts cleaned data
    :rtype: list
    :raise RequestException: If problem occur in get request
    """

    # List that store final cleaned data
    res = []

    # Getting the post as HTML and convert it to plain text
    try:
        html = requests.get(url).text
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    # Removing nested div elements that interfere with extracting the data
    html = remove_nested_divs(html)

    # Regex pattern to target every div with class=content class which is the html elements phpBB forum classify as actual data
    pattern = r"<div class=\"[^\"']*?\bcontent\b[^\"']*?\">(.*?)<\/div>"

    # Find all div elements that have class=content
    data = re.findall(pattern, html, re.DOTALL)

    # Traversing every div element(post) and remove all nested tags
    for post in data:
        post = re.sub(r"<[^>]*>", "", post)
        res.append(post)

    return res


def remove_nested_divs(html):
    """
    Remove nested div elements that interfere with extracting the data when using Regex
    :param html: The web page html content
    :type html: str
    :return: The html content without problamatic divs
    :rtype: str
    """
    for match in re.finditer(r'<blockquote><div>(.*?)<\/div><\/blockquote>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(match.group(), cleaned, html)
    return html


def output_proccesing(data):
    """
    Printing the posts data one by one, and save the posts to an phpBB-output.txt file
    :param data: Cleaned posts data
    :type data: str
    """
    
    # Enumerating each post
    data = dict(enumerate(data,1))
    # Save contents to output file and also prints every post
    with open("phpBB-output.txt", "w") as file:
        for num,post in data.items():
            file.write(f"{num}. {post}\n\n")
            print(f"{num}. {post}\n")


if __name__ == "__main__":
    main()