#!usr/bin/env python
# -*- coding: utf-8 -*-

'''
A Python/Selenium automated crawler to collect PDFs of handwritten
campaign-finance records from the interface provided by
Allegheny County, Pennsylvania, which doesn't particularly want
to be scraped.
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time
import os
from collections import Counter
import itertools
import subprocess

# we're going to need this more than once
dl_path = '/Volumes/AJsdrive/by_year'


class DocGetter():

    @staticmethod
    def open_browser():
        '''
        new Chrome instance with special options
        to make grabbing the PDF easier by avoiding
        the rendering extension and download dialogs
        '''
        # changes Chrome's default behavior to autodownload our files
        chrome_profile = webdriver.ChromeOptions()
        profile = {
            'profile.default_content_settings.multiple-automatic-downloads': 1,
            'download.default_directory': dl_path,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'plugins.plugins_list': [{
                'enabled': False, 'name': 'Chrome PDF Viewer'
            }]}
        chrome_profile.add_experimental_option('prefs', profile)
        return webdriver.Chrome(
            chrome_options=chrome_profile)

    @staticmethod
    def navigate(driver):
        '''
        takes us to the right page to begin
        '''
        driver.get('http://documents.alleghenycounty.us/publicaccess/DatasourceTemplate.aspx')

    @staticmethod
    def begin_search(driver):
        '''
        performs the text-box search for all campaign-finance records;
        tries for the broadest search the page supports at the time
        '''
        # makes sure we're searching campaign-finance records
        driver.find_element_by_css_selector('#CustomQueryDisplay > option[value="136"]').click()

        # main search box, only useful when can query everything --
        # which is intermittent at best.
        # when this works, best way to search, so worth a shot
        search_box = driver.find_element_by_id('KeywordDisplay_ctl01_textInput')
        search_action = search_box.send_keys('*\n')

        print 'making the list of doc_elems ....\n'
        doc_result = driver.find_element_by_css_selector('#DocumentResults tbody')
        # returns a list
        return doc_result.find_elements_by_tag_name('tr')

    @staticmethod
    def set_type_of_search(driver, doc_elems):
        '''
        if we can search everything at once, great. but often we can't.
        it doesn't matter for ultimate document collection whether
        we search by year, so this method decides for us how to proceed.
        '''
        if len(doc_elems) > 1:
            print 'Everything was in one place today. Here we go.\n'
            library = DocGetter.find_pdfs(driver, doc_elems)
            DocGetter.collect_pdfs(driver, library)

        else:
            print 'Can\'t search everything in one place today. Sad face. Searching by year instead.\n'
            DocGetter.search_by_year(driver, doc_elems)

    @staticmethod
    def search_by_year(driver, doc_elems):
        '''
        seach goes back to 2007, so we do, too.
        '''
        years = [
            '2007',
            '2008',
            '2009',
            '2010',
            '2011',
            '2012',
            '2013',
            '2014',
            '2015']

        for year in years:
            search_box = driver.find_element_by_id('KeywordDisplay_ctl02_textInput')
            search_box.clear()
            search_action = search_box.send_keys(year + '\n')

            library = DocGetter.find_pdfs(driver)
            DocGetter.collect_pdfs(driver, library)

        subprocess.Popen(['say', 'Holy shit. Are we done?'])

    @staticmethod
    def find_pdfs(driver, doc_elems):
        '''
        creates list of all our link elements and the
        (cleaned) document title text
        '''

        # first one is empty;
        # for some reason, Selenium will transform type(doc_elems)
        # from <list> to <webdriver> after calling python builtin functions
        # such as doc_elems.pop(0)
        del doc_elems[0]

        print 'doc_elems has', len(doc_elems), 'things in it.\n'

        # I'd love to use a generator for this so the whole thing
        # doesn't have to live in memory, but we'll need to use it
        # more than once.
        # also: chaining .replace() is ugly, but still faster than regex;
        # if anyone cares, could do something like (?=[A-Z0-9]+\b)(\w+\b)
        print 'cleaning future filenames ....\n'
        doc_names = [elem.get_attribute('innerHTML').strip().replace('"', '').replace('Campaign Finance Statement - ', '').replace('/', '').replace('<td>', '') for elem in doc_elems]

        print 'deduping ....\n'
        DocGetter.create_unique_titles(doc_names)

        print 'building tuples ....\n'
        return itertools.izip(doc_names, doc_elems)

    @staticmethod
    def create_unique_titles(doc_names):
        '''
        our list contains duplicate titles for unique documents;
        we want each to have a unique file name
        '''
        # creates a dictionary of our document titles and number of occurrences
        dupes = Counter(doc_names)

        for i, count in dupes.items():
            # if it's already unique, skip it
            if count > 1:
                # add a numerical counter to the end of the document title
                for suffix in range(1, count + 1):
                    # preserves order of the original list
                    doc_names[doc_names.index(i)] = '{0}_{1}'.format(i, str(suffix))

    @staticmethod
    def rename_file(dl_path, title):
        '''
        we try this at a couple of points, so why repeat ourselves?
        '''
        os.rename(
                '{1}/PublicAccessProvider.pdf'.format(dl_path),
                '{0}/{1}.pdf'.format(dl_path, title))

    @staticmethod
    def collect_pdfs(driver, library):
        '''
        opens each record in a new tab, one at a time,
        so we don't crash the browser or the site and still
        get what we want.

        Args:
        library: list of tuples, each containing
        [0]cleaned doc names,
        [1]clickable page elements
        '''
        no_names = []

        # if it breaks, I want to know on which list item so I can
        # jump back into the at the right place with
        # itertools.islice(library, list_position, None)
        for i, (title, document) in enumerate(library):
            # having made filenames unique, making sure we're not
            # grabbing something we already have
            if not os.path.isfile('{0}/{1}.pdf'.format(dl_path, title)):
                driver.switch_to.window(driver.window_handles[0])
                try:
                    document.click()
                    time.sleep(1)

                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(15)

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    time.sleep(10)

                    try:
                        time.sleep(5)
                        DocGetter.rename_file(dl_path, title)
                        print title, i

                    except OSError:
                        # a minority of these are large files that might not
                        # be ready for a name because they needed more time
                        # to download; let's wait a bit and try again
                        try:
                            time.sleep(15)
                            DocGetter.rename_file(dl_path, title)
                            print title, i
                        # still might not work and we should know what failed
                        # and where we are in the loop
                        except OSError:
                            no_names.append((title, document))
                            print '\n {0} did not want to name itself. check item {1} of'.format(title, i), len(library) + '\n'

                # will hit this if click event fails
                except WebDriverException as wde:
                    print '{0} ::: {1} does not seem to be clickable. check item {2} of'.format(wde, title, i), len(library)

            else:
                continue

        print len(no_names)
        print no_names

    @staticmethod
    def follow_the_money():
        '''
        runs the initial methods whereby we slurp up
        and spit-polish the data thingies
        '''
        driver = DocGetter.open_browser()
        DocGetter.navigate(driver)
        doc_elems = DocGetter.begin_search(driver)
        DocGetter.set_type_of_search(doc_elems)
