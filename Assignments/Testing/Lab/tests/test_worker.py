import unittest
from Lab.worker import Worker


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('John', 1000, 100)

    def test_worker_is_initialized(self):
        self.assertEqual(self.worker.name, 'John')
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 100)

    def test_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)
        # self.assertEqual(self.worker.energy - 1, old_energy)

    def test_worker_raises_exception_when_working_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_is_increased_after_work(self):
        old_salary = self.worker.salary
        self.worker.work()
        self.assertEqual(self.worker.money - old_salary, self.worker.salary)

    def test_worker_energy_decreased_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(old_energy - self.worker.energy, 1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, 'John has saved 0 money.')

if __name__ == '__main__':
    unittest.main()

