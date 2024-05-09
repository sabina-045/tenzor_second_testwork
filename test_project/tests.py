import pychrome

from test_project.pages import BasePage


browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab("https://sbis.ru/")
tab.start()
tab.call_method('Network.enable')
tab.call_method('Page.navigate', url="https://sbis.ru/", _timeout=5)
tab.wait(5)

page = BasePage(tab)
page.take_total_page_and_dom_load_time()
page.go_to_tariffs_page()
page.tariffs_page_click_on_restaurants_part()
page.open_feedback_card()

tab.stop()
browser.close_tab(tab)
