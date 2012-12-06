#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class LearningPage(BasePage):

    _page_title = 'Learn How to Make Websites | MDN'

    _page_title_locator = (By.CSS_SELECTOR, '#page-head .page-title')
    _html_locator = (By.CSS_SELECTOR, '#sub-html h2')
    _css_locator = (By.CSS_SELECTOR, '#sub-css h2')
    _javascript_locator = (By.CSS_SELECTOR, '#sub-js h2')
    _blackboard_locator = (By.ID, 'blackboard')
    _p2p_image_locator = (By.CSS_SELECTOR, '#learn-p2pu > p > span')

    def go_to_page(self):
        self.selenium.get(self.base_url + '/learn')
        self.is_the_current_page

    @property
    def is_page_title_visible(self):
        return self.is_element_visible(self._page_title_locator)

    @property
    def is_html_locator_visible(self):
        return self.is_element_visible(self._html_locator)

    @property
    def is_css_locator_visible(self):
        return self.is_element_visible(self._css_locator)

    @property
    def is_javascript_link_visible(self):
        return self.is_element_visible(self._javascript_locator)

    @property
    def is_blackboard_visible(self):
        return self.is_element_visible(self._blackboard_locator)

    @property
    def is_p2p_image_visible(self):
        return self.is_element_visible(self._p2p_image_locator)
