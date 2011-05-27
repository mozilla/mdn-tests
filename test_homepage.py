from selenium import selenium
from unittestzero import Assert
from demo_page import DemoPage

class TestHomepage:
        
    def test_header_links(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.go_to_page
        Assert.true(demo_pg.get_header_image)
        Assert.true(demo_pg.get_login_link)
        Assert.true(demo_pg.get_signup_link)
        Assert.true(demo_pg.get_search_mdn)
        
    def test_footer_links(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        Assert.true(demo_pg.feedback)
        Assert.true(demo_pg.footer_image)
        Assert.true(demo_pg.footer_copyright_text)
        Assert.true(demo_pg.footer_license)
        Assert.true(demo_pg.footer_privacy_policy)
        Assert.true(demo_pg.footer_language)
        Assert.true(demo_pg.footer_signup)
        Assert.true(demo_pg.footer_about)
        Assert.true(demo_pg.footer_login)
    
    def test_technology_links(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        links = demo_pg.get_tags
        for keys, values in sorted(links.items()):
            Assert.true(links[keys])