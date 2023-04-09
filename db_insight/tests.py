# User model
from django.contrib.auth.models import User

# Integration
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class UserTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        # cls.selenium.implicitly_wait(10)
        User.objects.create_user(username='testuser', password='12345')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/login/'))
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('12345')
        self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
