class Pie:
  def __init__(self, name, filling, crust):
    self.name = name
    self.filling = filling
    self.crust = crust

p1 = Pie("Key lime", "lime custard", "graham cracker")
p2 = Pie("Chocolate silk", "chocolate mousse", "graham cracker")

print(p2.name)
print(p2.filling)
print(p2.crust)
