from selenium import selenium
from unittestzero import Assert
from demo_page import DemoPage
from derby_page import DerbyPage
import pytest
xfail = pytest.mark.xfail


class TestDevDerbyPage:
     
    def test_is_footer_links(self, testsetup):
        derby_pg = DemoPage(testsetup)
        derby_pg.open("en-US/demos/devderby")
        Assert.true(derby_pg.is_footer_img_visible)
        Assert.true(derby_pg.is_footer_bar_feedback_link_visible)
        Assert.true(derby_pg.is_footer_licenses_link_visible)
        Assert.true(derby_pg.is_footer_about_link_visible)
        Assert.true(derby_pg.is_footer_privacy_link_visible)
        Assert.true(derby_pg.is_footer_help_link_visible)
        
    @xfail(reason="No derby winners on production yet")
    def test_derby_page(self, testsetup):
        derby_pg = DerbyPage(testsetup)
        derby_pg.open("en-US/demos/devderby")
        Assert.true(derby_pg.is_home_link_visible)
        Assert.true(derby_pg.is_challenges_link_visible)
        Assert.true(derby_pg.is_rules_link_visible)
        Assert.true(derby_pg.is_judging_link_visible)
        Assert.true(derby_pg.is_prizes_link_visible)
        Assert.true(derby_pg.is_resources_link_visible)
        Assert.true(derby_pg.is_submit_demo_link_visible)
        Assert.true(derby_pg.is_demo_studio_link_visible)
        Assert.true(derby_pg.is_previous_winner_banner_visible)
        Assert.true(derby_pg.is_previous_winner_demo_title_visible)
        Assert.true(derby_pg.is_previous_winner_name_visible)
        Assert.true(derby_pg.is_previous_winner_demo_button_visible)
        Assert.true(derby_pg.is_docs_link_visible)
        Assert.true(derby_pg.is_articles_link_visible)
        Assert.equal(derby_pg.get_prizes_text, "Prizes")
