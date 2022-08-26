# Extractor

Simple tool to extract posts and comments data from two specific forum posts by only using Regex. The tool extract raw data without information about dates, users, signatures etc.

## Features

1.  Extracting the post data
2.  Extracting the comments on the post

## Repository Structure

There's a folder for each post inside the folder there is the python code that extracts the post data and an output file that shows the extracted data.
I also created an enhanced version for self-exploring.

```ascii
├── phpbb-extractor/
│   ├── phpbb.py
│   ├── phpBB-output.txt
│   └── README.md
│
├── vbulletin-extractor/
│   ├── vbulletin.py
│   ├── vBulletin-output.txt
│   └── README.md
│
├── enchanced-extractor/
│   ├── extractor.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

## Installing
```bash
    $ git clone https://github.com/razlevio/extractor
    $ cd extractor
    $ pip install -r requirements.txt
```

## Dependencies

* [requests](https://requests.readthedocs.io/) >= 2.28.1

## Usage
```bash
    $ cd phpbb-extractor
    $ python phpbb.py
```
```bash
    $ cd vbulletin-extractor
    $ python vbulletin.py
```

## Observation
Extracting data from HTML using python with only Regex is not advisable; I did that because it was the task's requirement. In practice, there are better approaches to parsing HTML and extracting data from it. According to a [Stackoverflow post by bobince](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454): "Regex is not a tool that can be used to parse HTML correctly. The use of Regex will not allow you to consume HTML properly. Regular expressions are a tool that is insufficiently sophisticated to understand the constructs employed by HTML. HTML is not a regular language and hence cannot be parsed by regular expressions. Regex queries are not equipped to break down HTML into its meaningful parts. Even enhanced irregular regular expressions as used by Perl are not up to the task of parsing HTML. HTML is a language of sufficient complexity that it cannot be parsed by regular expressions.
