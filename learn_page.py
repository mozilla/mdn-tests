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
