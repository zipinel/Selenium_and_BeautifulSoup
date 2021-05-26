import requests


def linkCheck(linksFound):
    goodLinks = []
    badLinks = []
    for link in linksFound:
        res = requests.get(link)
        if res.status_code == 200:
            print(link + " <<<<<<<<<< 200")
            goodLinks.append(link)
        else:
            badLink = res.status_code
            badLinks.append(link)
            print(link + " <<<<<<<<<< link broken. Status: " + str(badLink))
    return goodLinks, badLinks
