from bs4 import BeautifulSoup
from Locators import webDriverSetup


def linkExtractor(pageWithLinks):
    #### First action the extractor will do is handling lazy loading of this page with the help of Selenium
    stretchedPage = webDriverSetup.seleniumAction(pageWithLinks)

    #### Now we pass the extended html that Selenium returned to us, inside BeautifulSoup
    soup = BeautifulSoup(stretchedPage, features="html.parser")
    linksFound = []
    for articleIndex in range(1, 50):
        htmlElement = soup.select(f'#YDC-Stream > ul > li:nth-of-type({articleIndex}) > div > div > div > h3 > a')
        for item in htmlElement:
            partialLink = item.get('href')
            articleLink = "https://news.yahoo.com" + str(partialLink)
            ### Some articles are just ads carefully designed to mimic a real article. This avoids it
            adRemover = "beap.gemini.yahoo.com"
            if adRemover not in articleLink:
                linksFound.append(articleLink)
    return linksFound
