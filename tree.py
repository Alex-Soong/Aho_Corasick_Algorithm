from node import Node


class Tree():
    def __init__(self):
        self.__root = Node()
 
    def AddPatterns(self, *Patterns):
        for pattern in Patterns:
            currentNode = self.__root
            for character in pattern:
                currentNode = currentNode.AddGotoNode(character)
            currentNode.AddOutput(pattern)
        self.__root.AddFailNode(self.__root)
        self.__root.ConstructionFail(self.__root)
        pass
 
    def Matching(self, text):
        currentNode = self.__root
        for character in text:
            currentNode = currentNode.NextNode(character)