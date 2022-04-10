from tree import Tree
import time
import os
 
if __name__ == '__main__':

    patterns = [
        'Harry', 'Hagrid', 'Snape', 'Hermione', # 'Quidditch', 'Dumbledore', 
        # 'Dursley', 'Ron', 'McGonagall', 'Dudley', 'Hogwarts', 'thanks', 'Ginny',
        # 'what', 'let', 'wand', 'Voldemort'
        ]
    t1 = Tree(advanced=False)
    t1.addPatterns(*patterns)
    t2 = Tree(advanced=True)
    t2.addPatterns(*patterns)
    
    file = open("text.txt", "r")
    text = file.read()
    time1 = time.time()
    t1.matching(text)
    time2 = time.time()
#     os.system('pause')
    time3 = time.time()
    t2.matching(text)
    time4 = time.time()
    
    print()
    print()
    print('Before optimization: total time: ' + str(time2 - time1) + "s")
    print()
    print('After optimization: total time: ' + str(time4 - time3) + "s")
    print()
    