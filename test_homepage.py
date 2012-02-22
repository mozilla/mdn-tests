#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.demo import DemoPage


class TestHomepage:

    def test_header_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.is_topics_link_visible)
        Assert.true(demo_pg.is_docs_link_visible)
        Assert.true(demo_pg.is_demos_link_visible)
        Assert.true(demo_pg.is_learning_link_visible)
        Assert.true(demo_pg.is_forums_link_visible)
        Assert.true(demo_pg.is_search_mdn_link_visible)
        Assert.true(demo_pg.is_demo_studio_link_visible)
        Assert.true(demo_pg.is_search_mdn_link_visible)
        Assert.true(demo_pg.is_learn_more_link_visible)

    def test_footer_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.is_footer_img_visible)
        Assert.true(demo_pg.is_footer_rss_link_visible)
        Assert.true(demo_pg.is_footer_bar_feedback_link_visible)
        Assert.true(demo_pg.is_footer_licenses_link_visible)
        Assert.true(demo_pg.is_footer_about_link_visible)
        Assert.true(demo_pg.is_footer_privacy_link_visible)
        Assert.true(demo_pg.is_footer_help_link_visible)

    def test_demo_title(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.open("/demos")
        totalDemoTitles = demo_pg.get_demo_title_count()
        for i in range(1, totalDemoTitles + 1):
            Assert.true(demo_pg.is_demo_title_visible(i))

    def test_demo_image(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.open("/demos")
        totalDemoImages = demo_pg.get_demo_image_count()
        for i in range(1, totalDemoImages + 1):
            Assert.true(demo_pg.is_demo_image_visible(i))
