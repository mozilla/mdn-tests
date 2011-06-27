from selenium import selenium
from unittestzero import Assert
from demo_page import DemoPage

class TestHomepage:
        
    def test_header_links(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        Assert.true(demo_pg.topics_link)
        Assert.true(demo_pg.docs_link)
        Assert.true(demo_pg.demos_link)
        Assert.true(demo_pg.learning_link)
        Assert.true(demo_pg.forums_link)
        Assert.true(demo_pg.join_mdn)
        Assert.true(demo_pg.login_locator)
        Assert.true(demo_pg.search_mdn_locator)
        Assert.true(demo_pg.demo_studio_locator)
        Assert.true(demo_pg.learning_link)
        Assert.true(demo_pg.forums_link)
        Assert.true(demo_pg.join_mdn)
        Assert.true(demo_pg.login_locator)
        Assert.true(demo_pg.search_mdn_locator)
        Assert.true(demo_pg.demo_studio_locator)
        Assert.true(demo_pg.learn_more_locator)
        
        
    def test_footer_links(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        Assert.true(demo_pg.footer_img)
        Assert.true(demo_pg.footer_rss_link)
        Assert.true(demo_pg.footer_bar_feedback_link)
        Assert.true(demo_pg.footer_licenses_link)
        Assert.true(demo_pg.footer_about_link)
        Assert.true(demo_pg.footer_privacy_link)
        Assert.true(demo_pg.footer_help_link)
        
    def test_demo_title(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        totalDemoTitles = demo_pg.get_demo_title_count()
        for i in range(1,totalDemoTitles+1):
            Assert.true(demo_pg.demo_title_locator(i))
            
    def test_demo_image(self,testsetup):
        demo_pg = DemoPage(testsetup)
        demo_pg.open("/demos")
        totalDemoImages = demo_pg.get_demo_image_count()
        for i in range(1,totalDemoImages+1):
            Assert.true(demo_pg.demo_image_locator(i))
      