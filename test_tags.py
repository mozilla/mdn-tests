from selenium import selenium
from unittestzero import Assert
from test_homepage import TestHomepage
from demo_page import DemoPage



class TestTags:
            
    def test_all_tags(self,testsetup):
        self.selenium = testsetup.selenium
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        links = demo_pg.get_tag_links
        for keys, values in sorted(links.items()):
            demo_pg.open(links[keys])
  