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
from page import Page


class DemoPage(Page):  
    _count = 1
    _topics_link_locator = "css=.toggle"
    _docs_link_locator = "css=.docs"
    _demos_link_locator = "css=.demos"
    _learning_link_locator = "css=.learning"
    _forums_link_locator = "css=.community"
    _join_mdn_locator = "css=.wrap>p:nth-child(1)>a"
    _login_locator = "css=.wrap>p:nth-child(2)>a"
    _search_mdn_locator ="css=#q"
    _demo_studio_locator = "css=#demos-head>h1"
    _learn_more_locator = "css=.learnmore>a"
    _submit_demo_locator = "css=.demo-buttons>li.submit"
    _join_derby_button_locator = "css=#derby-cta>a"
    _featured_demo_header_locator = "css=#featured-demos>header>h2"
    _browse_by_technology_locator = "css=#div#demo-tags>a"
    _tag_count = "css=#tags-list>li"
    _total_demo_count_locator = "css=.count"
    _up_and_coming_sort_locator = "css=.sort>li:nth-child(1)>a"
    _most_viewed_sort_locator = "css=.sort>li:nth-child(2)>a"
    _most_liked_sort_locator = "css=.sort>li:nth-child(3)>a"
    _most_recent_sort_locator = "css=.sort>li:nth-child(1)>a"
    _demo_image_count_locator = "css=.demo>.demo-title>a>img"
    _demo_title_count_locator ="css=.demo>.demo-title>a"
    _footer_img_locator = "css=#legal>img"
    _footer_rss_link_locator = "css=.feed>a"
    _footer_bar_feedback_link_locator = "css=#footbar>div.wrap>p>a"
    _footer_licenses_link_locator = "css=#legal>p>a:nth-child(1)"
    _footer_about_link_locator= "css=#legal>p>a:nth-child(2)"
    _footer_privacy_link_locator = "css=#legal>p>a:nth-child(3)"
    _footer_help_link_locator = "css=#legal>p>a:nth-child(4)"

    def go_to_demo_page(self):
        self.open("/demos")

    @property
    def is_topics_link_visible(self):
        return self.is_element_visible(self._topics_link_locator)

    @property
    def is_docs_link_visible(self):
        return self.is_element_visible(self._docs_link_locator)

    @property
    def is_demos_link_visible(self):
        return self.is_element_visible(self._demos_link_locator)

    @property
    def is_learning_link_visible(self):
        return self.is_element_visible(self._learning_link_locator)

    @property
    def is_forums_link_visible(self):
        return self.is_element_visible(self._forums_link_locator)

    @property
    def is_join_mdn_link_visible(self):
        return self.is_element_visible(self._join_mdn_locator)

    @property
    def is_login_link_visible(self):
        return self.is_element_visible(self._login_locator)

    @property
    def is_search_mdn_link_visible(self):
        return self.is_element_visible(self._search_mdn_locator)

    @property
    def is_demo_studio_link_visible(self):
        return self.is_element_visible(self._demo_studio_locator)

    @property
    def is_learn_more_link_visible(self):
        return self.is_element_visible(self._learn_more_locator)

    @property
    def is_submit_demo_link_visible(self):
        return self.is_element_visible(self._submit_demo_locator)

    @property
    def is_join_derby_link_visible(self):
        return self.is_element_visible(self._jon_derby_locator)

    @property
    def is_featured_demo_header_visible(self):
        return self.is_element_visible(self._featured_demo_header_locator)

    @property
    def is_browse_by_technology_link_visible(self):
        return self.is_element_visible(self._browse_by_technology_locator)

    def get_tag_count(self):
        return self.get_css_count(self._tag_count)

    def get_tag(self, count):
        _tag = "css=#tags-list>li:nth-child(%d)" % count
        return self.is_element_visible(_tag)

    def visit_tag_url(self, count):
        _tag = "css=#tags-list>li:nth-child(%d)" % count
        self.click(_tag, True)
        return self.get_url_current_page()

    @property
    def is_total_demo_count_visible(self):
        return self.is_element_visible(self._total_demo_count)

    @property
    def is_up_and_coming_sort_visible(self):
        return self.is_element_visible(self._up_and_coming_sort_locator)

    @property
    def is_most_viewed_sort_visible(self):
        return self.is_element_visible(self._most_viewed_sort_locator)

    @property
    def is_most_liked_sort_visible(self):
        return self.is_element_visible(self._most_liked_sort_locator)

    @property
    def is_most_recent_sort_visible(self):
        return self.is_element_visible(self._most_recent_sort_locator)

    def get_demo_image_count(self):
        return self.get_css_count(self._demo_image_count_locator)

    def is_demo_image_visible(self, count):
        _demo_image_locator = \
        "css=.demo:nth-child(%d)>.demo-title>a>img" % count
        return self.is_element_visible(_demo_image_locator)

    def get_demo_title_count(self):
        return self.get_css_count(self._demo_title_count_locator)

    def is_demo_title_visible(self, count):
        _demo_title_locator = \
        "css=.demo:nth-child(%d)>.demo-title>a" % count
        return self.is_element_visible(_demo_title_locator)

    @property
    def is_footer_img_visible(self):
        return self.is_element_visible(self._footer_img_locator)

    @property
    def is_footer_rss_link_visible(self):
        return self.is_element_visible(self._footer_rss_link_locator)

    @property
    def is_footer_bar_feedback_link_visible(self):
        return self.is_element_visible(self._footer_bar_feedback_link_locator)

    @property
    def is_footer_licenses_link_visible(self):
        return self.is_element_visible(self._footer_licenses_link_locator)

    @property
    def is_footer_about_link_visible(self):
        return self.is_element_visible(self._footer_about_link_locator)

    @property
    def is_footer_privacy_link_visible(self):
        return self.is_element_visible(self._footer_privacy_link_locator)

    @property
    def is_footer_help_link_visible(self):
        return self.is_element_visible(self._footer_help_link_locator)
