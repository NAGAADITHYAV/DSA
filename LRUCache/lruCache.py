class ListNode:
  def __init__(self, key = 0, val = 0, next = None, prev = None):
    self.key = key
    self.val = val
    self.next = next
    self.prev = prev
    
class LRUCache:

  def __init__(self, capacity: int):
    self.dict = {}
    self.capacity = capacity
    self.head = ListNode()
    self.tail = ListNode()
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def insert(self, node):
    prev = self.tail.prev
    prev.next = node
    node.prev = prev
    self.tail.prev = node
    node.next = self.tail

  def delete(self, node):
    prev = node.prev
    nextnode = node.next
    prev.next = nextnode
    nextnode.prev = prev
    return node

  def get(self, key: int) -> int:
    if key in self.dict:
      node = self.delete(self.dict[key])
      self.insert(node)
      return self.dict[key].val
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    node = ListNode(key, value)
    if key in self.dict:
      self.delete(self.dict[key])
    self.insert(node)
    self.dict[key] = node

    if self.capacity < len(self.dict):
      node = self.delete(self.head.next)
      del self.dict[node.key]
      


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)