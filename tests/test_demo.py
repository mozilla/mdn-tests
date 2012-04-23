#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from pages.demo import DemoPage

from unittestzero import Assert
import pytest


class TestDemo:

    @pytest.mark.nondestructive
    def test_header_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.header.is_topics_link_visible)
        Assert.true(demo_pg.header.is_docs_link_visible)
        Assert.true(demo_pg.header.is_demos_link_visible)
        Assert.true(demo_pg.header.is_learning_link_visible)
        Assert.true(demo_pg.header.is_community_link_visible)
        Assert.true(demo_pg.header.is_search_visible)

    @pytest.mark.nondestructive
    def test_footer_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.footer.is_logo_visible)
        Assert.true(demo_pg.footer.is_feedback_link_visible)
        Assert.true(demo_pg.footer.is_licenses_link_visible)
        Assert.true(demo_pg.footer.is_about_link_visible)
        Assert.true(demo_pg.footer.is_privacy_link_visible)
        Assert.true(demo_pg.footer.is_help_link_visible)

    @pytest.mark.nondestructive
    def test_page_elements_are_visible(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.is_demo_studio_link_visible)
        Assert.true(demo_pg.is_learn_more_link_visible)
        Assert.true(demo_pg.is_rss_link_visible)

    @pytest.mark.nondestructive
    def test_demos(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        for demo in demo_pg.demos:
            Assert.true(demo.is_title_visible)
            Assert.true(demo.is_thumbnail_visible)
