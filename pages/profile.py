#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class ProfilePage(BasePage):

    _nickname_locator = (By.CLASS_NAME, 'nickname')
    _irc_locator = (By.CLASS_NAME, 'irc')
    _organization_locator = (By.CLASS_NAME, 'org')
    _title_locator = (By.CLASS_NAME, 'title')
    _photo_locator = (By.CLASS_NAME, 'photo')
    _website_locator = (By.CSS_SELECTOR, '.website > .url')
    _twitter_locator = (By.CSS_SELECTOR, '.twitter > .url')
    _github_locator = (By.CSS_SELECTOR, '.github > .url')
    _docs_userpage_locator = (By.CSS_SELECTOR, '.docs > .url')

    @property
    def is_nickname_visible(self):
        return self.is_element_visible(self._nickname_locator)

    @property
    def is_irc_visible(self):
        return self.is_element_visible(self._irc_locator)

    @property
    def is_organization_visible(self):
        return self.is_element_visible(self._organization_locator)

    @property
    def is_title_visible(self):
        return self.is_element_visible(self._title_locator)
