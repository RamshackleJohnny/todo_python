from item import Item

class Manager(object):
    def __init__(self):
        pass

    def menu(self):
        print("Do you want to add something or check your list?")
        option = input("> ")
        option = option.lower()
        print(option)
        if option == 'add':
            Manager.add('')
        elif option == 'check':
            print("These things are on your list")
            Manager.view('')
            Manager.menu('')
        else:
            print("Sorry, I have no idea what you're talking about.")
            Manager.menu('')

    def view(self):
        file = open('todos.txt')
        print (file.read())


    def add(self):
        print("What do you want to add to your list?")
        task = input("> ")
        print("Is it done already?")
        done = input("> ")
        if done =='yes':
            done = True
        elif done == 'no':
            done = False
        print('Your list now contains the following')
        Item.compile('', done, task)
        Manager.view('')
