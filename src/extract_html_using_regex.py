# here we try to extract stuff from html webpage using regex
from urllib.request import urlopen
import re


def get_html(url: str):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode('utf-8')
    print(html)
    return html

# <title.*?> matches the opening <TITLE > tag in html.
# The <title part of the pattern matches with
# <TITLE because re.search() is called with re.IGNORECASE, and .*?> matches any text after <TITLE up to the first instance of >.
# .*? non-greedily matches all text after the opening <TITLE >, stopping at the first match for </title.*?>.
# </title.*?> differs from the first pattern only in its use of the / character, so it matches the closing </title  / > tag in html.

def extract_title(html: str):
    regex_pattern = "<title.*?>*<*title.*?>"
    match_results = re.search(regex_pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)
    print("-----\n\n")
    print(title)



if __name__ == "__main__":
    url = "http://olympus.realpython.org/profiles/dionysus"
    html = get_html(url)
    extract_title(html)