from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from base import BasePage
from mocks.mock_user import MockUser
from unittestzero import Assert

class DjangoAdmin(BasePage):
    _django_user_locator = (By.CSS_SELECTOR, '#id_username')
    _django_password_locator = (By.CSS_SELECTOR, '#id_password')
    _django_login_button_locator = (By.CSS_SELECTOR, 'input.grp-button.grp-default')
    _django_signed_in_locator = (By.CSS_SELECTOR, '#grp-admin-title')
    _django_logged_out_locator  = (By.CSS_SELECTOR, '.grp-current-page')
    _django_save_button_locator = (By.CSS_SELECTOR, 'input[value="Save"]')
    _waffle_module_locator = (By.CSS_SELECTOR, '#module-waffle')
    _change_waffle_flag_locator = (By.CSS_SELECTOR, '#module-waffle .grp-change-link a[href*="flag"]')
    _waffle_flags_locator = (By.CSS_SELECTOR, '#result_list tbody tr th a')
    _waffle_everyone_locator = (By.CSS_SELECTOR, '#id_everyone')
    _waffle_notification_locator = (By.CSS_SELECTOR, '#grp-container .grp-messagelist .grp-info:nth-of-type(1)')

    def go_to_page(self):
        self.selenium.get(self.base_url+'/admin/')

    def django_admin_sign_in(self, user=None):
        self.go_to_page()
        credentials = isinstance(user, MockUser) and \
        user or self.testsetup.credentials.get(user)
        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._django_user_locator))
        self.selenium.find_element(*self._django_user_locator).send_keys(credentials['name'])
        self.selenium.find_element(*self._django_password_locator).send_keys(credentials['password'])
        self.selenium.find_element(*self._django_login_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._django_signed_in_locator),
                                                         'Not Signed in.')       

    def django_admin_log_out(self):
        self.selenium.get(self.base_url+'/admin/logout/')
        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._django_logged_out_locator),
                                                         'Not Logged out.')       

    def toggle_waffle_everyone_flag(self, waffle_flag, setting='Unknown'):
        self.django_admin_sign_in('default')
        self.selenium.maximize_window()
        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._waffle_module_locator),
                                                         'Unable to locate Waffle module.')
        self.selenium.find_element(*self._change_waffle_flag_locator).click()

        for flag in self.selenium.find_elements(*self._waffle_flags_locator):
            if flag.text == waffle_flag:
                flag.click()
                break

        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._waffle_everyone_locator),
                                                         'Unable to locate Everyone dropdown.')
        select = Select(self.selenium.find_element(*self._waffle_everyone_locator))
        select.select_by_visible_text(setting)
        self.selenium.find_element(*self._django_save_button_locator).click()
        WebDriverWait(self.selenium, self.timeout).until(lambda s:
                                                         self.is_element_visible(self._waffle_notification_locator),
                                                         'Notification of flag change not found.')   
        Assert.true('changed successfully' in self.selenium.find_element(*self._waffle_notification_locator).text,
                    'Waffle flag %s not changed successfully.' % waffle_flag)

        self.django_admin_log_out()
