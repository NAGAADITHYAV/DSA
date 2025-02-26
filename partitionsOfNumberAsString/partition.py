class Partition:
  def __init__(self, s):
    self.partitions = []
    self.partition(s)

  def print_partitions(self):
    for x in self.partitions:
      print(x)

  def partition(self, s):
    pass

p = Partition('abc')
p.print_partitions()
