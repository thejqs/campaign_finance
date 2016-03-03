# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from collections import namedtuple
# from collections import OrderedDict

# import urllib2
# import urllib

# Validator = namedtuple('Validator', ['doc_id', 'checksum', 'doc_name'])
# Validator = namedtuple('Validator', ['doc_title', 'doc_element'])

# user_agent = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
#     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
#     )

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = user_agent

# driver = webdriver.PhantomJS(desired_capabilities=dcap)

# driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any', '--web-security=false'])

# fp = webdriver.FirefoxProfile()

# fp.set_preference('browser.download.folderList',2)
# fp.set_preference('browser.download.manager.showWhenStarting',False)
# fp.set_preference('browser.download.dir', os.getcwd())
# fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
# driver = webdriver.Firefox(firefox_profile=fp)


# mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"

# f_profile = webdriver.FirefoxProfile()
# f_profile.set_preference("browser.download.folderList", 2)
# f_profile.set_preference("browser.download.manager.showWhenStarting", False)
# f_profile.set_preference("browser.download.dir", dl_path)
# f_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
# f_profile.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
# f_profile.set_preference("pdfjs.disabled", True)

# return webdriver.Firefox(firefox_profile=f_profile)

# changes Chrome's default behavior
# dc = DesiredCapabilities.CHROME
# dc['loggingPrefs'] = {'browser': 'ALL'}



# chromeop = webdriver.ChromeOptions()
# chromeop.add_extension('Awesome-Screenshot-App_v1.0.6.crx')
# driver = webdriver.Chrome(chrome_options=chromeop)



# dl_path = '/Users/jacobsanders/Development/projects_2016/campaign_finance/main/allegheny_county_images'

# need for PhantomJS:        
# driver.set_window_size(1024, 480)

# driver.save_screenshot('allegheny_county_images/main_page.png')

    # first one is empty, but doing doc_elems.pop(0) within Selenium
    # for some reason changes type(doc_elems) from list to
    # a WebDriver object. Selenium is weird.

    
            # driver.execute_script('window.open("");')
            # driver.get('http://documents.alleghenycounty.us/publicaccess/PublicAccessProvider.ashx?action=PDFStream&docID=%s&chksum=%s' % (doc_id, checksum))

    # search by year
    # years = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

    # for year in years:
        # search_box = driver.find_element_by_id('KeywordDisplay_ctl02_textInput')
        # search_box.clear()
        # search_action = search_box.send_keys(year + '\n')

    # print '<%s>' % doc_names[300].get_attribute('innerHTML')
    # doc_elems[3000].click()
    # print doc_elems


    # doc_elem.click()

    # time.sleep(2)

    # import ipdb; ipdb.set_trace()

    # assert len(driver.window_handles) == 2
    # print driver.window_handles

    # driver.switch_to.window(driver.window_handles[-1])
    # driver.set_window_size(1024,480)

    
            # doc_name = doc_elem.get_attribute('innerHTML')
            # DocGetter.rename_file(doc_name, title_counter)

            # doc_name = doc_name.strip().replace('"', '').replace('Campaign Finance Statement - ', '').replace('/', '').replace('<td>', '')




        # return (
        #     Validator(
        #         doc_id=doc_elem.get_attribute('docid'),
        #         checksum=doc_elem.get_attribute('chksum'),
        #         doc_name=doc_elem.get_attribute('innerHTML'))
        #     for doc_elem in doc_elems)

        # for validator in validators:
        #     doc_id = validator[0]
        #     checksum = validator[1]
        #     doc_name = validator[2]



            # import ipdb; ipdb.set_trace()
            # if os.path.isfile('{0}/{1}.pdf'.format(dl_path, doc_name)):
                # certainly not the most elegant way to do this.
                # ideally, the incrementing would only happen within that
                # group of identically named documents; for example:
                # Darlene Harris Duplicate, Darlene Harris Duplicate 2,
                # Darlene Harris Duplicate 3, Dan Gilman Duplicate,
                # Dan Gilman Duplicate 1, etc.
            #     try:
            #         title_counter += 1
            #         title_counter_string = str(title_counter)
            #         os.rename(
            #             '{0}/PublicAccessProvider.pdf'.format(dl_path),
            #             '{0}/{1}-{2}.pdf'.format(dl_path, doc_name, title_counter_string))
            #         os.wait()
            #     except OSError:
            #         print '{0}/{1}-{2}.pdf'.format(dl_path, doc_name, title_counter_string) + '\n'
            #         print 'I am a duplicate. Come have a look at {0} or {1} or {2} -- it might be a little weird.'.format(dl_path, doc_name, title_counter_string) + '\n'
            # else:
            #     try:
            #         os.rename(
            #             '{0}/PublicAccessProvider.pdf'.format(dl_path),
            #             '{0}/{1}.pdf'.format(dl_path, doc_name))
            #         os.wait()
            #     except OSError:
            #         print '{0}/{1}.pdf\n'.format(dl_path, doc_name)
            #         print "Come have a look at {0} or {1} -- it might be a little weird.".format(dl_path, doc_name) + '\n'

            # print doc_name

            # time.sleep(.5)

        # print title_counter

    # @staticmethod
    # def rename_file(doc_name, title_counter):
    #     '''
    #     renames the file from its generic filename at download
    #     to something a human will appreciate, also handling
    #     potential duplicates
    #     '''
        # funky looking, but faster than regex
        # if anyone cares, could do something like (?=[A-Z0-9]+\b)(\w+\b)
        # print doc_name.strip()
        # doc_name = doc_name.strip().replace('"', '').replace('Campaign Finance Statement - ', '').replace('/', '').replace('<td>', '')

        # # import ipdb; ipdb.set_trace()
        # if os.path.isfile('{0}/{1}.pdf'.format(dl_path, doc_name)):
        #     # certainly not the most elegant way to do this.
        #     # ideally, the incrementing would only happen within that
        #     # group of identically named documents; for example:
        #     # Darlene Harris Duplicate, Darlene Harris Duplicate 2,
        #     # Darlene Harris Duplicate 3, Dan Gilman Duplicate,
        #     # Dan Gilman Duplicate 1, etc.
        #     try:
        #         title_counter += 1
        #         title_counter_string = str(title_counter)
        #         os.rename(
        #             '{0}/PublicAccessProvider.pdf'.format(dl_path),
        #             '{0}/{1}-{2}.pdf'.format(dl_path, doc_name, title_counter_string))
        #         os.wait()
        #         yield title_counter += 1
        #     except OSError:
        #         print dl_path + '\n' + doc_name + '\n' + title_counter_string + '\n'
        #         print 'I am a duplicate. Come have a look at {0} or {1} or {2} -- it might be a little weird.'.format(dl_path, doc_name, title_counter_string) + '\n'
        # else:
        #     try:
        #         os.rename(
        #             '{0}/PublicAccessProvider.pdf'.format(dl_path),
        #             '{0}/{1}.pdf'.format(dl_path, doc_name))
        #     except OSError:
        #         print dl_path + '\n' + doc_name + '\n'
        #         print "Come have a look at {0} or {1} -- it might be a little weird.".format(dl_path, doc_name) + '\n'

        # # print doc_name

        # time.sleep(.5)



    
    # driver.switch_to.window(driver.window_handles[0])

    # doc_title = doc_names[int('%d' % current_record)].get_attribute('innerHTML')

    # doc_title = doc_title.replace('Campaign Finance Statement - ', '').replace('N/A -', '')

    # print '<%s>' % doc_names[300].get_attribute('innerHTML')
    # doc_elems[3000].click()
    # print doc_elems

    # driver.switch_to.window(driver.window_handles[-1])
    # print current_record
    # driver.save_screenshot('allegheny_county_images/%s.png' % current_record)

    # driver.close()

    # print driver.window_handles

    # driver.switch_to.window(driver.window_handles[0])

    # print current_record
    # print doc_title

    # current_record += 1

    # import ipdb; ipdb.set_trace()

    # driver.find_element_by_tag_name('body')

    # driver.save_screenshot(
    #     'allegheny_county_images/%s.png' % doc_title
    #     )

    # driver.switch_to.active_element()

    # do stuff
    # for cookie in driver.get_cookies():
    #     print cookie, '\n'

    # ActionChains and send_keys fire but don't work;
    # same for context_click
    # page = driver.find_element_by_tag_name('body')
    # page.send_keys(Keys.COMMAND + 's')

    # action = ActionChains(driver)
    # action.key_down(Keys.COMMAND)
    # action.send_keys('s')
    # action.key_up(Keys.COMMAND)
    # action.perform()

    # the response object from urllib2 doesn't include
    # the document image yet -- embed tag hasn't
    # provided it yet and actual page source is inaccessible,
    # which is mean and stupid
    # req = urllib2.Request('http://documents.alleghenycounty.us/publicaccess/PublicAccessProvider.ashx?action=PDFStream&docID=%s&chksum=%s' % (document_id, checksum))

    # pdf_response = urllib2.urlopen(req)
    # print pdf_response.info().items()
    # print pdf_response.read()

    # pdf_page is a NoneType, not a response object;
    # nothing to grab here
    # BOOOOOOOO

    # time.sleep(3)

    # nope
    # driver.execute_script('document.execCommand("SaveAs")')

    # Selenium can't find the embed tag at all; view-source is disabled on the page.
    # src = driver.find_element_by_xpath('/html/body/embed').get_attribute('src')
    # print src

    # pdf = urllib.URLopener()
    # pdf.retrieve(src, 'allegheny_county_pdfs/%s.pdf' % doc_title)

    # this is there in the hidden page source but not targetable by Selenium for some reason.
    # save_button = driver.find_element_by_id('save')
    # save_button.click()

    # with open('allegheny_county_pdfs/%s.pdf' % doc_title, 'a+') as f:
    #     f.write(XXXXXXXX.read())