#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from base import BasePage


class WikiPage(BasePage):

    _page_title = 'Array - JavaScript | MDN'

    _settings_menu_locator = (By.ID, 'settings-menu')
    _wiki_document_title_locator = (By.CSS_SELECTOR, '.document-head > h1')
    _tags_list_locator = (By.CSS_SELECTOR, 'div.tag-attach-list')
    _contributors_list_locator = (By.CSS_SELECTOR, 'div[class="contributor-sub"]')

    def go_to_desired_page(self):
        self.selenium.get(self.base_url + '/docs/Web/JavaScript/Reference/Global_Objects/Array')
        self.is_the_current_page

    @property
    def settings_menu_visible(self):
        return self.is_element_visible(self._settings_menu_locator)

    @property
    def document_title(self):
        return self.is_element_visible(self._wiki_document_title_locator)

    @property
    def tags_list_visible(self):
        return self.is_element_visible(self._tags_list_locator)

    @property
    def contributors_list_visible(self):
        return self.is_element_visible(self._contributors_list_locator)


class EditPage(BasePage):

    _page_title = 'Create a New Article | MDN'

    _article_title_locator = (By.ID, 'id_title')
    _type_of_toc_locator = (By.ID, 'id_toc_depth')
    _save_changes_button_locator = (By.ID, 'btn-save')
    _document_title_locator = (By.CSS_SELECTOR, '#wiki-document-head > h1')
    _comment_field_locator = (By.ID, 'id_comment')
    _tags_list_locator = (By.CSS_SELECTOR, '.tagit-new')
    _wiki_doc_content_locator = (By.CSS_SELECTOR, '#wikiArticle > p')

    def go_to_new_wiki_page(self):
        self.selenium.get(self.base_url + '/docs/new')

    def send_input_text_for_body(self, value):
        iframe = self.selenium.find_elements_by_tag_name('iframe')[0]
        self.selenium.switch_to_frame(iframe)
        input_field = self.selenium.find_element_by_xpath('/html/body/p')
        input_field.send_keys(value)
        self.selenium.switch_to_default_content()

    def set_input_text_for(self, for_field, value):
        input_field = self.selenium.find_element(*getattr(self, '_%s_locator' % for_field))
        input_field.clear()
        input_field.send_keys(value)

    def select_type_of_TOC(self, option_value):
        element = self.selenium.find_element(*self._type_of_toc_locator)
        select = Select(element)
        select.select_by_value(option_value)

    def click_save_changes(self):
        self.selenium.find_element(*self._save_changes_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s: s.find_element(*self._document_title_locator))

    @property
    def wiki_doc_title(self):
        return self.selenium.find_element(*self._document_title_locator).text

    @property
    def wiki_doc_content(self):
        return self.selenium.find_element(*self._wiki_doc_content_locator).text
