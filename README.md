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