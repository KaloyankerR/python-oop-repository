from Lab.list import IntegerList
import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_init(self):
        new_list = IntegerList(1, 2, 3, 4, 5)
        self.assertEqual(new_list.get_data(), [1, 2, 3, 4, 5])

    def test_add(self):
        self.assertEqual(self.list.add(42), [42])

    def test_add_raises_value_error(self):
        self.assertRaises(ValueError, self.list.add, 'str')

    def test_remove_by_index(self):
        self.list.add(10)
        self.assertEqual(self.list.remove_index(0), 10)

    def test_remove_by_index_raises_index_error(self):
        self.assertRaises(IndexError, self.list.remove_index, 0)

    def test_init_takes_only_integers(self):
        new_list = IntegerList('pesho', 1, True, 34)
        self.assertEqual(new_list.get_data(), [1, 34])

    def test_get_should_return_specific_element(self):
        self.list.add(21)
        self.assertEqual(self.list.get(0), 21)

    def test_get_should_return_specific_element_raises_indexerror(self):
        self.assertRaises(IndexError, self.list.get, 0)

    def test_insert(self):
        self.list.add(12)
        self.list.insert(0, 10)
        self.assertEqual(self.list.get_data(), [10, 12])

    def test_insert_index_out_of_range_raises_indexerror(self):
        self.assertRaises(IndexError, self.list.insert, 0, 1)

    def test_insert_element_is_not_an_integer_raises_valueerror(self):
        self.list.add(12)
        self.assertRaises(ValueError, self.list.insert, 0, 'baba')

    def test_get_biggest_integer(self):
        new_list = IntegerList(2, 21, 20, 5)
        self.assertEqual(new_list.get_biggest(), 21)

    def test_get_index(self):
        new_list = IntegerList(1, 24, 12, 3)
        self.assertEqual(new_list.get_index(1), 0)


if __name__ == '__main__':
    unittest.main()
