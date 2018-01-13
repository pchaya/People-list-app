# Managing list operations for file IO and append

class PeopleList(object):

    def __init__(self, name = "My Group"):
        # create a new empty list for each group of people
        self.name = name
        self.list = []
        self.read()
    
    def read(self):
        # read people from file and fill list upon creating list
        # keep file open only for duration of read
        try:
            with open('people.txt', 'r') as f:
                for text in f.read().split(';'):
                    self.list.append(text)
        except IOError as error:
            print(error.errno)
            print(error)
        

    def write(self, toWrite):
        # write contents of list back to file
        try:
            with open('people.txt', 'w') as f:
                # write first person to avoid preceding ';'
                f.write(toWrite[0])
                # check for single element list, then write remaining
                if (len(toWrite) > 1):
                    for i in range(1, len(toWrite)):
                        f.write(';')
                        f.write(toWrite[i])
        except IOError as error:
            print(error.errno)
            print(error)
    
    # takes a list of names, and adds to group
    def addList(self, toAdd):
        for i in range(len(toAdd)):
            self.list.append(toAdd[i])
        
        # update file
        self.write(self.list)

    # takes a single name (str), and adds to group
    def add(self, name):
        # add person to the group
        self.list.append(name)

        # update file
        self.write(self.list)

    def remove(self, name):
        # find and remove a person from the group
        if name in self.list:
            self.list.remove(name)
            # update file
            self.write(self.list)
        else:
            print(name, ' is not in the group!')

    def display(self):
        # print out all people in list
        toDisplay = 'Here are all your group mates:'
        for person in self.list:
            toDisplay += ('\n+ ' + person)
        return toDisplay

if __name__ == '__main__':
    classmates = PeopleList()
    print(classmates.display())
    classmates.remove('John Watson')
    classmates.add('Sherlock Holmes')