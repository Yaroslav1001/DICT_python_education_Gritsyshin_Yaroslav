import requests
from bs4 import BeautifulSoup
from pprint import pprint


def parser_json():
    url = url_input("Pleas input URL >")
    response = requests.get(url)
    if response.ok:
        result = response.json()
        print(result.get('content'))

    else:
        print("Invalid quote resource!")


def web_parser():
    url = url_input("Please input URL >")
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    try:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.h1.string
        form = soup.find('meta', {'name': 'description'})
        if not title or not form:
            raise AttributeError()
        page_info = {"title": title, "description": form["content"]}
        pprint(page_info)

    except AttributeError:
        print("Invalid movie page!")


def save_page():
    url = url_input("Please input URL >")
    response = requests.get(url)
    if response.ok:
        saving_content(response.content)
    else:
        print(f"The URL returned {response.status_code}")


def saving_content(page):
    with open("web_page.html", "wb") as f:
        f.write(page)
        print("Content saved.")


def url_input(string):
    url = input(string)
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    print("URL mast begin with http:// or https://")
    url_input(string)


save_page()