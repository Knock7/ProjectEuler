class Node:
  def __init__(self, val):
    self.l = None
    self.r = None
    self.v = val

class Tree:
  def __init__(self):
    self.root = None

  def getRoot(self):
    return self.root

  def add(self, val):
    if(self.root == None):
      self.root = Node(val)
    else:
      self._add(val, self.root)

  def _add(self, val, node):
    if(val < node.v):
      if(node.l != None):
        self._add(val, node.l)
      else:
        node.l = Node(val)
    else:
      if(node.r != None):
        self._add(val, node.r)
      else:
        node.r = Node(val)

  def deleteTree(self):
    self.root = None

  def printTree(self):
    if(self.root != None):
      self._printTree(self.root)

  def _printTree(self,node):
    if(node != None):
      self._printTree(node.l)
      print str(node.v) + ' '
      self._printTree(node.r)
  
  def getArray(self):
    if(self.root != None):
      return self._getArray(self.root)
    else:
      return None

  def _getArray(self,node):
    if(node != None):
      a = self._getArray(node.l)
      a.append(node.v)
      a.append(self._getArray(node.r))
      return a
    else:
      return None

#tree = Tree()
#tree.add(3)
#tree.add(4)
#tree.add(0)
#tree.add(8)
#tree.add(2)
#tree.printTree()
#print (tree.find(3)).v
#print tree.find(10)
#tree.deleteTree()
#tree.printTree()
