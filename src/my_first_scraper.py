from urllib.request import urlopen

def get_html_str(url: str):
    page = urlopen(url)

    # urlopen() returns an HTTPResponse object:
    print(page)

    # To extract the HTML from the page, first use the HTTPResponse object’s .read() method, which returns a sequence of bytes.
    # Then use .decode() to decode the bytes to a string using UTF-8:

    html_bytes = page.read()
    html = html_bytes.decode('utf-8')

    print("\n-----HTML CONTENT-----\n")
    print(html)
    return html

def get_title(html: str):
    print("\n---Extracting Title from web page---\n")
    title_start_index = html.find("<title>") + len("<title>")
    title_end_index = html.find("</title>")
    title = html[title_start_index: title_end_index]
    print(title)
    
if __name__ == "__main__":
    url = 'http://olympus.realpython.org/profiles/aphrodite'
    html = get_html_str(url)
    get_title(html)