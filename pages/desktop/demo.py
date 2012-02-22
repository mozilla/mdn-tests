#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from page import Page


class ProfilePage(Page):
    _login_link_locator = "css=.minor > .wrap > p.user-state > a:nth-of-type(2)"
    _username_locator = "css=#text-username"
    _password_locator = "css=#password-password"
    _login_button_locator = "css=.input-button"
    _nickname_locator = "css=.nickname"
    _irc_locator = "css=.irc"
    _company_locator = "css=.org"
    _title_locator = "css=.title"
    _photo_locator = "css=.photo"
    _website_locator = "css=.website > .url"
    _twitter_locator = "css=.twitter > .url"
    _github_locator = "css=.github > .url"
    _docs_userpage_locator = "css=.docs > .url"

    def go_to_profile_page(self):
        self.open("/en-US/profiles/testaccount/")

    def log_user_in(self, user="default"):
        self.open("/Special:UserLogin?returntotitle=%2Fen-US%2Fprofiles%2Ftestaccount%2F")
        credentials = self.testsetup.credentials[user]
        self.selenium.type(self._username_locator, credentials['username'])
        self.selenium.type(self._password_locator, credentials['password'])
        self.selenium.click(self._login_button_locator)
        self.selenium.wait_for_page_to_load(self.timeout)

    @property
    def is_nickname_visible(self):
        return self.is_element_visible(self._nickname_locator)

    @property
    def is_irc_link_visible(self):
        return self.is_element_visible(self._irc_locator)

    @property
    def is_company_link_visible(self):
        return self.is_element_visible(self._company_locator)

    @property
    def is_title_link_visible(self):
        return self.is_element_visible(self._title_locator)


class DemoPage(Page):
    _count = 1
    _topics_link_locator = "css=.toggle"
    _docs_link_locator = "css=.docs"
    _demos_link_locator = "css=.demos"
    _learning_link_locator = "css=.learning"
    _forums_link_locator = "css=.community"
    _join_mdn_locator = "css=.wrap > p:nth-child(1) > a"
    _login_locator = "css=.wrap > p:nth-child(2) > a"
    _search_mdn_locator = "css=#q"
    _demo_studio_locator = "css=#demos-head > h1"
    _learn_more_locator = "css=.learnmore > a"
    _submit_demo_locator = "css=.demo-buttons > li.submit"
    _join_derby_button_locator = "css=#derby-cta > a"
    _featured_demo_header_locator = "css=#featured-demos > header > h2"
    _browse_by_technology_locator = "css=#div#demo-tags > a"
    _tag_count = "css=#tags-list > li"
    _total_demo_count_locator = "css=.count"
    _up_and_coming_sort_locator = "css=.sort > li:nth-child(1) > a"
    _most_viewed_sort_locator = "css=.sort > li:nth-child(2) > a"
    _most_liked_sort_locator = "css=.sort > li:nth-child(3) > a"
    _most_recent_sort_locator = "css=.sort > li:nth-child(1) > a"
    _demo_image_count_locator = "css=.demo > .demo-title > a > img"
    _demo_title_count_locator = "css=.demo > .demo-title > a"
    _footer_img_locator = "css=#legal > img"
    _footer_rss_link_locator = "css=.feed > a"
    _footer_bar_feedback_link_locator = "css=#footbar > div.wrap > p > a"
    _footer_licenses_link_locator = "css=#legal > p > a:nth-child(1)"
    _footer_about_link_locator = "css=#legal > p > a:nth-child(2)"
    _footer_privacy_link_locator = "css=#legal > p > a:nth-child(3)"
    _footer_help_link_locator = "css=#legal > p > a:nth-child(4)"

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
        _tag = "css=#tags-list > li:nth-child(%d)" % count
        return self.is_element_visible(_tag)

    def visit_tag_url(self, count):
        _tag = "css=#tags-list > li:nth-child(%d)" % count
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
        "css=.demo:nth-child(%d) > .demo-title > a > img" % count
        return self.is_element_visible(_demo_image_locator)

    def get_demo_title_count(self):
        return self.get_css_count(self._demo_title_count_locator)

    def is_demo_title_visible(self, count):
        _demo_title_locator = \
        "css=.demo:nth-child(%d) > .demo-title > a" % count
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
