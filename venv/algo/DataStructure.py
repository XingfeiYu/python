class TreeNode:
    def __init__(self, value): self.value = value

    def setLeft(self, left): self.left = left

    def setRight(self, right): self.right = right


head = TreeNode(3)
head.setLeft(TreeNode(2))
head.setRight(TreeNode(4))
print head.value
print head.left.value
print head.right.value

def printInfo(): print "Here is module DataStructure"