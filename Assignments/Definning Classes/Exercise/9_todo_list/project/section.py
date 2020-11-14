class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        task = [x for x in self.tasks if x.name == task_name]
        if task:
            task = task[0]
            task.completed = True
            return f'Completed task {task.name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        completed_task_counter = []

        for x in range(len(self.tasks)):
            if self.tasks[x].completed:
                completed_task_counter.append(x)

        [self.tasks.pop(x) for x in completed_task_counter]
        return f'Cleared {len(completed_task_counter)} tasks.'

    def view_section(self):
        data = f'Section {self.name}:\n'
        for x in self.tasks:
            data += f'{x.details()}\n'
        return data
