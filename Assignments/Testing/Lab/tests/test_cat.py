from Lab.cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Joe')

    def test_init(self):
        self.assertEqual(self.cat.name, 'Joe')
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_cat_increases_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
