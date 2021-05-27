from urllib.request import urlopen

url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
soup.title