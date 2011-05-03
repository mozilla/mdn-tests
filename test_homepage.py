import unittest
from selenium import selenium
from demo_page import DemoPage
from vars import ConnectionParameters


class TestHomepage(unittest.TestCase):

    def setUp(self):
        self.selenium = selenium(ConnectionParameters.server, \
        ConnectionParameters.port, ConnectionParameters.browser, \
        ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()
        
    def test_header_links(self):
        demo_pg = DemoPage(self.selenium)
        demo_pg.go_to_page
        self.assertTrue(demo_pg.get_header_image)
        self.assertTrue(demo_pg.get_login_link)
        self.assertTrue(demo_pg.get_signup_link)
        self.assertTrue(demo_pg.get_search_mdn)
        
    def test_footer_links(self):
        demo_pg = DemoPage(self.selenium)
        demo_pg.go_to_page
        self.assertTrue(demo_pg.feedback)
        self.assertTrue(demo_pg.footer_image)
        self.assertTrue(demo_pg.footer_copyright_text)
        self.assertTrue(demo_pg.footer_license)
        self.assertTrue(demo_pg.footer_privacy_policy)
        self.assertTrue(demo_pg.footer_language)
        self.assertTrue(demo_pg.footer_signup)
        self.assertTrue(demo_pg.footer_about)
        self.assertTrue(demo_pg.footer_login)
    
    def test_technology_links(self):
        demo_pg = DemoPage(self.selenium)
        demo_pg.go_to_page
        links = demo_pg.get_tags
        for keys, values in sorted(links.items()):
            self.assertTrue(links[keys])
            

if __name__ == "__main__":
    unittest.main() 