class étudiant:
    def __init__(self, nom, prenom, age, CNE, moyenne):
        self.n = nom
        self.p = prenom
        self.a = age
        self.c = CNE
        self.m = moyenne


# creation de la liste
list = []
# appending instances to list
list.append(étudiant('elarusi', 'kholoud', 21, 'p14', 19))
list.append(étudiant('rouan', 'houda', 22, 'p15', 14))
list.append(étudiant('salimi', 'arwa', 23, 'p16', 16))
for obj in list:
    print("***la liste triee par age***\n")
    print(obj.n, obj.p, obj.a, obj.c, obj.m, sep=' ')

list.sort(key=lambda x: x.a)
for obj in list:
    print("nom: ", obj.n, " prenom: ", obj.p, " age: ", obj.a, " cne: ", obj.c, " moyenne: ", obj.m, sep=' ')
print("\n")

