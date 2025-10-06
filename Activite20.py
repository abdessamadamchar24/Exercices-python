adresses_ip = ["192.168.0.1" , "10.0.0.1" , "172.16.0.1" , "200.100.50.1" , "169.254.0.1"]

classes={
    "192.168.0.1" : "classe C",
    "10.0.0.1" : "classe A",
    "172.16.0.1" : "classe B",
    "200.100.50.1" : "adresse IP publique",
    "169.254.0.1" : "adresse IP de lien local (APIPA)"
}

#Questoin 1:
print("1) La premiere adresse dans la liste c'est ", adresses_ip[0])


#Questoin 2:
print("2) La derniere adresse dans la liste c'est ", adresses_ip[len(adresses_ip)-1])



#Questoin 3:
print("3) La troisieme adresse dans la liste c'est ", adresses_ip[2])


#Questoin 4:
adresses_ip.append("172.31.0.1")


#Questoin 5:
adresses_ip.remove("200.100.50.1")


#Questoin 6:
print("6)Le nombre d'adresses restanats dans la liste c'est ", len(adresses_ip))


#Questoin 7:
ip="192.168.0.1"
if ip in adresses_ip:
    print("7) ",ip , " est presente dans la liste")
else:
    print(ip , " n'est pas presente dans la liste")



#Questoin 8:
ip="10.0.0.1"
print("8) La classe d'adresse IP de ",ip," :",classes[ip])

#Questoin 9:
adresses_ip.sort()
print("9) la liste trie: adresses_ip=",adresses_ip)

#Questoin 10:
isClassC=True
for cle,valeur in classes.items():
    if valeur != "classe C":
        isClassC=False
        break

if(isClassC):
    print("10) Toutes les adresses Ip de la liste appartiennent a la classe C")
else:
    print("10) Il existe des adresses Ip de la liste n'appartiennent pas a la classe C")


#Questoin 11:
c=0
for cle,valeur in classes.items():
    if valeur=="adresse IP publique":
        c+=1

print("11)Le nombre d'adresses Ip publiques dans la liste c'est: ",c)