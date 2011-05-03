from selenium import selenium
import vars
from page import Page

page_load_timeout = vars.ConnectionParameters.page_load_timeout


class DemoPage(Page):

    _header_image_locator = 'css=#logo > a img'
    _login_locator = 'css=#utility > p.user-state > a:nth-child(1)'
    _signup_locator = 'css=#utility >p.user-state > a:nth-child(2)'
    _featured_demos_header_locator = 'css=#featured-demos>header > h2'
    _search_mdn_locator = "css=#q"
    _search_locator = 'css=input#search-demos'
    _search_heading_locator = "css=.page-title"
    _most_viewed_locator = 'css=#gallery-sort >.sort > li:nth-child(1) > a'
    _most_liked_locator = 'css=#gallery-sort >.sort > li:nth-child(2) > a'
    _most_recent_locator = 'css=#gallery-sort >.sort > li:nth-child(3) >a'
    _submit__demo_locator = 'css=#page-head.landing > p .aide demo-submit'
    _feedback_locator = "css=#footbar > div.wrap> p >a"
    _footer_image_locator = 'css=#legal > img'
    _footer_copyright_text_locator = 'css=#legal > p#copyright'
    _footer_license_locator = 'css=#legal > p >a:nth-child(1)'
    _footer_about_locator = 'css=#legal >p > a:nth-child(2)'
    _footer_privacy_policy_locator = 'css=#legal > p > a:nth-child(3)'
    _footer_language_locator = 'css=select#language'
    _footer_login_locator = 'css=#site-info >.wrap >.user-state>a:nth-child(1)'
    _footer_signup_locator ='css=#site-info > .wrap > .user-state>a:nth-child(2)'
    _technology_locator ="css=.cols-2 > li > a"

    def __init__(self,selenium):
        self.selenium = selenium
   
    @property
    def get_technology(self):
        technology_text =[]
        technology_visible =[]
        count = self.selenium.get_css_count(self._technology_locator)
        for i in range(1,count):
            locator = "css=.cols-2>li:nth-child(%d)>a" % i
            technology_text.append(self.selenium.get_text(locator))
            technology_visible.append(self.selenium.is_visible(locator))
        return dict(zip(technology_text, technology_visible))
    

    @property
    def go_to_page(self):
        self.selenium.open('demos/')
        self.selenium.window_maximize()
        print self.selenium.get_location()
        #self.selenium.wait_for_page_to_load(page_load_timeout)

    @property
    def get_header_image(self):
        return self.is_element_present(self._header_image_locator)

    @property
    def get_login_link(self):
        return self.is_element_present(self._login_locator)

    @property
    def get_signup_link(self):
        return self.is_element_present(self._signup_locator)

    @property
    def get_search_mdn(self):
        return self.is_element_present(self._search_mdn_locator)

    @property
    def get_featured_demos_header(self):
        return self.is_element_present(self._featured_demos_header_locator)

    @property
    def search(self):
        return self.is_element_present(self._search_locator)

    @property
    def search_heading(self):
        return is_element_present(self._search_heading_locator)


    @property
    def perform_search(self,locator,term):
        self.selenium.type(locator, term + "\15")
        return self.search_heading

    @property
    def most_viewed(self):
        return self.is_element_present(self._most_viewed_locator)

    @property
    def most_liked(self):
        return self.is_element_present(self._most_liked_locator)

    @property
    def most_recent(self):
        return self.is_element_present(self._most_recent_locator)

    @property
    def submit_demo(self):
        return self.is_element_present(_submit_demo_locator)

    @property
    def feedback(self):
        return self.is_element_present(self._feedback_locator)

    @property
    def footer_image(self):
        return self.is_element_present(self._footer_image_locator)

    @property
    def footer_copyright_text(self):
        return self.is_element_present(self._footer_copyright_text_locator)

    @property
    def footer_license(self):
        return self.is_element_present(self._footer_license_locator)

    @property
    def footer_about(self):
        return self.is_element_present(self._footer_about_locator)

    @property
    def footer_privacy_policy(self):
        return self.is_element_present(self._footer_privacy_policy_locator)

    @property
    def footer_language(self):
        return self.is_element_present(self._footer_language_locator)

    @property
    def footer_login(self):
        return self.is_element_present(self._footer_login_locator)

    @property
    def footer_signup(self):
        return self.is_element_present(self._footer_signup_locator) 