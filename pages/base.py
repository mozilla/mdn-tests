#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class BasePage(Page):

    def link_destination(self, locator):
        link = self.selenium.find_element(*locator)
        return link.get_attribute('href')

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

        _sign_in_locator = (By.CSS_SELECTOR, '#masthead .browserid-signin')
        _sign_out_locator = (By.LINK_TEXT, 'Sign out')
        _profile_link_locator = (By.CSS_SELECTOR, '.user-state a')
        _search_locator = (By.ID, 'q')

        main_nav_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-main-topics a'),
                'url_suffix': '#nav-sub-topics',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-docs a'),
                'url_suffix': '/docs',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-demos a'),
                'url_suffix': '/demos/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-learning a'),
                'url_suffix': '/learn',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-community a'),
                'url_suffix': '#nav-sub-community',
            }
        ]

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
        def is_search_present(self):
            return self.is_element_present(self._search_locator)

        @property
        def browser_id_info(self):
            return self.BrowserIDInfoRegion(self.testsetup)

        class BrowserIDInfoRegion(Page):

            _sign_in_locator = (By.CSS_SELECTOR, '.browserid-info .browserid-signin')

            def click_sign_in(self):
                self.selenium.find_element(*self._sign_in_locator).click()

    class FooterRegion(Page):

        footer_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#footbar > div.wrap > p > a'),
                'url_suffix': 'mdn.uservoice.com/forums/51389-mdn-website-feedback-http-developer-mozilla-org',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(1)'),
                'url_suffix': '/docs/Project:Copyrights',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(2)'),
                'url_suffix': '/docs/Project:About',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(3)'),
                'url_suffix': '/privacy',
            }
        ]

        _logo_locator = (By.CSS_SELECTOR, '#legal > img')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)
