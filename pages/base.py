#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page
from mocks.mock_user import MockUser
from persona_test_user import PersonaTestUser


class BasePage(Page):

    _sign_in_with_locator = (By.CSS_SELECTOR, '.oauth-login-options')
    _persona_login_locator = (By.CSS_SELECTOR, '.launch-persona-login')
    _create_new_profile_button = (By.CSS_SELECTOR, '.submit > button')
    _username_input_field_locator = (By.ID, 'id_username')

    def _go_to_page(self, path_to_page):
        self.selenium.maximize_window()
        self.selenium.get(self.base_url + path_to_page)
        self.is_the_current_page

    def link_destination(self, locator):
        link = self.selenium.find_element(*locator)
        return link.get_attribute('href')

    def sign_in(self, user=None):
        credentials = isinstance(user, MockUser) and \
            user or self.testsetup.credentials.get(user, PersonaTestUser().create_user())

        bid_login = self.click_sign_in_to_register(expect='new')
        bid_login.sign_in(credentials['email'], credentials['password'])
        if user == "default":
            WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_signed_in)

    def click_sign_in_to_register(self, expect='new'):
        hover_element = self.selenium.find_element(*self._sign_in_with_locator)
        ActionChains(self.selenium).\
            move_to_element(hover_element).\
            perform()
        self.selenium.find_element(*self._persona_login_locator).click()

        from browserid.pages.sign_in import SignIn
        return SignIn(self.selenium, self.timeout, expect=expect)

    def enter_new_user_profile(self, _username):
        self.selenium.find_element(*self._username_input_field_locator).send_keys(_username)
        self.selenium.find_element(*self._create_new_profile_button).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_signed_in)

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

        _sign_out_locator = (By.LINK_TEXT, 'Sign out')
        _profile_link_locator = (By.CSS_SELECTOR, '.user-state a')
        _search_locator = (By.ID, 'q')
        _zones_submenu_locator = (By.ID, 'nav-zones-submenu')
        _zones_menu_locator = (By.CSS_SELECTOR, '#main-nav > ul > li:nth-of-type(1) > a')
        _web_platform_submenu_locator = (By.ID, 'nav-platform-submenu')
        _web_platform_menu_locator = (By.CSS_SELECTOR, '#main-nav > ul > li:nth-of-type(2) > a')
        _tools_locator = (By.CSS_SELECTOR, '#main-nav > ul > li:nth-of-type(3) > a')
        _demos_locator = (By.CSS_SELECTOR, '#main-nav > ul > li:nth-of-type(4) > a')
        _connect_locator = (By.CSS_SELECTOR, '#main-nav > ul > li:nth-of-type(5) > a')

        main_nav_links_list = [
            {
                'locator': _zones_menu_locator,
                'url_suffix': '/docs/Zones',
            }, {
                'locator': _web_platform_menu_locator,
                'url_suffix': '/docs/Web',
            }, {
                'locator': _tools_locator,
                'url_suffix': '/docs/Tools',
            }, {
                'locator': _demos_locator,
                'url_suffix': '/demos/',
            }, {
                'locator': _connect_locator,
                'url_suffix': '/docs/Mozilla/Connect',
            }
        ]

        zones_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(1) > a'),
                'url_suffix': '/Add-ons',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(2) > a'),
                'url_suffix': '/Apps',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(3) > a'),
                'url_suffix': '/Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(4) > a'),
                'url_suffix': '/Marketplace',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(5) > a'),
                'url_suffix': '/Firefox_OS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-zones-submenu li:nth-of-type(6) > a'),
                'url_suffix': '/Persona',
            }
        ]

        get_involved_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(1) > a'),
                'url_suffix': '/Join_the_community',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(2) > a'),
                'url_suffix': '/Contributing'
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community > li:nth-of-type(3) > a'),
                'url_suffix': '/events',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community> li:nth-of-type(4) > a'),
                'url_suffix': '/Follow_what_s_happening',
            }
        ]

        web_platform_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(1) > a'),
                'url_suffix': '/HTML',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(2) > a'),
                'url_suffix': '/CSS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(3) > a'),
                'url_suffix': '/JavaScript',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(4) > a'),
                'url_suffix': '/Graphics',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(5) > a'),
                'url_suffix': '/API',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(6) > a'),
                'url_suffix': '/Apps',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(1) li:nth-of-type(7) > a'),
                'url_suffix': '/MathML',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(1) > a'),
                'url_suffix': '/Tutorials',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(2) > a'),
                'url_suffix': '/Reference',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(3) > a'),
                'url_suffix': '/Guide',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(4) > a'),
                'url_suffix': '/Accessibility',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(5) > a'),
                'url_suffix': '/demos/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-platform-submenu > div:nth-of-type(2) li:nth-of-type(6) > a'),
                'url_suffix': '/docs/Web',
            }
        ]

        @property
        def is_web_platform_submenu_displayed(self):
            return self.is_element_visible(self._web_platform_submenu_locator)

        def open_web_platform_menu(self):
            web_platform_menu = self.selenium.find_element(*self._web_platform_menu_locator)
            ActionChains(self.selenium).move_to_element(web_platform_menu).perform()
            WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_web_platform_submenu_displayed)

        @property
        def is_zones_submenu_displayed(self):
            return self.is_element_visible(self._zones_submenu_locator)

        def open_zones_menu(self):
            zones_menu = self.selenium.find_element(*self._zones_menu_locator)
            ActionChains(self.selenium).move_to_element(zones_menu).perform()
            WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_zones_submenu_displayed)

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
                'url_suffix': '/en-US/docs/Project:MDN/About#Copyrights_and_licenses',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(3)'),
                'url_suffix': '/en-US/docs/Project:MDN/About',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(4)'),
                'url_suffix': '//github.com/mozilla/kuma',
            }, {
                'locator': (By.CSS_SELECTOR, 'footer p > bdi > a:nth-child(5)'),
                'url_suffix': '//www.mozilla.org/privacy/websites/',
            }
        ]

        _logo_locator = (By.CSS_SELECTOR, 'footer p')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)
