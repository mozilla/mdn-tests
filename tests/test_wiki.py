#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import re

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.wiki import WikiPage

from unittestzero import Assert
import pytest

class TestWiki:

    wiki_page_list = [
        {
            'url':      '/docs',
            'title':    'Web technology for developers | MDN'
        },
    ]

    wiki_page_css_selectors = ["#settings-menu", "#languages-menu", ".document-head",
                               ".tag-list", ".contributor-sub"]

    @pytest.mark.nondestructive
    def test_page_view(self, mozwebqa):

        for wiki in self.wiki_page_list:
            wiki_page = WikiPage(mozwebqa)
            wiki_page.go_to_page(wiki_page.base_url + wiki['url'], wiki['title'])
            for selector in self.wiki_page_css_selectors:
                Assert.not_none(wiki_page.selenium.find_element_by_css_selector(selector))