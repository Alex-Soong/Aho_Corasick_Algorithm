class Node():
    def __init__(self, IsBole=True, Character=None):
        self.__goto = {}
        self.__fail = None
        self.__output = None
        self.__isbole = IsBole
        self.__character = Character
 
    def AddGotoNode(self, Character):
        if Character not in self.__goto.keys():
            currentNode = Node(self.__character is None, Character)
            self.__goto[Character] = currentNode
            return currentNode
        else:
            return self.__goto[Character]
 
    def ConstructionFail(self, TargetNode):
        for currentNode in self.__goto.values():
            currentNode.AddFailNode(TargetNode)
        for currentNode in self.__goto.values():
            currentNode.ConstructionFail(currentNode.__fail)
 
    def AddFailNode(self, TargetNode):
        if self.__isbole:
            self.__fail = TargetNode
        elif self.__character in TargetNode.__goto.keys():
            self.__fail = TargetNode.__goto[self.__character]
        else:
            self.__fail = TargetNode.__fail
 
    def AddOutput(self, Pattern):
        self.__output = Pattern
 
    def NextNode(self, Character):
        currentNode = self
        while True:
            currentNode.PrintResult()
            if Character in currentNode.__goto.keys():
                return currentNode.__goto[Character]
            elif currentNode.__character is None:
                return currentNode
            currentNode = currentNode.__fail
 
    def PrintResult(self):
        if self.__output is not None:
            # print(self.__output, end=" ")
            pass