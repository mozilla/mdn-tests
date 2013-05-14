#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.learning import LearningPage

from unittestzero import Assert
import pytest


class TestLearning:

    @pytest.mark.nondestructive
    def test_main_nav_links_are_visible(self, mozwebqa):
        learning_page = LearningPage(mozwebqa)
        learning_page.go_to_page()
        bad_links = []
        for link in learning_page.header.main_nav_links_list:
            if not learning_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(learning_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_footer_links_are_visible(self, mozwebqa):
        learning_page = LearningPage(mozwebqa)
        learning_page.go_to_page()
        bad_links = []
        for link in learning_page.footer.footer_links_list:
            if not learning_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(learning_page.header.is_search_present)
        Assert.true(learning_page.footer.is_logo_visible)

    @pytest.mark.nondestructive
    def test_page_elements_are_visible(self, mozwebqa):
        learning_page = LearningPage(mozwebqa)
        learning_page.go_to_page()
        Assert.true(learning_page.is_page_title_visible)
        Assert.true(learning_page.is_html_locator_visible)
        Assert.true(learning_page.is_css_locator_visible)
        Assert.true(learning_page.is_javascript_link_visible)
        Assert.true(learning_page.is_blackboard_visible)
        Assert.true(learning_page.is_p2p_image_visible)
