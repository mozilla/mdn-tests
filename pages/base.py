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

        _sign_in_locator = (By.CSS_SELECTOR, '.browserid .signin')
        _sign_out_locator = (By.LINK_TEXT, 'Sign out')
        _profile_link_locator = (By.CSS_SELECTOR, '.user-state a')
        _search_locator = (By.ID, 'q')
        _read_docs_locator = (By.CSS_SELECTOR, '#nav-main-docs a')
        _make_apps_locator = (By.CSS_SELECTOR, '#nav-main-apps a')
        _use_firefox_locator = (By.CSS_SELECTOR, '#nav-main-firefox a')
        _submit_demos_locator = (By.CSS_SELECTOR, '#nav-main-demos a')
        _get_involved_locator = (By.CSS_SELECTOR, '#nav-main-community a')

        main_nav_links_list = [
            {
                'locator': _read_docs_locator,
                'url_suffix': '#nav-sub-docs',
            }, {
                'locator': _make_apps_locator,
                'url_suffix': 'https://marketplace.firefox.com/developers/?menu',
            }, {
                'locator': _use_firefox_locator,
                'url_suffix': '#nav-sub-firefox',
            }, {
                'locator': _submit_demos_locator,
                'url_suffix': '/demos/?menu',
            }, {
                'locator': _get_involved_locator,
                'url_suffix': '#nav-sub-community',
            }
        ]

        build_use_firefox_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox > li:nth-of-type(1) > a'),
                'url_suffix': '/Firefox_OS?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox > li:nth-of-type(2) > a'),
                'url_suffix': '/Firefox?menu'
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox > li:nth-of-type(3) > a'),
                'url_suffix': '/Mobile?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox > li:nth-of-type(4) > a'),
                'url_suffix': '/Add-ons?menu',
            }
        ]

        get_involved_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(1) > a'),
                'url_suffix': '/Join_the_community?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(2) > a'),
                'url_suffix': '/Contributing?menu'
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(3) > a'),
                'url_suffix': '/events?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community> li:nth-of-type(4) > a'),
                'url_suffix': '/Follow_what_s_happening?menu',
            }
        ]

        read_docs_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(1) > a'),
                'url_suffix': '/HTML?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(2) > a'),
                'url_suffix': '/CSS?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(3) > a'),
                'url_suffix': '/JavaScript?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(4) > a'),
                'url_suffix': '/Graphics?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(5) > a'),
                'url_suffix': '/API?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(6) > a'),
                'url_suffix': '/Apps?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul > li:nth-of-type(7) > a'),
                'url_suffix': '/tools?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(1) > ul >  li:nth-of-type(8) > a'),
                'url_suffix': '/MathML?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(1) > a'),
                'url_suffix': '/Tutorials?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(2) > a'),
                'url_suffix': '/Reference?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(3) > a'),
                'url_suffix': '/Guide?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(4) > a'),
                'url_suffix': '/Accessibility?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(5) > a'),
                'url_suffix': '/demos/?menu',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs > ul > li:nth-of-type(2) > ul > li:nth-of-type(6) > a'),
                'url_suffix': '/docs?menu',
            }
        ]

        def open_read_docs_menu(self):
            self.selenium.find_element(*self._read_docs_locator).click()

        def open_use_firefox_menu(self):
            self.selenium.find_element(*self._use_firefox_locator).click()

        def open_get_involved_menu(self):
            self.selenium.find_element(*self._get_involved_locator).click()

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

    class FooterRegion(Page):

        footer_links_list = [
            {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(2)'),
                'url_suffix': '/en-US/docs/Project:Copyrights',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(3)'),
                'url_suffix': '/en-US/docs/Project:About',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(4)'),
                'url_suffix': '//github.com/mozilla/kuma',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(5)'),
                'url_suffix': '//www.mozilla.org/en-US/privacy',
            }
        ]

        _logo_locator = (By.CSS_SELECTOR, 'footer p')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)
