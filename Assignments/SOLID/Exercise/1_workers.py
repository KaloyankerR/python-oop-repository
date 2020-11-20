class Worker:
    @staticmethod
    def work():
        print("I'm working!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if 'Worker' in [x.__name__ for x in worker.__class__.__mro__]:
            self.worker = worker
        else:
            assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker:
    @staticmethod
    def work():
        print("I work very hard!!!")
