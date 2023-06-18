# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import requests

# # url = "http://olympus.realpython.org/profiles/dionysus"
# url = "https://www.airtel.in/business/commercial-communication/help#:~:text=with%20Principal%20Entities-,Click%20here%20to%20download,-Download%20Forms"

# # page = urlopen(url)
# # html = page.read().decode("utf-8")
# # soup = BeautifulSoup(html, "html.parser")

# # print(dir(soup))
# # print(soup.get_text())
# # link = soup.find("a", href=True, string="Click here to download")
# # print(link)
# page = requests.get(url)
# print(page.text)


import requests
from bs4 import BeautifulSoup

url = "https://www.airtel.in/business/commercial-communication/help#:~:text=with%20Principal%20Entities-,Click%20here%20to%20download,-Download%20Forms"

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the relevant section or element containing the desired data
    section = soup.find("div", class_="class-of-the-section")  # Adjust the class based on the specific HTML structure

    if section:
        # Extract the text content from the section
        data = section.get_text()

        # Print the extracted data
        print(data)
    else:
        print("Section not found on the page.")
else:
    print("Unable to access the URL.")
