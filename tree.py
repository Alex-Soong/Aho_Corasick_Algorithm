from node import Node


class Tree():
    def __init__(self, advanced=False):
        self.__root = Node()
        self.__advanced = advanced
        self.__result = {}
        
    def addPatterns(self, *Patterns):
        for pattern in Patterns:
            self.__result[pattern] = 0
            currentNode = self.__root
            for character in pattern:
                currentNode = currentNode.addGotoNode(character)
            currentNode.addOutput(pattern)
        self.__root.addFailNode(self.__root)
        self.__root.constructionFail(self.__root)
        if self.__advanced == True:
            self.advancedTree()
 
    def matching(self, text):
        currentNode = self.__root
        if self.__advanced == True:
            for character in text:
                currentNode = currentNode.nextNodeAdvanced(character, self)
        else:
            for character in text:
                currentNode = currentNode.nextNode(character, self)
            
        
    def advancedTree(self):
        lst = self.levelOrder()
        
        for node in lst:
            for character in " .,:\"?!QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm\n":
                if character not in node.getGotoKeys():
                    node.addEdge(character, node.getFailNode())

    def levelOrder(self):
        lst = []
        queue = []
        queue.append(self.__root)
        while queue:
            cur = queue.pop(0)
            lst.append(cur)
            for node in cur.getGotoNodes():
                queue.append(node)
        return lst
    
    def addResult(self, str):
        self.__result[str] = self.__result[str] + 1
        
    def getResult(self):
        return self.__result