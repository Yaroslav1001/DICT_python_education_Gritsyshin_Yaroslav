import requests
from bs4 import BeautifulSoup
import shutil
from os import mkdir
import string

BASE_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"


def simple_parser():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url)
    if response.ok:
        result = response.json()
        print(result.get('content'))

    else:
        print("Invalid quote resource!")


def parse_html_doc():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})

    try:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.h1.string
        description = soup.find('meta', {'name': 'description'})
        if not title or not description:
            raise AttributeError()
        film_info = {"title": title, "description": description["content"]}
        print(film_info)

    except AttributeError:
        print("Invalid movie page!")


def save_html_page():
    url = correct_input_url("Please input URL > ")
    response = requests.get(url)
    if response.ok:
        save_in_file(response.content)
    else:
        print(f"The URL returned {response.status_code}")


def save_in_file(page):
    with open("web_page.html", "wb") as f:
        f.write(page)
        print("Content saved.")


def parsing_articles():
    shutil.rmtree("articles")
    response = requests.get(BASE_URL)
    if response.ok:
        links = get_tuple_links(response)
        print("Determine what articles you need, this may take some time...")
        mkdir("articles")
        save_all_article(links)

    else:
        print(f"The URL returned {response.status_code}")


def correct_input_url(string):
    url = input(string)
    if url.startswith('http://'):
        return url
    elif url.startswith('https://'):
        return url
    print("URL mast begin with http:// or https://")
    correct_input_url(string)


def get_tuple_links(response):
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    links_tags = soup.find_all("a", class_="c-card__link")
    return map(lambda x: (x.text, x["href"]), links_tags)


def get_article_by_path(path):
    host = "https://www.nature.com"
    response = requests.get(f"{host}{path}")
    if response.ok:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:

            article_type = soup.find("article")["data-track-component"]
            if article_type != "news":
                return
        except KeyError:
            return

        if article_type != "news":
            return

        try:
            article_content = soup.find("div", {"class": "c-article-body"}).get_text().strip()
        except AttributeError:
            article_content = soup.find("article").get_text().strip()
        return article_content


def save_all_article(links):
    for link in links:
        name, path = link
        article = get_article_by_path(path)
        if not article:
            continue
        save_article(name, article)


def save_article(name: string, content):
    table = name.maketrans("", "", string.punctuation + "’")
    title = name.translate(table)
    title = title.strip().replace(" ", "_")

    print("Title: ", title)
    with open(f"articles/{title}.txt", "w") as f:
        f.write(content)
        print("Article saved.")

parsing_articles()
