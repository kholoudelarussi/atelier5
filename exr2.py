class Vecteur2D:
 """Definition d'une classe."""
 def __init__(self, x0=0, y0=0):
     """Constructeur avec parametres par defaut."""
     self.x = x0 # initialisation de x et y, attributs d'instance
     self.y = y0
 def __add__(self, autre):
     """Addition vectorielle."""
     return Vecteur2D(self.x+autre.x, self.y+autre.y)
 def __str__(self):
     """Affichage d'un Vecteur2D."""
     return "Vecteur({:g}, {:g})".format(self.x, self.y)
# test
v1, v2 = Vecteur2D(2, 1), Vecteur2D(2, 8)
print(v1)
print(v2)
print(v1 + v2)
