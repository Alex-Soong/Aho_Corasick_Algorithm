from tree import Tree
import time
 
if __name__ == '__main__':

    t = Tree()
    t.AddPatterns('Harry', 'Hagrid', 'Snape', 'Hermione', 'Quidditch', 'Dumbledore',
                  'Dursley', 'Ron', 'McGonagall', 'Dudley', 'Hogwarts')
    file = open("text.txt", "r")
    time1 = time.time()
    t.Matching(file.read())
    time2 = time.time()
    print()
    print('Before optimization: total time: ' + str(time2 - time1) + "s")
    print()