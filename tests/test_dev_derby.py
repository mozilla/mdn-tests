#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.derby import DerbyPage

from unittestzero import Assert
import pytest


class TestDevDerby:

    @pytest.mark.nondestructive
    def test_main_nav_links_are_visible(self, mozwebqa):
        derby_page = DerbyPage(mozwebqa)
        derby_page.go_to_page()
        bad_links = []
        for link in derby_page.header.main_nav_links_list:
            if not derby_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(derby_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_footer_links_are_visible(self, mozwebqa):
        derby_page = DerbyPage(mozwebqa)
        derby_page.go_to_page()
        bad_links = []
        for link in derby_page.footer.footer_links_list:
            if not derby_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(derby_page.header.is_search_present)
        Assert.true(derby_page.footer.is_logo_visible)

    @pytest.mark.xfail(reason="No derby winners on production yet")
    @pytest.mark.nondestructive
    def test_derby_links_visible(self, mozwebqa):
        derby_page = DerbyPage(mozwebqa)
        derby_page.go_to_page()
        Assert.true(derby_page.is_home_link_visible)
        Assert.true(derby_page.is_challenges_link_visible)
        Assert.true(derby_page.is_rules_link_visible)
        Assert.true(derby_page.is_judging_link_visible)
        Assert.true(derby_page.is_prizes_link_visible)
        Assert.true(derby_page.is_resources_link_visible)
        Assert.true(derby_page.is_submit_demo_link_visible)
        Assert.true(derby_page.is_demo_studio_link_visible)
        Assert.true(derby_page.is_previous_winner_banner_visible)
        Assert.true(derby_page.is_previous_winner_demo_title_visible)
        Assert.true(derby_page.is_previous_winner_name_visible)
        Assert.true(derby_page.is_previous_winner_demo_button_visible)
        Assert.true(derby_page.is_docs_link_visible)
        Assert.true(derby_page.is_demos_link_visible)
        Assert.true(derby_page.is_articles_link_visible)
        Assert.equal(derby_page.prizes_heading, 'PRIZES')
        Assert.true(derby_page.is_prizes_image_visible)

    @pytest.mark.nondestructive
    def test_judge_photos_visible(self, mozwebqa):
        derby_page = DerbyPage(mozwebqa)
        derby_page.go_to_page()

        derby_page.click_judging_link()
        all_judges = derby_page.current_judges + derby_page.past_judges
        Assert.greater(len(all_judges), 0)

        for judge in all_judges:
            Assert.true(judge.is_photo_visible)

    @pytest.mark.nondestructive
    def test_are_previous_challenges_visible(self, mozwebqa):
        derby_page = DerbyPage(mozwebqa)
        derby_page.go_to_page()

        derby_page.click_previous_challenges_link()
        Assert.greater(len(derby_page.previous_challenges), 0)
        for challenge in derby_page.previous_challenges:
            Assert.true(challenge.is_name_visible)
