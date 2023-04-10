# User model
from django.contrib.auth.models import User

# Unit
from django.test import TestCase
from .models import Company

# Integration
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

import pdb


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(
            name="Apple",
            domain="apple.com",
            industry="Technology")

    def test_company_attributes(self):
        apple = Company.objects.get(name="Apple")
        self.assertEqual(apple.name, 'Apple')
        self.assertEqual(apple.domain, 'apple.com')
        self.assertTrue(apple.created_at)
        self.assertTrue(apple.updated_at)


class CreateCompanyTestCase(StaticLiveServerTestCase):
    fixtures = ['company/fixtures/companies.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        User.objects.create_user(username='testuser', password='12345')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_create(self):
        self.selenium.get('%s%s' % (self.live_server_url, "/accounts/login/"))
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("testuser")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("12345")
        self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click()

        self.selenium.get('%s%s' % (self.live_server_url, "/company"))
        self.selenium.find_element(By.ID, "createCompany").click()

        company_input = self.selenium.find_element(By.NAME, "name")
        company_input.send_keys("Test")
        domain_input = self.selenium.find_element(By.NAME, "domain")
        domain_input.send_keys("test.com")
        industry_input = self.selenium.find_element(By.NAME, "industry")
        industry_input.send_keys("Test Industry")

        self.selenium.find_element(By.ID, "saveCompany").click()

        test_company = Company.objects.last()
        self.assertEqual(test_company.name, 'Test')
        self.assertEqual(test_company.domain, 'test.com')
        self.assertTrue(test_company.created_at)
        self.assertTrue(test_company.updated_at)
