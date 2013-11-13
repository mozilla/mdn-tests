#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


class TestSignIn:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_sign_in(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in()
        Assert.true(home_page.is_signed_in)

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    def test_sign_out(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in()
        home_page.header.click_sign_out()
        Assert.false(home_page.is_signed_in)
