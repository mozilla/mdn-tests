#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.demo import DemoPage
from pages.desktop.derby import DerbyPage
import pytest
xfail = pytest.mark.xfail


class TestDevDerbyPage:

    def test_are_footer_links_visible(self, mozwebqa):
        derby_pg = DemoPage(mozwebqa)
        derby_pg.open("en-US/demos/devderby")
        Assert.true(derby_pg.is_footer_img_visible)
        Assert.true(derby_pg.is_footer_bar_feedback_link_visible)
        Assert.true(derby_pg.is_footer_licenses_link_visible)
        Assert.true(derby_pg.is_footer_about_link_visible)
        Assert.true(derby_pg.is_footer_privacy_link_visible)
        Assert.true(derby_pg.is_footer_help_link_visible)

    @xfail(reason="No derby winners on production yet")
    def test_derby_links_visible(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()
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
        Assert.true(derby_pg.is_prizes_image_visible)
        Assert.equal(derby_pg.get_prizes_text, "Prizes")

    def test_judge_images_visible(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()
        number_of_judges = derby_pg.get_number_of_judges
        for i in range(1, number_of_judges):
            Assert.true(derby_pg.is_judge_photo_visible(i))

    def test_are_previous_challenges_present(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()
        number_of_challenges = derby_pg.get_number_of_previous_challenges
        for i in range(1, number_of_challenges):
            Assert.true(derby_pg.are_previous_challenges_visible(i))
