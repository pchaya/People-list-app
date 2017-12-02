# Managing list operations for file IO and append

class PeopleList(object):

    def __init__(self):
        # create a new empty list for each group of people
        self.list = []
        self.read()
    
    def read(self):
        # read people from file and fill list upon creating list
        # keep file open only for duration of read
        with open('people.txt', 'r') as f:
            for text in f.read().split(';'):
                self.list.append(text)

    def write(self, toWrite):
        # write contents of list back to file
        with open('people.txt', 'w') as f:
            # write first person to avoid preceding ';'
            f.write(toWrite[0])
            # check for single element list, then write remaining
            if (len(toWrite) > 1):
                for i in range(1, len(toWrite)):
                    f.write(';')
                    f.write(toWrite[i])
        
    def add(self, name):
        # a person to the group
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

    def print(self):
        # print out all people in list
        print('Here are all your classmates:',)
        for person in self.list:
            print('\t+', person,)

if __name__ == '__main__':
    classmates = PeopleList()
    classmates.print()
    classmates.remove('John Watson')
    classmates.add('Sherlock Holmes')