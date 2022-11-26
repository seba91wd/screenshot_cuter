# -*-coding:Latin-1 -*
from PIL import Image, ImageEnhance
import glob

# Ce programe rogne et re-nomme automatiquement des images
# en les classent par ordre décroissant
# utiliser pour redimentionner des captures d'écran de scan sur internet

#Dossier source des image
source_dir = "/home/pi/Documents/scan/*.png"

#Dossier de sauvegarde
save_dir = "/home/pi/Documents/scan/"

#Creation list decroissante
my_images_list = glob.glob(source_dir)
my_images_list = sorted(my_images_list)

count_file = 0          #Compteur de fichier
count = 1               #Compteur de pages
l = 271                 #Dimmention découpage (pixel le plus a gauche)
t = 220                 #Dimmention découpage (pixel le plus haut)
w = 1361                #Dimmention découpage (pixel le plus a droite)
h = 1885                #Dimmention découpage (pixel le plus bas)
box = (l, t, l+w, t+h)  #Creation de la boite de decoupe
go_all = 0              #Demare le découpage de toutes les images si (1)
objet_nb = (len(my_images_list))  #Enumération des fichiers

print ("<------------------------------------------------>")
print ("Nombre d'images a traiter : %s") % (objet_nb)

for x in range (0, objet_nb):
    i_file = my_images_list[(count_file)]
    s_file = (i_file.split("/"))
    print "%s/%s : %s" % (count_file + 1, objet_nb, s_file[5])
    count_file = (count_file + 1)
print ("<------------------------------------------------>")
print (" ")
count_file = 0          #Remise a 0 du compteur de fichier

for my_image in my_images_list:
    im = Image.open(my_image)
    fichier = (my_images_list[(count_file)])

    if count == 1:
        #im.show()  #Ouvre l'image dans une fenetre (inutile en ssh)
        print (fichier.split("/")[5])
        reponse = raw_input("Cette image est elle la 1er de la série ? [o/n] ")
        if reponse == "o":
            print "Indiquer le numero de page ex: 123"
            count = int(raw_input("Page : "))
            print("Début de traitement...")
            go_all = 1
        elif reponse == "n":
            print("Les fichiers doivent etre re-daté")
            exit()
        else:
            print("Répondez par o ou n")
            exit()
    
    if go_all == 1:
        size_im = im.size
        area = im.crop(box)
        size_area = area.size
        print (" ")
        print ("<------------------------------------------------>")
        print "Image : %s / %s" % ((count_file + 1), objet_nb)
        print "Traitement de", (fichier.split("/")[5])
        print "Dimension post découpage  =>", (size_im)
        print "Dimension apres découpage =>", (size_area)
        print "Enregitrer sous V3P%s.png" % (count)
        area.save((save_dir + "V3P%s" + ".png") % (count))
        count_file = (count_file + 1)
        count = (count + 1)
print ("")
print ("<------------------------------------------------>")
print count_file, "Images découpées dans", save_dir
print ("Fin de traitement")