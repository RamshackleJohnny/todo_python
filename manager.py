from item import Item

class Manager(object):
    def __init__(self):
        pass

    def menu(self):
        print("Do you want to add something, remove something, or check your list?")
        option = input("> ")
        option = option.lower()
        print(option)
        if option == 'add':
            Manager.add('')
        elif option == 'check':
            print("These things are on your list")
            Manager.view('')
            Manager.menu('')
        elif option == 'remove':
            inpot = open('todos.txt','r').readlines()
            print('These are your options, which do you want to remove? (Write the line number)')
            Manager.view('')
            theline = input("> ")
            theline = int(theline)
            with open('todos.txt','w') as output:
                for thedo, line in enumerate(inpot):
                    if thedo != theline - 1:
                        output.write(line)
            print('Your list now contains the following')
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
        done = done.lower()
        if done =='yes':
            done = True
        elif done == 'no':
            done = False
        print('Your list now contains the following')
        Item.compile('', done, task)
        Manager.view('')
        Manager.menu('')
