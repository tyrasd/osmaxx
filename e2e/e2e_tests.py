#!/usr/bin/env python3

import datetime
import os
import sys
from time import sleep
import unittest

import requests
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.zip_file_helpers import check_if_result_contains_data
from helpers import docker_compose

sys.path.append(os.path.join(__file__))

ADMIN_USER_FOR_TESTS = 'admin'
ADMIN_PASSWORD_FOR_TESTS = 'admin'


def _clean_start_containers():
    """
    first clean up, then check for newer images and then start the containers.
    Then wait 10 seconds to be certain the webapp is up and ready to receive.
    """
    docker_compose.clean()
    docker_compose.pull()
    docker_compose.start()
    docker_compose.create_superuser_for_test(username=ADMIN_USER_FOR_TESTS, password=ADMIN_PASSWORD_FOR_TESTS)
    sleep(10)


def _stop_and_remove_containers():
    """
    stop the containers and then cleanup
    """
    docker_compose.stop()
    docker_compose.clean()


class SeleniumTests(unittest.TestCase):
    wait_time_seconds = datetime.timedelta(minutes=5).total_seconds()
    excerpt_data = {
        'send_keys': {
            'new_excerpt_name': 'HSR',
            'new_excerpt_bounding_box_north': '47.22407852727801',
            'new_excerpt_bounding_box_west':  '8.815616369247437',
            'new_excerpt_bounding_box_east':  '8.819221258163452',
            'new_excerpt_bounding_box_south': '47.222388077452706',
        },
        'click': [
            'export_options.excerptconverter.gisexcerptconverter.gis_excerpt_converter.formats_0',
            'export_options.excerptconverter.gisexcerptconverter.gis_excerpt_converter.formats_1',
            'export_options.excerptconverter.gisexcerptconverter.gis_excerpt_converter.formats_2',
            'export_options.excerptconverter.gisexcerptconverter.gis_excerpt_converter.formats_3',
        ],
    }
    driver = webdriver.Firefox

    def setUp(self):
        self.browser = self.driver()

    def tearDown(self):
        self.browser.close()

    def test_login_logout(self):
        self._login()
        self._logout()

    def test_create_new_excerpt_succeeds(self):
        self._login()
        self._create_new_order()
        self._go_to_order()
        links = self._wait_for_order_to_complete_and_fetch_resulting_links()
        self.assertEqual(len(links), 8)
        download_links = self._get_download_links_from_links(links)
        for download_link in download_links:
            self._download_and_test_zip_contents(download_link)

    # Helper methods
    def _login(self):
        self.browser.get(self._make_link('/login/'))
        login_form = self.browser.find_element_by_id('osmaxx-login-form')
        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id("id_password")
        username.send_keys('admin')
        password.send_keys('admin')
        login_form.find_element_by_xpath("//input[@type='submit']").click()

    def _logout(self):
        self.browser.get(self._make_link('/logout/'))

    def _create_new_order(self):
        self.browser.get(self._make_link('/orders/new/#new-excerpt'))
        # wait for page to load
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located((By.ID, "new_excerpt_name"))
        )
        for html_id, send_value in self.excerpt_data['send_keys'].items():
            element = self.browser.find_element_by_id(html_id)
            element.clear()
            element.send_keys(send_value)
        for html_id in self.excerpt_data['click']:
            self.browser.find_element_by_id(html_id).click()
        self.browser.find_element_by_xpath("//input[@type='submit']").click()

    def _go_to_order(self):
        self.browser.get(self._make_link('/orders/'))
        xpath_link_to_order = '/html/body/div/div/div[2]/div/h3/a'
        WebDriverWait(self.browser, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath_link_to_order))
        )
        self.browser.find_element_by_xpath(xpath_link_to_order).click()

    def _wait_for_order_to_complete_and_fetch_resulting_links(self):
        poll_frequency_in_seconds = 10
        waited_time_in_seconds = 0
        while not self._download_finished():
            waited_time_in_seconds += poll_frequency_in_seconds
            if waited_time_in_seconds >= self.wait_time_seconds:
                raise selenium_exceptions.TimeoutException
            sleep(poll_frequency_in_seconds)
        links = self._get_download_a_tags()
        return links

    def _get_download_links_from_links(self, links):
        download_links_index_start = 0
        download_links_index_skip = 2
        number_of_downloads = 4
        return [links[i].get_attribute('href') for i in range(
            start=download_links_index_start,
            stop=number_of_downloads * download_links_index_skip - 1,
            step=download_links_index_skip,
        )]

    def _download_and_test_zip_contents(self, download_link):
        r = requests.get(download_link)
        check_if_result_contains_data(r.content, self.assertGreater)

    def _make_link(self, link):
        host = 'http://localhost:8000{}'
        return host.format(link)

    def _get_download_a_tags(self):
        return self.browser.find_element_by_class_name('download_files').find_elements_by_tag_name('a')

    def _get_status_element(self):
        return self.browser.find_element_by_xpath('/html/body/div/div/div[2]/table/tbody/tr[3]/td/span').text

    def _download_finished(self):
        self._reload_browser()
        status_element = self._get_status_element()
        self.assertFalse('∅' in status_element)
        return '✓' not in status_element

    def _reload_browser(self):
        self.browser.get(self.browser.current_url)

if __name__ == '__main__':
    _clean_start_containers()
    try:
        unittest.main()
    finally:
        _stop_and_remove_containers()
