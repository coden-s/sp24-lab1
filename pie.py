class Pie:
  def __init__(self, name, filling, crust):
    self.name = name
    self.filling = filling
    self.crust = crust

p1 = Pie("Key lime", "lime custard", "graham cracker")
p2 = Pie("Apple", "apples", "dough")
p3 = Pie("Ice Cream Pie", "Coockie and Cream Ice Cream", "Oreos")
p4 = Pie("Broreo Pot Pie, Brussel Sprouts and Chicken", "Minced Oreo")
p5 = Pie("Strawberry Rhubarb", "Strawberry and Ruhbarb Glaze", "graham crackers")
p6 = Pie("Pumpkin", "pumpkin", "dough")
p7 = Pie("Shepherd's Pie", "peas, carrots, and lamb", "mashed potatoes")


print(p1.name)
print(p1.filling)
print(p1.crust)
