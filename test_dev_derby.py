from selenium import selenium
from unittestzero import Assert
from demo_page import DemoPage
from derby_page import DerbyPage
import pytest
xfail = pytest.mark.xfail


class TestDevDerbyPage:
    
    def test_footer_links(self,testsetup):
        derby_pg = DemoPage(testsetup)
        derby_pg.open("en-US/demos/devderby")
        Assert.true(derby_pg.footer_img)
        Assert.true(derby_pg.footer_bar_feedback_link)
        Assert.true(derby_pg.footer_licenses_link)
        Assert.true(derby_pg.footer_about_link)
        Assert.true(derby_pg.footer_privacy_link)
        Assert.true(derby_pg.footer_help_link)
        
    @xfail(reason="No derby winners on production yet")
    def test_derby_page(self,testsetup):
        derby_pg = DerbyPage(testsetup)
        derby_pg.open("en-US/demos/devderby")
        Assert.true(derby_pg.home_locator)
        Assert.true(derby_pg.challenges_locator)
        Assert.true(derby_pg.rules_locator)
        Assert.true(derby_pg.judging_locator)
        Assert.true(derby_pg.prizes_locator)
        Assert.true(derby_pg.resources_locator)
        Assert.true(derby_pg.submit_demo_locator)
        Assert.true(derby_pg.demo_studio_locator)
        Assert.true(derby_pg.previous_winner_banner)
        Assert.true(derby_pg.previous_winner_demo_title)
        Assert.true(derby_pg.previous_winner_name)
        Assert.true(derby_pg.previous_winner_demo_button)
        Assert.true(derby_pg.docs_link)
        Assert.true(derby_pg.articles_link)
        
