#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page
from base import BasePage


class DemoPage(BasePage):

    _page_title = 'Demo Studio | MDN'

    _demo_studio_locator = (By.CSS_SELECTOR, '#demos-head > h1')
    _learn_more_locator = (By.CSS_SELECTOR, '.learnmore > a')
    _demos_locator = (By.CSS_SELECTOR, '.gallery .demo')
    _rss_link_locator = (By.CSS_SELECTOR, '.feed > a')

    def go_to_demo_page(self):
        self.selenium.get(self.base_url + '/demos')
        self.is_the_current_page

    @property
    def is_demo_studio_link_visible(self):
        return self.is_element_visible(self._demo_studio_locator)

    @property
    def is_learn_more_link_visible(self):
        return self.is_element_visible(self._learn_more_locator)

    @property
    def demos(self):
        return [self.Demo(self.testsetup, element) for element in self.selenium.find_elements(*self._demos_locator)]

    @property
    def is_rss_link_visible(self):
        return self.is_element_visible(self._rss_link_locator)

    class Demo(Page):

        _title_locator = (By.CSS_SELECTOR, 'h2 > a')
        _thumbnail_locator = (By.TAG_NAME, 'img')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def is_title_visible(self):
            return self._root_element.find_element(*self._title_locator).is_displayed()

        @property
        def is_thumbnail_visible(self):
            return self._root_element.find_element(*self._thumbnail_locator).is_displayed()
