class Pie:
  def __init__(self, name, filling, crust):
    self.name = name
    self.filling = filling
    self.crust = crust

p1 = Pie("Key lime", "lime custard", "graham cracker")
p2 = Pie("Apple", "apples", "dough")
p3 = Pie("Ice Cream Pie", "Coockie and Cream Ice Cream", "Oreos")

print(p1.name)
print(p1.filling)
print(p1.crust)
