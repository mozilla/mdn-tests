#!/usr/bin/env python
#
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is MDN
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL,and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from selenium import selenium
from unittestzero import Assert
from demo_page import DemoPage
from derby_page import DerbyPage
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
