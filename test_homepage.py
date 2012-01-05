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
from unittestzero import Assert
from pages.desktop.demo import DemoPage


class TestHomepage:

    def test_header_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.is_topics_link_visible)
        Assert.true(demo_pg.is_docs_link_visible)
        Assert.true(demo_pg.is_demos_link_visible)
        Assert.true(demo_pg.is_learning_link_visible)
        Assert.true(demo_pg.is_forums_link_visible)
        Assert.true(demo_pg.is_search_mdn_link_visible)
        Assert.true(demo_pg.is_demo_studio_link_visible)
        Assert.true(demo_pg.is_search_mdn_link_visible)
        Assert.true(demo_pg.is_learn_more_link_visible)

    def test_footer_links(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.go_to_demo_page()
        Assert.true(demo_pg.is_footer_img_visible)
        Assert.true(demo_pg.is_footer_rss_link_visible)
        Assert.true(demo_pg.is_footer_bar_feedback_link_visible)
        Assert.true(demo_pg.is_footer_licenses_link_visible)
        Assert.true(demo_pg.is_footer_about_link_visible)
        Assert.true(demo_pg.is_footer_privacy_link_visible)
        Assert.true(demo_pg.is_footer_help_link_visible)

    def test_demo_title(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.open("/demos")
        totalDemoTitles = demo_pg.get_demo_title_count()
        for i in range(1, totalDemoTitles + 1):
            Assert.true(demo_pg.is_demo_title_visible(i))

    def test_demo_image(self, mozwebqa):
        demo_pg = DemoPage(mozwebqa)
        demo_pg.open("/demos")
        totalDemoImages = demo_pg.get_demo_image_count()
        for i in range(1, totalDemoImages + 1):
            Assert.true(demo_pg.is_demo_image_visible(i))
