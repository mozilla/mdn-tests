#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage

from unittestzero import Assert
import pytest


@pytest.mark.skipif("config.getvalue('base_url').endswith('allizom.org')")
class TestHome:

    @pytest.mark.nondestructive
    def test_main_nav_links_are_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.header.main_nav_links_list:
            if not home_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(home_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_main_nav_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.header.main_nav_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_main_nav_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in home_page.header.main_nav_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not home_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_zones_links_are_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_zones_menu()
        bad_links = []
        for link in home_page.header.zones_links_list:
            if not home_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(home_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_zones_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_zones_menu()
        bad_links = []
        for link in home_page.header.zones_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_zones_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_zones_menu()
        bad_urls = []
        for link in home_page.header.zones_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not home_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.native
    @pytest.mark.nondestructive
    def test_web_platform_menu_links_are_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_web_platform_menu()
        bad_links = []
        for link in home_page.header.web_platform_links_list:
            if not home_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(home_page.header.is_search_present)

    @pytest.mark.nondestructive
    def test_web_platform_menu_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_web_platform_menu()
        bad_links = []
        for link in home_page.header.web_platform_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    @pytest.mark.xfail("config.getvalue('base_url').endswith('allizom.org')",
                       reason="BUG 802196: Broken links on staging")
    def test_web_platform_menu_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        home_page.header.open_web_platform_menu()
        bad_urls = []
        for link in home_page.header.web_platform_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not home_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))

    @pytest.mark.nondestructive
    def test_footer_links_are_visible(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.footer.footer_links_list:
            if not home_page.is_element_visible(link.get('locator')):
                bad_links.append('The link at %s is not visible' % link.get('locator')[1:])
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))
        Assert.true(home_page.header.is_search_present)
        Assert.true(home_page.footer.is_logo_visible)

    @pytest.mark.nondestructive
    def test_footer_link_destinations_are_correct(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_links = []
        for link in home_page.footer.footer_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        Assert.equal(0, len(bad_links), '%s bad links found: ' % len(bad_links) + ', '.join(bad_links))

    @pytest.mark.nondestructive
    def test_footer_link_urls_are_valid(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        bad_urls = []
        for link in home_page.footer.footer_links_list:
            url = home_page.link_destination(link.get('locator'))
            if not home_page.is_valid_link(url):
                bad_urls.append('%s is not a valid url' % url)
        Assert.equal(0, len(bad_urls), '%s bad urls found: ' % len(bad_urls) + ', '.join(bad_urls))
