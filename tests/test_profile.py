#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestProfile:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_profile_page(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in()

        profile_page = home_page.header.click_profile_link()
        Assert.true(profile_page.is_nickname_visible)
        Assert.true(profile_page.is_irc_visible)
        Assert.true(profile_page.is_organization_visible)
        Assert.true(profile_page.is_title_visible)
