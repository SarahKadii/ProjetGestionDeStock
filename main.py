import re

#Ouverture du fichier en lecture
file = open('produits.txt',"r")
lines = file.readlines()

#initialisation d'une liste vide
liste = []
for line in lines:
    #Enlever l'espace et le \n de ma cdc
    line = re.split(' |\n',line) 
    #Supprimer les '' de la liste
    if '' in line:
        line.remove('')
    #Concatenation des deux chaines
    liste += line
    #print(line)
print(liste)   

#Initialisation des produits
liste2 = ['Stylo','Crayon','Trousse']
i = 0
while i < len(liste):
    if liste[i] in liste2:
        print(liste[i]+ " existe dans la liste des produits")
    else:
        print(liste[i]+ " n'existe pas dans la liste des produits")
    i += 2
    
       


