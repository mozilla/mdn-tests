#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page
from base import BasePage


class DerbyPage(BasePage):

    _page_title = 'Dev Derby | MDN'

    _home_link_locator = (By.CSS_SELECTOR, '#nav-derby > ul > li > em')  # strictly this isn't a link
    _challenges_link_locator = (By.CSS_SELECTOR, '#nav-derby li:nth-child(2) a')
    _rules_link_locator = (By.CSS_SELECTOR, '#nav-derby li:nth-child(3) a')
    _judging_link_locator = (By.CSS_SELECTOR, '#nav-derby li:nth-child(4) a')
    _prizes_link_locator = (By.CSS_SELECTOR, '#nav-derby li:nth-child(5) a')
    _resources_link_locator = (By.CSS_SELECTOR, '#nav-derby li:nth-child(6) a')
    _submit_demo_link_locator = (By.CSS_SELECTOR, '#derby-head .submit a')
    _demo_studio_link_locator = (By.CSS_SELECTOR, '#derby-head .presents a')
    _previous_winner_banner_locator = (By.CSS_SELECTOR, '#prev-winner > h1')
    _previous_winner_demo_title_locator = (By.CSS_SELECTOR, '#prev-winner .title a')
    _previous_winner_name_locator = (By.CSS_SELECTOR, '#prev-winner .author')
    _previous_winner_demo_button_locator = (By.CSS_SELECTOR, '#prev-winner .launch a')
    _docs_link_locator = (By.CSS_SELECTOR, '#resources .res-docs a')
    _demos_link_locator = (By.CSS_SELECTOR, '#resources .res-demos a')
    _articles_link_locator = (By.CSS_SELECTOR, '#resources .res-articles a')
    _prizes_heading_locator = (By.CSS_SELECTOR, '#challenge-prizes > h1')
    _prizes_image_locator = (By.CSS_SELECTOR, '#challenge-prizes img.prize')
    _current_judges_locator = (By.XPATH, "id('tab-judging')/ul[contains(@class, 'judges')][1]/li")
    _past_judges_locator = (By.XPATH, "id('tab-judging')/ul[contains(@class, 'judges')][2]/li")
    _previous_challenges_link_locator = (By.CSS_SELECTOR, '#current-challenge li:nth-child(5) a')
    _previous_challenges_locator = (By.CSS_SELECTOR, '#tab-previous .previous li')

    def go_to_derby_page(self):
        self.selenium.get(self.base_url + '/demos/devderby')
        self.is_the_current_page

    @property
    def is_prizes_image_visible(self):
        return self.is_element_visible(self._prizes_image_locator)

    @property
    def prizes_heading(self):
        return self.selenium.find_element(*self._prizes_heading_locator).text

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
    def is_demos_link_visible(self):
        return self.is_element_visible(self._demos_link_locator)

    @property
    def is_articles_link_visible(self):
        return self.is_element_visible(self._articles_link_locator)

    def click_judging_link(self):
        self.selenium.find_element(*self._judging_link_locator).click()

    @property
    def current_judges(self):
        return [self.Judge(self.testsetup, element) for element in self.selenium.find_elements(*self._current_judges_locator)]

    @property
    def past_judges(self):
        return [self.Judge(self.testsetup, element) for element in self.selenium.find_elements(*self._past_judges_locator)]

    def click_previous_challenges_link(self):
        self.selenium.find_element(*self._previous_challenges_link_locator).click()

    @property
    def previous_challenges(self):
        return [self.PreviousChallenge(self.testsetup, element) for element in self.selenium.find_elements(*self._previous_challenges_locator)]

    class Judge(Page):

        _name_locator = (By.CSS_SELECTOR, 'h3 a')
        _photo_locator = (By.CLASS_NAME, 'photo')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            return self._root_element.find_element(*self._name_locator).text

        @property
        def is_photo_visible(self):
            return self._root_element.find_element(*self._photo_locator).is_displayed()

    class PreviousChallenge(Page):

        _name_locator = (By.CSS_SELECTOR, 'h3 a')

        def __init__(self, testsetup, element):
            Page.__init__(self, testsetup)
            self._root_element = element

        @property
        def name(self):
            return self._root_element.find_element(*self._name_locator).text

        @property
        def is_name_visible(self):
            return self._root_element.find_element(*self._name_locator).is_displayed()
