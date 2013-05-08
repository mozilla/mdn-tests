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
        _docs_menu_locator = (By.CSS_SELECTOR, '#nav-main-docs a')
        _make_apps_menu_locator = (By.CSS_SELECTOR, '#nav-main-apps a')
        _get_involved_menu_locator = (By.CSS_SELECTOR, '#nav-main-community a')
        _build_use_firefox_menu_locator = (By.CSS_SELECTOR, '#nav-main-firefox a')
        _demos_menu_locator = (By.CSS_SELECTOR, '#nav-main-demos a')

        main_nav_links_list = [
            {
                'locator': _docs_menu_locator,
                'url_suffix': '#nav-sub-docs',
            }, {
                'locator': _make_apps_menu_locator,
                'url_suffix': '/developers/',
            }, {
                'locator': _build_use_firefox_menu_locator,
                'url_suffix': '#nav-sub-firefox',
            }, {
                'locator': _demos_menu_locator,
                'url_suffix': '/demos/',
            }, {
                'locator': _get_involved_menu_locator,
                'url_suffix': '#nav-sub-community',
            }
        ]

        build_use_firefox_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox li:nth-child(1) a'),
                'url_suffix': '/Firefox_OS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox li:nth-child(2) a'),
                'url_suffix': '/Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox li:nth-child(3) a'),
                'url_suffix': '/Firefox_for_Android',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-firefox li:nth-child(4) a'),
                'url_suffix': '/Addons',
            }
        ]

        docs_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(1) a'),
                'url_suffix': '/docs/Web/HTML',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(2) a'),
                'url_suffix': '/docs/Web/CSS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(3) a'),
                'url_suffix': '/docs/Web/JS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(4) a'),
                'url_suffix': '/docs/Web/Graphics',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(5) a'),
                'url_suffix': '/docs/Web/API',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(6) a'),
                'url_suffix': '/docs/Apps',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(7) a'),
                'url_suffix': '/docs/Tools',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(8) a'),
                'url_suffix': '/docs/Web/MathML',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(9) a'),
                'url_suffix': '/docs/Web',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(1) a'),
                'url_suffix': '/docs/Web/Tutorials',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(2) a'),
                'url_suffix': '/docs/Web/References',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(3) a'),
                'url_suffix': '/docs/Web/Guide',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(4) a'),
                'url_suffix': '/demos/',
            }
        ]

        get_involved_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(1) a'),
                'url_suffix': '/Join_the_community',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(2) a'),
                'url_suffix': '/Contributing',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(3) a'),
                'url_suffix': '/events',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(4) a'),
                'url_suffix': '/Follow_what_s_happening',
            }
        ]

        def open_build_use_firefox_menu(self):
            self.selenium.find_element(*self._build_use_firefox_menu_locator).click()

        def open_docs_menu(self):
            self.selenium.find_element(*self._docs_menu_locator).click()

        def open_get_involved_menu(self):
            self.selenium.find_element(*self._get_involved_menu_locator).click()

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
                'url_suffix': '/docs/Project:Feedback',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(1)'),
                'url_suffix': '/docs/Project:Copyrights',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(2)'),
                'url_suffix': '/docs/Project:About',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(3)'),
                'url_suffix': 'https://github.com/mozilla/kuma/',
            }, {
                'locator': (By.CSS_SELECTOR, '#legal > p > a:nth-child(4)'),
                'url_suffix': '/privacy',
            }
        ]

        _logo_locator = (By.CSS_SELECTOR, '#legal > img')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)
