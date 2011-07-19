from selenium import selenium
from page import Page

class DerbyPage(Page):
    _home_locator = "css=#nav-derby>ul>li>em"
    _challenges_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(2)>a"
    _rules_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(3)>a"
    _judging_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(4)>a"
    _prizes_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(5)>a"
    _resources_locator = "css=#nav-derby>ul:nth-child(1)>li:nth-child(6)>a"
    _submit_demo_locator = "css=.submit>a"
    _demo_studio_locator = "css=.presents>a"
    _previous_winner_banner = "css=#prev-winner>h1"
    _previous_winner_demo_title = "css=.title>a"
    _previous_winner_name = "css=#prev-winner>h3>a"
    _previous_winner_demo_button = "css=#prev-winner>p.launch>a"
    _docs_link = "css=.res-docs>a"
    _demos_link = "css=.res-demos>a"
    _articles_link = "css=.res-articles>a"
    
    @property
    def home_locator(self):
        return self.is_element_present(self._home_locator)
    
    @property
    def challenges_locator(self):
        return self.is_element_present(self._challenges_locator)
        
    @property
    def rules_locator(self):
        return self.is_element_present(self._rules_locator)
        
    @property
    def judging_locator(self):
        return self.is_element_present(self._judging_locator)
        
        
    @property
    def prizes_locator(self):
        return self.is_element_present(self._prizes_locator)
        
    @property
    def resources_locator(self):
        return self.is_element_present(self._resources_locator)
        
    @property
    def submit_demo_locator(self):
        return self.is_element_present(self._submit_demo_locator)
        
    @property
    def demo_studio_locator(self):
        return self.is_element_present(self._demo_studio_locator)
        
    @property
    def previous_winner_banner(self):
        return self.is_element_present(self._previous_winner_banner)
        
    @property
    def previous_winner_demo_title(self):
        return self.is_element_present(self._previous_winner_demo_title)
        
    @property
    def previous_winner_name(self):
        return self.is_element_present(self._previous_winner_name)
        
    @property
    def previous_winner_demo_button(self):
        return self.is_element_present(self._previous_winner_demo_button)
        
    @property
    def docs_link(self):
        return self.is_element_present(self._docs_link)
        
    @property
    def  articles_link(self):
        return self.is_element_present(self._articles_link)
