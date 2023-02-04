import os

# folder path
# r means the string will be treated as raw string : a character following a backslash is included in the string without change 
dir_path = r'/home/dell/projet/dossier'
print (dir_path)


# test de la fonction os.getcwd() :
#########################
print("\ntest fonction os.getcwd()")
current_path=os.getcwd()
print (current_path)


# test de la fonction os.path.joint() :
#########################
print("\ntest fonction os.path.joint")
chemin=os.path.join(current_path, "dossier")
print (chemin)


# test de la fonction os.listdir() :
#########################
print("\ntest fonction os.listdir()")
# liste = os.listdir(r"./dossier")
liste = os.listdir(chemin)
print (liste)


# list to store files
#########################
print("\nfonction générale pour lister les fichiers dans un dossier")
res = []
# Iterate directory
for item in os.listdir(chemin):
    # check if current item is a file
    if os.path.isfile(os.path.join(chemin, item)):
        res.append(item)
print(res)


# list to store files with specific extension
#########################
print("\nfonction générale pour lister les fichiers qui se terminent par .mp4")
res = []
# Iterate directory
for item in os.listdir(chemin):
    # check if current item ends with ".mp4"
    if item.endswith(".mp4"):
        res.append(item)
print(res)



# rename files
#########################
print("\nfonction renommage des fichiers")
os.chdir(chemin) 
for nom in res:
    # parsing filename
    nom_sep=nom.split("_")
    year=nom_sep[0][0:4]
    month=nom_sep[0][4:6]
    day=nom_sep[0][6:]
    print (year, month, day)

    hour=nom_sep[1][0:2]
    min=nom_sep[1][2:4]
    sec=nom_sep[1][4:6]
    print (hour, min, sec)

    new_name="-".join([year, month, day]) + " " + "".join([hour, min, sec]) + ".mp4"
    print(new_name)

    os.rename(nom,new_name)

print ("done")