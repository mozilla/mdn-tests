#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from mocks.mock_user import MockUser
from persona_test_user import PersonaTestUser

from page import Page


class BasePage(Page):

    _sign_in_locator = (By.CSS_SELECTOR, '.browserid')
    _browserid_info_submenu_locator = (By.CSS_SELECTOR, '.browserid-info.sub-menu')
    _submenu_sign_in_locator = (By.CSS_SELECTOR, '.browserid-info .browserid-signin')
    _create_new_profile_button = (By.CSS_SELECTOR, '#create_user .submit > button')
    _username_input_field_locator = (By.ID, 'id_for_username')

    def link_destination(self, locator):
        link = self.selenium.find_element(*locator)
        return link.get_attribute('href')

    def sign_in(self, user=None):

        credentials = isinstance(user, MockUser) and user or self.testsetup.credentials.get(user, PersonaTestUser().create_user())

        bid_login = self.click_sign_in_register(expect='new')
        bid_login.sign_in(credentials['email'], credentials['password'])

    def click_sign_in_register(self, expect='new'):

        self.selenium.find_element(*self._sign_in_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(self._browserid_info_submenu_locator))
        self.selenium.find_element(*self._submenu_sign_in_locator).click()
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

        _sign_in_locator = (By.CSS_SELECTOR, '#masthead .browserid-signin')
        _sign_out_locator = (By.LINK_TEXT, 'Sign out')
        _profile_link_locator = (By.CSS_SELECTOR, '.user-state a')
        _search_locator = (By.ID, 'q')
        _topics_menu_locator = (By.CSS_SELECTOR, '#nav-main-topics a')
        _docs_menu_locator = (By.CSS_SELECTOR, '#nav-main-docs a')
        _community_menu_locator = (By.CSS_SELECTOR, '#nav-main-community a')
        _username_locator = (By.CSS_SELECTOR, '.user-state > li:nth-child(1) > a')

        main_nav_links_list = [
            {
                'locator': _topics_menu_locator,
                'url_suffix': '#nav-sub-topics',
            }, {
                'locator': _docs_menu_locator,
                'url_suffix': '/docs',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-demos a'),
                'url_suffix': '/demos/',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-main-learning a'),
                'url_suffix': '/learn',
            }, {
                'locator': _community_menu_locator,
                'url_suffix': '#nav-sub-community',
            }
        ]

        topics_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-web a'),
                'url_suffix': '/web',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-apps a'),
                'url_suffix': '/apps',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-mobile a'),
                'url_suffix': '/mobile',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-addons a'),
                'url_suffix': '/addons',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-mozilla a'),
                'url_suffix': '/mozilla',
            }
        ]

        docs_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(1) a'),
                'url_suffix': '/docs/HTML',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(2) a'),
                'url_suffix': '/docs/DOM',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(3) a'),
                'url_suffix': '/docs/Using_HTML5_audio_and_video_in_Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(4) a'),
                'url_suffix': '/docs/Using_HTML5_audio_and_video_in_Firefox',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(5) a'),
                'url_suffix': '/docs/SVG',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(1) ul li:nth-child(6) a'),
                'url_suffix': '/docs/WebGL',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(1) a'),
                'url_suffix': '/docs/HTML/HTML5',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(2) a'),
                'url_suffix': '/docs/WebSockets',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(3) a'),
                'url_suffix': '/docs/HTML/Using_the_application_cache',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(4) a'),
                'url_suffix': '/docs/DOM/Storage',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(5) a'),
                'url_suffix': '/docs/IndexedDB',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(2) ul li:nth-child(6) a'),
                'url_suffix': '/docs/Using_files_from_web_applications',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(1) a'),
                'url_suffix': '/docs/CSS',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(2) a'),
                'url_suffix': '/docs/CSS/Using_CSS_gradients',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(3) a'),
                'url_suffix': '/docs/CSS/Using_CSS_transforms',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(4) a'),
                'url_suffix': '/docs/CSS/Using_CSS_transitions',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(5) a'),
                'url_suffix': '/docs/CSS/Using_CSS_animations',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(3) ul li:nth-child(6) a'),
                'url_suffix': '/docs/CSS/Media_queries',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(1) a'),
                'url_suffix': '/docs/JavaScript',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(2) a'),
                'url_suffix': '/docs/AJAX',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(3) a'),
                'url_suffix': '/docs/HTML/Canvas',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(4) a'),
                'url_suffix': '/docs/Using_geolocation',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(5) a'),
                'url_suffix': '/docs/DragDrop/Drag_and_Drop',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-docs ul li:nth-child(4) ul li:nth-child(6) a'),
                'url_suffix': '/docs/DOM/Using_web_workers',
            }
        ]

        community_links_list = [
            {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(1) a'),
                'url_suffix': '/events',
            }, {
                'locator': (By.CSS_SELECTOR, '#nav-sub-community li:nth-child(2) a'),
                'url_suffix': '/promote',
            }
        ]

        def open_topics_menu(self):
            self.selenium.find_element(*self._topics_menu_locator).click()

        def open_docs_menu(self):
            self.selenium.find_element(*self._docs_menu_locator).click()

        def open_community_menu(self):
            self.selenium.find_element(*self._community_menu_locator).click()

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
        def wait_for_username_visible(self):
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self._username_locator).is_displayed())

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
                'url_suffix': '/privacy',
            }
        ]

        _logo_locator = (By.CSS_SELECTOR, '#legal > img')

        @property
        def is_logo_visible(self):
            return self.is_element_visible(self._logo_locator)
