#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.derby import DerbyPage

from unittestzero import Assert
import pytest


class TestDevDerby:

    @pytest.mark.nondestructive
    def test_header_links(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()
        Assert.true(derby_pg.header.is_topics_link_visible)
        Assert.true(derby_pg.header.is_docs_link_visible)
        Assert.true(derby_pg.header.is_demos_link_visible)
        Assert.true(derby_pg.header.is_learning_link_visible)
        Assert.true(derby_pg.header.is_community_link_visible)
        Assert.true(derby_pg.header.is_search_visible)

    @pytest.mark.nondestructive
    def test_are_footer_links_visible(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()
        Assert.true(derby_pg.footer.is_logo_visible)
        Assert.true(derby_pg.footer.is_feedback_link_visible)
        Assert.true(derby_pg.footer.is_licenses_link_visible)
        Assert.true(derby_pg.footer.is_about_link_visible)
        Assert.true(derby_pg.footer.is_privacy_link_visible)
        Assert.true(derby_pg.footer.is_help_link_visible)

    @pytest.mark.xfail(reason="No derby winners on production yet")
    @pytest.mark.nondestructive
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
        Assert.true(derby_pg.is_demos_link_visible)
        Assert.true(derby_pg.is_articles_link_visible)
        Assert.equal(derby_pg.prizes_heading, 'PRIZES')
        Assert.true(derby_pg.is_prizes_image_visible)

    @pytest.mark.nondestructive
    def test_judge_photos_visible(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()

        derby_pg.click_judging_link()
        all_judges = derby_pg.current_judges + derby_pg.past_judges
        Assert.greater(len(all_judges), 0)

        for judge in all_judges:
            Assert.true(judge.is_photo_visible)

    @pytest.mark.nondestructive
    def test_are_previous_challenges_visible(self, mozwebqa):
        derby_pg = DerbyPage(mozwebqa)
        derby_pg.go_to_derby_page()

        derby_pg.click_previous_challenges_link()
        Assert.greater(len(derby_pg.previous_challenges), 0)
        for challenge in derby_pg.previous_challenges:
            Assert.true(challenge.is_name_visible)
