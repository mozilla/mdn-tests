#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page
from base import BasePage

class WikiPage(BasePage):


    def go_to_page(self, url=None, title=None):
        self._page_title = title
        self.selenium.get(url)
        self.is_the_current_page

