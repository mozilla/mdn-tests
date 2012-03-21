#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class BasePage(Page):

    def sign_in(self, user='default'):
        credentials = self.testsetup.credentials[user]
        self.header.click_sign_in()
        self.header.browser_id_info.click_sign_in()
        from browserid import BrowserID
        browser_id = BrowserID(self.selenium, self.timeout)
        browser_id.sign_in(credentials['email'], credentials['password'])
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self.header._sign_out_locator))

    @property
    def is_signed_in(self):
        return self.header.is_sign_out_visible

    @property
    def header(self):
        return self.HeaderRegion(self.testsetup)

    @property
    def footer(self):
        return self.FooterRegion(self.testsetup)

    class HeaderRegion(Page):

        _topics_link_locator = (By.CSS_SELECTOR, '#nav-main-topics a')
        _docs_link_locator = (By.CSS_SELECTOR, '#nav-main-docs a')
        _demos_link_locator = (By.CSS_SELECTOR, '#nav-main-demos a')
        _learning_link_locator = (By.CSS_SELECTOR, '#nav-main-learning a')
        _community_link_locator = (By.CSS_SELECTOR, '#nav-main-community a')
        _sign_in_locator = (By.CSS_SELECTOR, '#masthead .browserid-signin')
        _sign_out_locator = (By.LINK_TEXT, 'Sign out')
        _profile_link_locator = (By.CSS_SELECTOR, '.user-state a')
        _search_locator = (By.ID, 'q')

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
        def is_community_link_visible(self):
            return self.is_element_visible(self._community_link_locator)

        def click_sign_in(self):
            self.selenium.find_element(*self._sign_in_locator).click()

        @property
        def is_sign_out_visible(self):
            return self.is_element_visible(self._sign_out_locator)

        def click_sign_out(self):
            self.selenium.find_element(*self._sign_out_locator).click()

        def click_profile_link(self):
            self.selenium.find_element(*self._profile_link_locator).click()
            from pages.profile import ProfilePage
            return ProfilePage(self.testsetup)

        @property
        def is_search_visible(self):
            return self.is_element_visible(self._search_locator)

        @property
        def browser_id_info(self):
            return self.BrowserIDInfoRegion(self.testsetup)

        class BrowserIDInfoRegion(Page):
    
            _sign_in_locator = (By.CSS_SELECTOR, '.browserid-info .browserid-signin')
    
            def click_sign_in(self):
                self.selenium.find_element(*self._sign_in_locator).click()


    class FooterRegion(Page):

        _logo_locator = (By.CSS_SELECTOR, '#legal > img')
        _feedback_link_locator = (By.CSS_SELECTOR, '#footbar > div.wrap > p > a')
        _licenses_link_locator = (By.CSS_SELECTOR, '#legal > p > a:nth-child(1)')
        _about_link_locator = (By.CSS_SELECTOR, '#legal > p > a:nth-child(2)')
        _privacy_link_locator = (By.CSS_SELECTOR, '#legal > p > a:nth-child(3)')
        _help_link_locator = (By.CSS_SELECTOR, '#legal > p > a:nth-child(4)')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)

        @property
        def is_feedback_link_visible(self):
            return self.is_element_visible(self._feedback_link_locator)

        @property
        def is_licenses_link_visible(self):
            return self.is_element_visible(self._licenses_link_locator)

        @property
        def is_about_link_visible(self):
            return self.is_element_visible(self._about_link_locator)

        @property
        def is_privacy_link_visible(self):
            return self.is_element_visible(self._privacy_link_locator)

        @property
        def is_help_link_visible(self):
            return self.is_element_visible(self._help_link_locator)
