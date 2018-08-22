from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'thmbooom',
  scripts=['thmbooom'],   
  version = '0.114',
  description = 'Module to auto download lecture slides https://moodle.thm.de',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Bilal Reffas',
  author_email = 'bilalreffas@googlemail.com',
  url = 'https://github.com/BilalReffas/Thmbooom',
  download_url = 'https://github.com/BilalReffas/Thmbooom',
  keywords = ['python','webscraping','downloader','automation','uiatomation-selenium'],
     classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)