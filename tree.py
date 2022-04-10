from node import Node


class Tree():
    def __init__(self, advanced=False):
        self.__root = Node()
        self.advanced = advanced
        
    def addPatterns(self, *Patterns):
        for pattern in Patterns:
            currentNode = self.__root
            for character in pattern:
                currentNode = currentNode.addGotoNode(character)
            currentNode.addOutput(pattern)
        self.__root.addFailNode(self.__root)
        self.__root.constructionFail(self.__root)
        if self.advanced == True:
            self.advancedTree()
 
    def matching(self, text):
        currentNode = self.__root
        if self.advanced == True:
            for character in text:
                currentNode = currentNode.nextNodeAdvanced(character)
        else:
            for character in text:
                currentNode = currentNode.nextNode(character)
            
        
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