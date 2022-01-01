#classe
class Vecteur2D:
 """LesVecteursplans."""
 def __init__(self, x0=0, y0=0):
     """Constructeuravecparametrespardefaut."""
     self.x=x0 #initialisationdexety,attributsd'instance
     self.y=y0
#programmeprincipal
print(" vecteur2d sans parametres".center(50,'-'))
v1=Vecteur2D()
print("x=%g,y=%g" % (v1.x,v1.y))
print()
print("vecteur2d avec 2 parametres".center(50,'-'))
v2=Vecteur2D(2,1)
print("x=%g,y=%g" % (v2.x,v2.y))

