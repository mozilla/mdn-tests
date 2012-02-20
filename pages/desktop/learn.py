#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium import selenium
from page import Page


class LearnPage(Page):
    _make_web_better_locator = "css=.wrap>.page-title"
    _html_locator = "css=#sub-html>a>h2"
    _css_locator = "css=#sub-css>a>h2"
    _javascript_locator = "css=#sub-js>a>h2"
    _blackboard_image_locator = "css=#blackboard"
    _p2p_image_locator = "css=#learn-p2pu>p>a>span"

    def go_to_learn_page(self):
        self.open("/learn")

    @property
    def is_make_web_better_visible(self):
        return self.is_element_visible(self._make_web_better_locator)

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
    def is_blackboard_image_visible(self):
        return self.is_element_visible(self._blackboard_image_locator)

    @property
    def is_p2p_image_visible(self):
        return self.is_element_visible(self._p2p_image_locator)
