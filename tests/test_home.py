#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestHome:

    @pytest.mark.nondestructive
    def test_header_links(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        Assert.true(home_pg.header.is_topics_link_visible)
        Assert.true(home_pg.header.is_docs_link_visible)
        Assert.true(home_pg.header.is_demos_link_visible)
        Assert.true(home_pg.header.is_learning_link_visible)
        Assert.true(home_pg.header.is_community_link_visible)
        Assert.true(home_pg.header.is_search_visible)

    @pytest.mark.nondestructive
    def test_footer_links(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        Assert.true(home_pg.footer.is_logo_visible)
        Assert.true(home_pg.footer.is_feedback_link_visible)
        Assert.true(home_pg.footer.is_licenses_link_visible)
        Assert.true(home_pg.footer.is_about_link_visible)
        Assert.true(home_pg.footer.is_privacy_link_visible)
        Assert.true(home_pg.footer.is_help_link_visible)
