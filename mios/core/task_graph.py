class TaskGraph:
    def __init__(self):
        self.tasks = {}
        self.dependencies = {}

    def add_task(self, task):
        self.tasks[task] = []

    def add_dependency(self, task1, task2):
        if task1 not in self.dependencies:
            self.dependencies[task1] = []
        self.dependencies[task1].append(task2)

    def get_next_tasks(self):
        ready_tasks = []
        for task, deps in self.dependencies.items():
            if all(dep in self.tasks for dep in deps):
                ready_tasks.append(task)
        return ready_tasks
