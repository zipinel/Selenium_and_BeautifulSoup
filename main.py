from Base import linkChecker
from Locators import locator
from Pages import PagesToCheck
import pytest

pageWithLinksToTest = PagesToCheck.getPages()
links = locator.linkExtractor(pageWithLinksToTest)
linksChecked = linkChecker.linkCheck(links)


def test_badLinks():
    allLinks = linksChecked
    assert allLinks[1] == []
