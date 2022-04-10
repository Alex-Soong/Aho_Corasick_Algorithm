class Node():
    def __init__(self, IsBole=True, Character=None):
        self.__goto = {}
        self.__fail = None
        self.__output = None
        self.__isbole = IsBole
        self.__character = Character
 
    def addGotoNode(self, Character):
        if Character not in self.__goto.keys():
            currentNode = Node(self.__character is None, Character)
            self.__goto[Character] = currentNode
            return currentNode
        else:
            return self.__goto[Character]
 
    def constructionFail(self, TargetNode):
        for currentNode in self.__goto.values():
            currentNode.addFailNode(TargetNode)
        for currentNode in self.__goto.values():
            currentNode.constructionFail(currentNode.__fail)
 
    def addFailNode(self, TargetNode):
        if self.__isbole:
            self.__fail = TargetNode
        elif self.__character in TargetNode.__goto.keys():
            self.__fail = TargetNode.__goto[self.__character]
        else:
            self.__fail = TargetNode.__fail
 
    def addOutput(self, Pattern):
        self.__output = Pattern
 
    def nextNode(self, Character):
        currentNode = self
        while True:
            currentNode.printResult()
            if Character in currentNode.__goto.keys():
                return currentNode.__goto[Character]
            elif currentNode.__character is None:
                return currentNode
            currentNode = currentNode.__fail
 
    def nextNodeAdvanced(self, Character):
        if Character in self.__goto.keys():
            self.printResult()
            return self.__goto[Character]
        else:
            return self

    def printResult(self):
        if self.__output is not None:
            print(self.__output, end=" ")
            pass
        
    def getGotoKeys(self):
        return self.__goto.keys()
    
    def getGotoNodes(self):
        return self.__goto.values()
    
    def getFailNode(self):
        return self.__fail
    
    def addEdge(self, character, node):
        if character not in self.__goto.keys():
            self.__goto[character] = node
        
