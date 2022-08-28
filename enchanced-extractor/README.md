# Extractor

Simple tool to extract posts and comments data from different forums. The tool extract raw data without information about dates, users, signatures etc.

## Features

1.  Extracting the post raw data, which indicates what is the post about
2.  Extracting the raw comments on the post


## Installing
```bash
    $ git clone https://github.com/razlevio/extractor
    $ cd extractor/enchanced-extractor
    $ pip install -r requirements.txt
```
We also need to including `chromedriver`, [download chromedriver](https://chromedriver.chromium.org/downloads) notice that you need to download the chromedriver with the correct version according to the installed chrome version in your PC.  
After downloading the chromedriver include it in the `extractor/enchanced-extractor/` folder
## Dependencies

* [Selenium](https://www.selenium.dev/) >= 4.4.3
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) >= 4.11.1


## Usage
```bash
    $ python controller.py
```
or
```bash
    $ python controller.py -flag url
    # flags:
    #   -ph for phpBB
    #   -b for vBulletin
    #   -r for reddit
```
