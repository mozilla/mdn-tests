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
# Portions created by the Initial Developer are Copyright (C) 2011
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

from unittestzero import Assert
from pages.desktop.demo import DemoPage
from pages.desktop.learn import LearnPage


class TestLearnPage:

    def test_are_footer_links_visible(self, mozwebqa):
        learn_pg = DemoPage(mozwebqa)
        learn_pg.open("en-US/learn")
        Assert.true(learn_pg.is_footer_img_visible)
        Assert.true(learn_pg.is_footer_bar_feedback_link_visible)
        Assert.true(learn_pg.is_footer_licenses_link_visible)
        Assert.true(learn_pg.is_footer_about_link_visible)
        Assert.true(learn_pg.is_footer_privacy_link_visible)
        Assert.true(learn_pg.is_footer_help_link_visible)

    def test_header_links_visible(self, mozwebqa):
        learn_pg = DemoPage(mozwebqa)
        learn_pg.open("en-US/learn")
        Assert.true(learn_pg.is_topics_link_visible)
        Assert.true(learn_pg.is_docs_link_visible)
        Assert.true(learn_pg.is_demos_link_visible)
        Assert.true(learn_pg.is_learning_link_visible)
        Assert.true(learn_pg.is_forums_link_visible)
        Assert.true(learn_pg.is_search_mdn_link_visible)
        Assert.true(learn_pg.is_learning_link_visible)
        Assert.true(learn_pg.is_forums_link_visible)
        Assert.true(learn_pg.is_search_mdn_link_visible)

    def test_page_elements_are_visible(self, mozwebqa):
        learn_pg = LearnPage(mozwebqa)
        learn_pg.go_to_learn_page()
        Assert.true(learn_pg.is_make_web_better_visible)
        Assert.true(learn_pg.is_html_locator_visible)
        Assert.true(learn_pg.is_css_locator_visible)
        Assert.true(learn_pg.is_javascript_link_visible)
        Assert.true(learn_pg.is_blackboard_image_visible)
        Assert.true(learn_pg.is_p2p_image_visible)
