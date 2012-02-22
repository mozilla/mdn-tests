#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.demo import DemoPage
from pages.desktop.learn import LearnPage


class TestLearnPage:

    def test_are_footer_links_visible(self, mozwebqa):
        learn_pg = DemoPage(mozwebqa)
        learn_pg.open("en-US/learn")
        Assert.true(learn_pg.is_footer_img_visible)
        Assert.true(learn_pg.is_footer_bar_feedback_link_visible)
        Assert.true(learn_pg.is_footer_licenses_link_visible)
        Assert.true(learn_pg.is_footer_about_link_visible)
        Assert.true(learn_pg.is_footer_privacy_link_visible)
        Assert.true(learn_pg.is_footer_help_link_visible)

    def test_header_links_visible(self, mozwebqa):
        learn_pg = DemoPage(mozwebqa)
        learn_pg.open("en-US/learn")
        Assert.true(learn_pg.is_topics_link_visible)
        Assert.true(learn_pg.is_docs_link_visible)
        Assert.true(learn_pg.is_demos_link_visible)
        Assert.true(learn_pg.is_learning_link_visible)
        Assert.true(learn_pg.is_forums_link_visible)
        Assert.true(learn_pg.is_search_mdn_link_visible)
        Assert.true(learn_pg.is_learning_link_visible)
        Assert.true(learn_pg.is_forums_link_visible)
        Assert.true(learn_pg.is_search_mdn_link_visible)

    def test_page_elements_are_visible(self, mozwebqa):
        learn_pg = LearnPage(mozwebqa)
        learn_pg.go_to_learn_page()
        Assert.true(learn_pg.is_make_web_better_visible)
        Assert.true(learn_pg.is_html_locator_visible)
        Assert.true(learn_pg.is_css_locator_visible)
        Assert.true(learn_pg.is_javascript_link_visible)
        Assert.true(learn_pg.is_blackboard_image_visible)
        Assert.true(learn_pg.is_p2p_image_visible)
