import unittest
from Algorithm import Algorithm

class Item:
    def __init__(self, _weight, _value):
        self.weight = _weight
        self.value = _value


class BackBackTester(unittest.TestCase):


    def get_mock_item_list(self):
        item_list = []
        item1 = Item(1, 100)
        item2 = Item(2, 200)
        item3 = Item(3, 300)
        item_list.append(item1)
        item_list.append(item2)
        item_list.append(item3)
        return item_list

    def test_simple_case(self):
        item_list = self.get_mock_item_list()
        algorithm = Algorithm
        result_id_list = algorithm.slove(input_item_list=item_list, weight=400);
        self.assertEquals(result_id_list,[1,3])
