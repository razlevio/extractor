import requests
import re

def main():
    vBulletin = "https://forum.vbulletin.com/forum/vbulletin-3-8/vbulletin-3-8-questions-problems-and-troubleshooting/414325-www-vs-non-www-url-causing-site-not-to-login"
    posts = extract_posts(vBulletin)
    output_proccesing(posts)

def extract_posts(url):
    """
    Extracts posts and comments from provided vBulletin forum post
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

    # Regex pattern to target every div with class=content class which is the html elements vBulletin forum classify as actual data
    pattern = r"<div class=\"[^\"']*?\bjs-post__content-text restore h-wordwrap\" itemprop=\"text\b[^\"']*?\">(.*?)<\/div>"

    # Find all div elements that have class=js-post__content-text restore h-wordwrap and attribute itemprop=text
    data = re.findall(pattern, html, re.DOTALL)

    # Traversing every div element(post) and remove all nested tags and some irrelevant tabs spaces and newlines
    for post in data:
        post = re.sub(r"<[^>]*>", "", post)
        post = re.sub(r"&quot;", "\"", post)
        post = post.strip()
        post = re.sub(r"[\r\n\t]+(.)*?", r"\n", post)
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
    for match in re.finditer(r'<div class="bbcode_quote_container b-icon b-icon__ldquo-l--gray">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(match.group(), cleaned, html)

    for match in re.finditer(r'<div class=\"bbcode_postedby\">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"(<[^>]*>)", "", match.group())
        cleaned = re.sub(r"View Post", "", cleaned)
        html = re.sub(r'<div class=\"bbcode_postedby\">(.|\n)*?<\/div>', cleaned, html, 1)

    for match in re.finditer(r'<div class="message">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="message">(.|\n)*?<\/div>', cleaned, html, 1)

    for match in re.finditer(r'<div class="quote_container">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="quote_container">(.|\n)*?<\/div>', cleaned, html, 1)

    for match in re.finditer(r'<div class="bbcode_quote">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="bbcode_quote">(.|\n)*?<\/div>', cleaned, html, 1)
    
    for match in re.finditer(r'<div class="bbcode_description">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="bbcode_description">(.|\n)*?<\/div>', cleaned, html, 1)
    
    for match in re.finditer(r'<div class="bbcode_code">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="bbcode_code">(.|\n)*?<\/div>', cleaned, html, 1)

    for match in re.finditer(r'<div class="bbcode_container">(.|\n)*?<\/div>', html):
        cleaned = re.sub(r"<[^>]*>", "", match.group())
        html = re.sub(r'<div class="bbcode_container">(.|\n)*?<\/div>', cleaned, html, 1)

    return html


def output_proccesing(data):
    """
    Printing the posts data one by one, and save the posts to an vBulletin-output.txt file
    :param data: Cleaned posts data
    :type data: str
    """
    print(data)
    # Enumerating each post
    data = dict(enumerate(data,1))

    # Save contents to output file and also prints every post
    with open("vBulletin-output.txt", "w") as file:
        for num,post in data.items():
            file.write(f"{num}. {post}\n\n")
            print(f"{num}. {post}\n")


if __name__ == "__main__":
    main()
