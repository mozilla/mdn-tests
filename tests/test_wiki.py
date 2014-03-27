#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random
import string
import pytest

from unittestzero import Assert

from pages.wiki import WikiPage
from pages.wiki import EditPage


class TestWiki:

    @pytest.mark.nondestructive
    def test_view_wiki_page(self, mozwebqa):
        wiki_page = WikiPage(mozwebqa)
        wiki_page.go_to_desired_page()

        Assert.true(wiki_page.settings_menu_visible)
        Assert.true(wiki_page.document_title)
        Assert.true(wiki_page.tags_list_visible)
        Assert.true(wiki_page.contributors_list_visible)

    def test_add_wiki_page(self, mozwebqa):
        wiki_page = EditPage(mozwebqa)
        wiki_page.go_to_new_wiki_page()
        wiki_page.sign_in()

        input_text = 'automatic_test_by_Selenium_tests_%s' % random.choice(string.lowercase)

        # Slug is the same as the title
        wiki_page.set_input_text_for('article_title', input_text)
        wiki_page.set_input_text_for('comment_field', input_text)
        wiki_page.select_type_of_TOC('2')
        wiki_page.send_input_text_for_body(input_text)

        wiki_page.click_save_changes()

        Assert.equal(input_text, wiki_page.wiki_doc_title)
        Assert.equal(input_text, wiki_page.wiki_doc_content)
