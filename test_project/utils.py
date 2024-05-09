def take_element_node_id(tab, selector):
    """Получаем node_id элемента."""
    document = tab.call_method('DOM.getDocument')
    document_root_node_id = document["root"]["nodeId"]
    element_node_id = tab.call_method(
        'DOM.querySelector',
        nodeId=document_root_node_id,
        selector=selector)
    node_id = element_node_id['nodeId']

    return node_id


def click_on_element(tab, node_id):
    """Функция нажатия кнопкой мыши."""
    box_model = tab.call_method('DOM.getBoxModel', nodeId=node_id)
    coordinates_x = round(box_model['model']['content'][0] +
                          box_model['model']['width'] / 2)
    coordinates_y = round(box_model['model']['content'][1] +
                          box_model['model']['height'] / 2)
    tab.call_method('Input.dispatchMouseEvent',
                    type='mouseMoved',
                    x=coordinates_x, y=coordinates_y)
    tab.call_method('Input.dispatchMouseEvent',
                    type='mousePressed',
                    x=coordinates_x, y=coordinates_y,
                    button='left', clickCount=1)
    tab.call_method('Input.dispatchMouseEvent',
                    type='mouseReleased',
                    x=coordinates_x, y=coordinates_y,
                    button='left', clickCount=1)
