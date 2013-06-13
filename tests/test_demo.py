#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.demo import DemoPage

from unittestzero import Assert
import pytest


class TestDemo:

    @pytest.mark.nondestructive
    def test_main_nav_links_are_visible(self, mozwebqa):
        demo_page = DemoPage(mozwebqa)
        demo_page.go_to_page()
        bad_links = []
        for link in demo_page.header.main_nav_links_list:
            if not demo_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(demo_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_footer_links_are_visible(self, mozwebqa):
        demo_page = DemoPage(mozwebqa)
        demo_page.go_to_page()
        bad_links = []
        for link in demo_page.footer.footer_links_list:
            if not demo_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(demo_page.header.is_search_present)
        Assert.true(demo_page.footer.is_logo_visible)

    @pytest.mark.nondestructive
    def test_page_elements_are_visible(self, mozwebqa):
        demo_page = DemoPage(mozwebqa)
        demo_page.go_to_page()
        Assert.true(demo_page.is_demo_studio_link_visible)
        Assert.true(demo_page.is_learn_more_link_visible)
        Assert.true(demo_page.is_rss_link_visible)

    @pytest.mark.nondestructive
    def test_demos(self, mozwebqa):
        demo_page = DemoPage(mozwebqa)
        demo_page.go_to_page()
        for demo in demo_page.demos:
            Assert.true(demo.is_title_visible)
            Assert.true(demo.is_thumbnail_visible)
