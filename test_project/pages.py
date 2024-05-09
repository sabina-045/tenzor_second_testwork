from test_project.utils import *
from selector import *


class BasePage:
    def __init__(self, tab):
        self.tab = tab

    def take_total_page_and_dom_load_time(self):
        """Получаем полное время загрузки страницы и DOM."""
        self.tab.call_method('Performance.enable')
        metrics = self.tab.call_method('Performance.getMetrics')
        start_time = metrics['metrics'][35]['value']
        timestamp = metrics['metrics'][0]['value']
        dom_content_loaded = metrics['metrics'][34]['value']
        page_total_load_result = timestamp - start_time
        dom_load_result = dom_content_loaded - start_time
        self.tab.call_method('Performance.disable')

        print(f'Время загрузки страницы {round(page_total_load_result, 2)} миллисекунд(а).',
              f'Время загрузки DOM {round(dom_load_result, 2)} миллисекунд(а).', sep='\n')

    def go_to_tariffs_page(self):
        """Переходим на страницу с тарифами."""
        node_id = take_element_node_id(self.tab, SBIS_PAGE_TARIFFS_BUTTON_SELECTOR)
        click_on_element(self.tab, node_id)
        self.tab.wait(5)

    def tariffs_page_click_on_restaurants_part(self):
        """Нажимаем на вкладку для ресторанов."""
        node_id = take_element_node_id(self.tab, TARIFFS_PAGE_RESTAURANTS_BUTTON_SELECTOR)
        click_on_element(self.tab, node_id)
        self.tab.wait(5)

    def open_feedback_card(self):
        """Открываем карточку с обратной связью."""
        node_id = take_element_node_id(self.tab, TARIFFS_PAGE_FEEDBACK_CARD)
        self.tab.call_method('DOM.scrollIntoViewIfNeeded', nodeId=node_id)
        click_on_element(self.tab, node_id)
        self.tab.wait(5)
