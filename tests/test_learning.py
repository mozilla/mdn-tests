#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.learning import LearningPage

from unittestzero import Assert
import pytest


class TestLearning:

    @pytest.mark.nondestructive
    def test_footer_links_visible(self, mozwebqa):
        learning_pg = LearningPage(mozwebqa)
        learning_pg.go_to_learning_page()
        Assert.true(learning_pg.footer.is_logo_visible)
        Assert.true(learning_pg.footer.is_feedback_link_visible)
        Assert.true(learning_pg.footer.is_licenses_link_visible)
        Assert.true(learning_pg.footer.is_about_link_visible)
        Assert.true(learning_pg.footer.is_privacy_link_visible)
        Assert.true(learning_pg.footer.is_help_link_visible)

    @pytest.mark.nondestructive
    def test_header_links_visible(self, mozwebqa):
        learning_pg = LearningPage(mozwebqa)
        learning_pg.go_to_learning_page()
        Assert.true(learning_pg.header.is_topics_link_visible)
        Assert.true(learning_pg.header.is_docs_link_visible)
        Assert.true(learning_pg.header.is_demos_link_visible)
        Assert.true(learning_pg.header.is_learning_link_visible)
        Assert.true(learning_pg.header.is_community_link_visible)
        Assert.true(learning_pg.header.is_search_visible)

    @pytest.mark.nondestructive
    def test_page_elements_are_visible(self, mozwebqa):
        learning_pg = LearningPage(mozwebqa)
        learning_pg.go_to_learning_page()
        Assert.true(learning_pg.is_page_title_visible)
        Assert.true(learning_pg.is_html_locator_visible)
        Assert.true(learning_pg.is_css_locator_visible)
        Assert.true(learning_pg.is_javascript_link_visible)
        Assert.true(learning_pg.is_blackboard_visible)
        Assert.true(learning_pg.is_p2p_image_visible)
