#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest
from persona_test_user import PersonaTestUser


class TestSignIn:

    @pytest.mark.nondestructive
    def test_sign_in(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in(user="default")
        home_page.header.wait_for_username_visible
        Assert.true(home_page.is_signed_in)

    @pytest.mark.nondestructive
    def test_sign_out(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in(user="default")
        home_page.header.wait_for_username_visible
        home_page.header.click_sign_out()
        Assert.false(home_page.is_signed_in)

    def test_create_new_account(self, mozwebqa):
        user = PersonaTestUser().create_user()
        _username = user['email'].split('@')[0]

        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.sign_in(user)
        Assert.true(home_page.is_the_current_page)

        home_page.enter_new_user_profile(_username)
        Assert.equal(home_page.display_name, _username)
