import datetime

class Item(object):
    def __init__(self, complete, action):
        self.complete = complete
        self.action = action

    def compile(self,complete, action):
        task = []
        now = datetime.date.today()
        task.append(now)
        task.append(complete)
        task.append(action)
        file = open('todos.txt', 'a')
        file.write(f'Created: {now} | Action: {action} | Completed?: {complete} \n')
        file.close()
