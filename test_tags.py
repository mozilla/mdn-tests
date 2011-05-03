import unittest
from selenium import selenium
from demo_page import DemoPage
from test_homepage import TestHomepage
from vars import ConnectionParameters


class TestTags(unittest.TestCase):
    
    def setUp(self):
        self.selenium = selenium(ConnectionParameters.server,\
        ConnectionParameters.port,ConnectionParameters.browser,\
        ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(ConnectionParameters.page_load_timeout)
        
    def tearDown(self):
        self.selenium.stop()
        
    def test_all_tags(self):
        demo_pg = DemoPage(self.selenium)
        demo_pg.go_to_page
        links = demo_pg.get_tag_links
        for keys, values in sorted(links.items()):
            demo_pg.open(links[keys])

            
            
            
    
if __name__ == "__main__":
    unittest.main()    