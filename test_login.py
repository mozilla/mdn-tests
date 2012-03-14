#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from pages.desktop.demo import ProfilePage
import pytest

xfail = pytest.mark.xfail


class TestLogin:

    @xfail(reason="We don't have BrowserID on stage yet")
    @pytest.mark.nondestructive
    def test_login(self, mozwebqa):
        profile_page = ProfilePage(mozwebqa)
        profile_page.go_to_profile_page()
        profile_page.log_user_in()
        profile_page.is_nickname_visible
        profile_page.is_irc_link_visible
        profile_page.is_company_link_visible
        profile_page.is_title_link_visible
