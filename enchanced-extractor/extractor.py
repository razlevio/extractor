import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup

class Extractor:
    """
    A class to represent forum posts extractor object

    :attribute url: The post url
    :type url: str
    :attribute target_element: The specific forum html element that represents the posts data
    :type target_element: str
    :attribute target_class: The specific class that attached to the elements that represents the posts data
    :type target_class: str

    :method extract_html_data: Extracts the html from the forum post web page
    :method extract_posts: Extracts the posts data from the html
    :method output_proccesing: Printing the posts data and create output file with the posts contents
    """

    def __init__(self, url, target_element, target_class):
        """
        Constructor that gets url, target element and target class and initalize the extractor object
        :param url: The post url
		:type name: str
        :param target_element: The specific forum html element that represents the posts data
        :type target_element: str
        :param target_class: The specific class that attached to the elements that represents the posts data
        :type target_class: str
        """
        self.url = url
        self.target_element = target_element
        self.target_class = target_class


    def extract_html_data(self):
        """
        Extract the html content of a webpage
        :param url: The link of the webpage
        :type url: str
        :return: The html content of the webpage
        :rtype: str
        """

        # Setting up chromedriver
        driver = webdriver.Chrome("./chromedriver")

        # Wait for javascript to load
        driver.implicitly_wait(1000)
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.get(self.url)

        # Loop to keep scrolling the page to load all javascript
        while True:
            # Scroll down to the bottom.
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load the page.
            time.sleep(1)
            # Calculate new scroll height and compare with last scroll height.
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Extracting the html from the selenium driver
        html = driver.page_source
        driver.close()
        driver.quit()

        return html


    def extract_posts(self, html):
        """
        Extracts posts and comments from provided forum post
        :param html: The html content of the forum post
        :type url: str
        :return: List that holds the posts cleaned data
        :rtype: list
        """

        # List that store final cleaned data
        res = []

        # HTML parser
        soup = BeautifulSoup(html, 'html.parser')

        # Getting all posts
        posts = soup.findAll(self.target_element, class_=self.target_class)

        for post in posts:
            post = post.text.strip()
            post = re.sub(r"View Post", "", post)
            post = re.sub(r"&quot;", "\"", post)
            post = re.sub(r"[\r\n\t]+(.)*?", r"\n", post)
            res.append(post)

        return res


    def output_proccesing(self, data):
        """
        Printing the posts data one by one, and save the posts to an output.txt file
        :param data: Cleaned posts data
        :type data: str
        """
        
        # Enumerating each post
        data = dict(enumerate(data,1))
        # Save contents to output file and also prints every post
        with open("vBulletin-output.txt", "w") as file:
            for num,post in data.items():
                file.write(f"{num}. {post}\n\n")
                print(f"{num}. {post}\n")


    def extract(self):
        """
        The extraction proccess combining the functions above by firstly extract the html
        then extract the posts out from the html and then proccessing and printing the raw posts data
        """
        html = self.extract_html_data()
        posts = self.extract_posts(html)
        self.output_proccesing(posts)
