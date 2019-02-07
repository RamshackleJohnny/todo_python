class Item(object):
    def __init__(self, complete, action):
        self.complete = complete
        self.action = action

    def compile(self):
        task = []
        task.append(action)
        task.append(complete)
        now = datetime.date.today()
        task.append(now)
        return task

def func():
    print('This works')
