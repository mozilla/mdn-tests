from selenium import selenium
from page import Page

class DemoPage(Page):
    _count = 1
    _topics_link_locator = "css=.toggle"
    _docs_link_locator = "css=.docs"
    _demos_link_locator = "css=.demos"
    _learning_link_locator = "css=.learning"
    _forums_link_locator = "css=.community"
    _join_mdn_locator = "css=.wrap>p:nth-child(1)>a"
    _login_locator = "css=.wrap>p:nth-child(2)>a"
    _search_mdn_locator ="css=#q"
    _demo_studio_locator = "css=#demos-head>h1"
    _learn_more_locator  = "css=.learnmore>a"
    _submit_demo_locator = "css=.demo-buttons>li.submit"
    _join_derby_button_locator = "css=#derby-cta>a"
    _featured_demo_header = "css=#featured-demos>header>h2"
    _browse_by_technology = "css=#div#demo-tags>a"
    _tag_count = "css=#tags-list>li"
    _total_demo_count = "css=.count"
    _up_and_coming_sort = "css=.sort>li:nth-child(1)>a"
    _most_viewed_sort = "css=.sort>li:nth-child(2)>a"
    _most_liked_sort = "css=.sort>li:nth-child(3)>a"
    _most_recent_sort = "css=.sort>li:nth-child(1)>a"
    _demo_image_count = "css=.demo>.demo-title>a>img"
    _demo_title_count ="css=.demo>.demo-title>a"
    _footer_img = "css=#legal>img"
    _footer_rss_link = "css=.feed>a"
    _footer_bar_feedback_link = "css=#footbar>div.wrap>p>a"
    _footer_licenses_link = "css=#legal>p>a:nth-child(1)"
    _footer_about_link = "css=#legal>p>a:nth-child(2)"
    _footer_privacy_link = "css=#legal>p>a:nth-child(3)"
    _footer_help_link = "css=#legal>p>a:nth-child(4)"
    
    @property 
    def topics_link(self):
        return self.is_element_present( self._topics_link_locator)
        
    @property
    def docs_link(self):
        return self.is_element_present( self._docs_link_locator)
        
    @property
    def demos_link(self):
        return self.is_element_present( self._demos_link_locator)
        
    @property
    def learning_link(self):
        return self.is_element_present( self._learning_link_locator)
        
    @property
    def forums_link(self):
        return self.is_element_present( self._forums_link_locator)
        
    @property
    def join_mdn(self):
        return self.is_element_present( self._join_mdn_locator)
        
    @property
    def login_locator(self):
        return self.is_element_present( self._login_locator)
        
    @property
    def search_mdn_locator(self):
        return self.is_element_present( self._search_mdn_locator)
        
    @property
    def demo_studio_locator(self):
        return self.is_element_present( self._demo_studio_locator)
        
    @property
    def learn_more_locator(self):
        return self.is_element_present( self._learn_more_locator)
        
    @property
    def submit_demo_locator(self):
        return self.is_element_present( self._submit_demo_locator)
        
    @property
    def join_derby_locator(self):
        return self.is_element_present( self._jon_derby_locator)
        
    @property
    def featured_demo_locator(self):
        return self.is_element_present( self._featured_demo_locator)
        
    @property
    def browse_by_technology(self):
        return self.is_element_present( self._browse_by_technology)
        
    def get_tag_count(self):
        return self.get_css_count(self._tag_count)
        
    def get_tag(self,count):
        _tag = "css=#tags-list>li:nth-child(%d)" % count
        return self.is_element_present(_tag)
        
    def visit_tag_url(self,count):
        _tag = "css=#tags-list>li:nth-child(%d)" % count
        self.click(_tag,True)
        return self.get_url_current_page()
        
            
    @property
    def total_demo_count(self):
        return self.is_element_present( self._total_demo_count)
        
    @property
    def up_and_coming_sort(self):
        return self.is_element_present( self._up_and_coming_sort)
        
    @property
    def most_viewed_sort(self):
        return self.is_element_present( self._most_viewed_sort)
        
    property
    def most_liked_sort(self):
        return self.is_element_present( self._most_liked_sort)
        
    @property
    def most_recent_sort(self):
        return self.is_element_present( self._most_recent_sort)
        
    
    def get_demo_image_count(self):
        return self.get_css_count(self._demo_image_count)
        
        
    def demo_image_locator(self,count):
        _demo_image_locator = \
        "css=.demo:nth-child(%d)>.demo-title>a>img" % count
        return self.is_element_present( _demo_image_locator)
        
    
    def get_demo_title_count(self):
       return self.get_css_count(self._demo_title_count)
        
    def demo_title_locator(self,count):
        _demo_title_locator = \
        "css=.demo:nth-child(%d)>.demo-title>a" % count
        return self.is_element_present(_demo_title_locator)
        
    @property
    def footer_img(self):
        return self.is_element_present( self._footer_img)
        
    @property
    def footer_rss_link(self):
        return self.is_element_present( self._footer_rss_link)
        
    @property
    def footer_bar_feedback_link(self):
        return self.is_element_present( self._footer_bar_feedback_link)
        
    @property
    def footer_licenses_link(self):
        return self.is_element_present( self._footer_licenses_link)
        
    @property
    def footer_about_link(self):
        return self.is_element_present( self._footer_about_link)
        
    @property
    def footer_privacy_link(self):
        return self.is_element_present( self._footer_privacy_link)
        
    @property
    def footer_help_link(self):
        return self.is_element_present( self._footer_help_link)   
  
  