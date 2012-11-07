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
    _manage_api_keys_locator = (By.CSS_SELECTOR, '.edit > .button')
    _submit_demo_locator = (By.CSS_SELECTOR, 'p.none > a.button')
    
    def click_manage_api_keys(self):
        return self.selenium.find_element(*self._manage_api_keys_locator).click()

    class KeyPage(BasePage):
        _create_new_key_button = (By.CSS_SELECTOR, '.button.positive')
        _history_button = (By.CSS_SELECTOR, '.actions > .button.positive')
        _delete_history_button = (By.CSS_SELECTOR, '.actions > .button.negative')
        _delete_button = (By.CSS_SELECTOR, '.key > button')
        _description_textbox = (By.CSS_SELECTOR, 'textarea#id_description')
        _description_text = "Testing api key"
        _create_button = (By.CSS_SELECTOR, '.key > .button.positive')
        _cancel_button = (By.CLASS_NAME, '.button')
        _key_id_text = (By.CSS_SELECTOR, '.key > code')
        _secret_text = (By.CSS_SELECTOR, '.secret > code')
        _description = (By.CSS_SELECTOR, '.description > dd')
        _new_keys_url = "/keys/new"

        def go_to_page(self, subpage="/keys/"):
            self.selenium.get(self.base_url + subpage)

        def click_create_new_key(self):
            return self.selenium.find_element(*self._create_new_key_button).click()

        def click_history_button(self):
            return self.selenium.find_element(*self._history_button).click()

        def click_delete_history_button(self):
            return self.selenium.find_element(*self._delete_history_button).click()

        def enter_description_text(self):
            return self.selenium.find_element(*self._description_textbox).send_keys(self._description_text)

        def click_create_button(self):
            return self.selenium.find_element(*self._create_button).click()

        def click_cancel_button(self):
            return self.selenium.find_element(*self._cancel_button).click()
 
        @property
        def create_key(self):
            self.go_to_page()
            self.click_create_new_key()
            self.enter_description_text()
            self.click_create_button()
            return self.is_element_visible(self._key_id_text)
            

        @property
        def delete_latest_key(self):
            self.go_to_page()
            self.click_delete_history_button()
            self.selenium.find_element(*self._delete_button).click()
            return self.selenium.current_url

    @property
    def is_submit_demo_button_visible(self):
        return self.is_element_visible(self._submit_demo_locator)

    @property
    def is_manage_api_keys_visible(self):
        return self.is_element_visible(self._manage_api_keys_locator)

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
