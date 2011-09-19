#!/usr/bin/env python
#
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is MDN
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Raymond Etornam Agbeame
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL,and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from selenium import selenium
from page import Page


class DerbyPage(Page):
    _home_link_locator = "css=#nav-derby>ul>li>em"
    _challenges_link_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(2)>a"
    _rules_link_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(3)>a"
    _judging_link_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(4)>a"
    _prizes_link_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(5)>a"
    _resources_link_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(6)>a"
    _submit_demo_link_locator = "css=.submit>a"
    _demo_studio_link_locator = "css=.presents>a"
    _previous_winner_banner_locator = "css=#prev-winner>h1"
    _previous_winner_demo_title_locator = "css=.title>a"
    _previous_winner_name_locator = "css=#prev-winner>h3>a"
    _previous_winner_demo_button_locator = "css=#prev-winner>p.launch>a"
    _docs_link_locator = "css=.res-docs>a"
    _demos_link_locator = "css=.res-demos>a"
    _articles_link_locator = "css=.res-articles>a"
    _prizes_locator = "css=#challenge-prizes>h1"
    _prizes_image_locator = "css=.prize"
    _previous_link_locator = "css=.tabs>li>a#tab-previous"
    _judge_locator = "css=.judges>vcard>h3>a>img"
    _previous_challenges_locator = "css=.ul.previous>li>h3"

    @property
    def get_number_of_judges(self):
        return self.get_css_count(self._judge_locator)

    def go_to_derby_page(self):
        self.open("en-US/demos/devderby")

    def is_judge_photo_visible(self, count):
        self.click(self._judging_link_locator)
        judge_photo_locator = "css=.judges>.vcard:nth-child(%d)>h3>a>img" % count
        return self.is_element_visible(judge_photo_locator)

    def are_previous_challenges_visible(self, count):
        self.click(self._previous_link_locator)
        previous_challenge_locator = 'css=ul.previous>li:nth-child(%d)' % count
        return self.is_element_visible(previous_challenge_locator)

    @property
    def get_number_of_previous_challenges(self):
        return self.get_css_count(self._previous_challenges_locator)

    @property
    def is_prizes_image_visible(self):
        return self.is_element_visible(self._prizes_image_locator)

    @property
    def get_prizes_text(self):
        return self.get_text(self._prizes_locator)

    @property
    def is_home_link_visible(self):
        return self.is_element_visible(self._home_link_locator)

    @property
    def is_challenges_link_visible(self):
        return self.is_element_visible(self._challenges_link_locator)

    @property
    def is_rules_link_visible(self):
        return self.is_element_visible(self._rules_link_locator)

    @property
    def is_judging_link_visible(self):
        return self.is_element_visible(self._judging_link_locator)

    @property
    def is_prizes_link_visible(self):
        return self.is_element_visible(self._prizes_link_locator)

    @property
    def is_resources_link_visible(self):
        return self.is_element_visible(self._resources_link_locator)

    @property
    def is_submit_demo_link_visible(self):
        return self.is_element_visible(self._submit_demo_link_locator)

    @property
    def is_demo_studio_link_visible(self):
        return self.is_element_visible(self._demo_studio_link_locator)

    @property
    def is_previous_winner_banner_visible(self):
        return self.is_element_visible(self._previous_winner_banner_locator)

    @property
    def is_previous_winner_demo_title_visible(self):
        return self.is_element_visible(self._previous_winner_demo_title_locator)

    @property
    def is_previous_winner_name_visible(self):
        return self.is_element_visible(self._previous_winner_name_locator)

    @property
    def is_previous_winner_demo_button_visible(self):
        return self.is_element_visible(self._previous_winner_demo_button_locator)

    @property
    def is_docs_link_visible(self):
        return self.is_element_visible(self._docs_link_locator)

    @property
    def is_articles_link_visible(self):
        return self.is_element_visible(self._articles_link_locator)
