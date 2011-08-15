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
    _articles_link_locaator = "css=.res-articles>a"
    _prizes_locator = "css=.challenge-prizes>h1"
    
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
        return self.is_element_visible(self._demo_studio_locator)
        
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
    def  is_articles_link(self):
        return self.is_element_visible(self._articles_link_locator)
