import pandas as pd


def demandeGroupes():
     """Fonction qui demande à l'utilisateur sont groupe de TD et TP, retourne un tableau avec en premier index le TD et en deuxième index le TP.
     """

     td = input("Quel est votre groupe (1ATDA, 1ATDB, 1ATDC) ? ")
     tp = input("Quel est votre groupe (1ATP1, 1ATP2, 1ATP3, 1ATP4, 1ATP5) ? ")
     groups = []
     
     #demande de saisir à nouveau le groupe de TD si il y a une erreur
     while td == "1ATDA" and td == "1ATDB" and td == "1ATDC":
          td = input("Erreur, veuillez saisir un groupe valide (1ATDA, 1ATDB, 1ATDC) ? ")

     #demande de saisir à nouveau le groupe de TP si il y a une erreur
     while tp == "1ATP1" and tp == "1ATP2" and tp == "1ATP3" and tp == "1ATP4" and tp == "1ATP5":
          td = input("Erreur, veuillez saisir un groupe valide (1ATDA, 1ATDB, 1ATDC) ? ")

     #formatage du groupe de TD saisie par l'utilisateur
     groupeTD = ""
     if td == "1ATDA":
          groupeTD = " 1ATDA "
     elif td == "1ATDB":
          groupeTD = " 1ATDB "
     else:
          groupeTD = " 1ATDC "

     #formatage du groupe de TP saisie par l'utilisateur
     groupeTP = ""
     if tp[1] == "1ATP1":
          groupeTP = " 1ATP1 "
     elif tp[1] == "1ATP2":
          groupeTP = " 1ATP2 "
     elif tp[1] == "1ATP3":
          groupeTP = " 1ATP3 "
     elif tp[1] == "1ATP4":
          groupeTP = " 1ATP4 "
     else:
          groupeTP = " 1ATP5 "
     
     groups.append(groupeTD) #ajouts du groupe de TD après formatage dans le tableau "groups"
     groups.append(groupeTP) #ajouts du groupe de TP après formatage dans le tableau "groups"
     
     return groups

def groupeTaleau(groups):
     """Fonction qui permet de crée un nouveau dataframe et le retourne avec seulement les cour d'un TD, TP, CM
     
     PARAMÉTRES : 
     groups => array, contient le groupe de TD à l'index 0 et le groupe de TP à l'index 1
     """     

     #Enregistrement dans une variable "data" des données du fichier ADECAL_officiel.csv au format pandas.core.frame.DataFrame
     data = pd.DataFrame(pd.read_csv("ADECAL_officiel.csv"))

     #Enregistrement dans une variable "dataTD" de l'ensemble des cours ayant comme groupe le td choisi par l'utilisateur
     td = groups[0]
     dataTD = data.query("Groupe == @td") #la méthode ".query" (s'implique sur un objet de type dataframe) permet de selectionner toutes les lignes d'un dataframe respectant la condition entre guillement (@ => référence à une variable)
     #Enregistrement dans une variable "dataTP" de l'ensemble des cours ayant comme groupe le tp choisi par l'utilisateur
     tp = groups[1]
     dataTP = data.query("Groupe == @tp")
     #Enregistrement dans une variable "dataCM" de l'ensemble des cours en CM (commun à tout TD ou TP)
     cm = " 1A "
     dataCM = data.query("Groupe == @cm")
     
     courGroup = []
     
     #Parcour de la liste de "dataTD" pour les ajouter au tableau "courGroup"
     for lineTD in range(len(dataTD)):
          courGroup.append(dataTD.iloc[lineTD, :]) #la methode ".iloc" (s'implique sur un objet de type dataframe) permet de selectionner une ou plusieurs lignes, une ou plusieurs colonnes, ou une valeur précise ([ligne, colone). Ici elle permet de selectionner chaque ligne a chaque tour de boucle  
          
     #Parcour de la liste de "dataTP" pour les ajouter au tableau "courGroup"
     for lineTP in range(len(dataTP)):
          courGroup.append(dataTP.iloc[lineTP, :])
     
     #Parcour de la liste de "dataCM" pour les ajouter au tableau "courGroup"
     for lineCM in range(len(dataCM)):
          courGroup.append(dataCM.iloc[lineCM, :])
        
          
     return pd.DataFrame(courGroup)

def modules(groupsTrier):
     """Fonction qui permet d'afficher chaque module de façon individuelle avec la data de début et la date de fin
     
     PARAMÉTRES :
     groupsTrier => dataframe, contenant l'ensemble des cours du TD, TP et CM choisi 
     """

     #Exclure les lignes avec "Exam" dans la colonne "Summary"
     groupsTrier = groupsTrier[~groupsTrier['Summary'].str.contains('Exam')] #la méthode ".str.contains('Exam')" (s'implique sur un objet de type Series) renvoie une série de booléen qui indique si le mot présent entre parenthése est présent dans la sous-chaine ou non, le ~ permet d'inverser les booléen

     #Enregistrement dans une variable "moduleDateMin" l'ensemble des matières regroupé (plus aucun doublon) et agrégen la colonne "Date" avec les dates minimal
     moduleDateMin = groupsTrier.groupby('Summary').agg({'Date': 'min'}) #La méthode "groupby('Summary')" (s'implique sur un objet de type DataFrame) permet de réunir ensemble des valeurs de la colonne "Summary" ensemble pour avoir chaque valeur de façon unique; la méthode "agg({'Date': 'min'})" (s'implique sur un objet de type DataFrame) permet d'agréger une colonne en plus et utilisa la fonction 'min' pour prendre seulement les valueur les plus basses
     #Enregistrement dans une variable "moduleDateMax" l'ensemble des matières regroupé (plus aucun doublon) et agrégen la colonne "Date" avec les dates maximal
     moduleDateMax = groupsTrier.groupby('Summary').agg({'Date': 'max'})

     #on renome les colonnes "DtStart" et "DtFin"
     moduleDateMin.rename(columns = {'Date':'DtStart'}, inplace = True) #La méthode ".rename(columns = {'Date':'DtStart'}, inplace = True)" (s'implique sur un objet de type DataFrame) permet de rennomer une colonne 
     moduleDateMax.rename(columns = {'Date':'DtFin'}, inplace = True)
     
     # Fusionner les DataFrames pour créer toutModules
     toutModules = pd.merge(moduleDateMin, moduleDateMax[['DtFin']], left_index=True, right_index=True) #La méthode ".merge" (s'implique sur un objet de type DataFrame ou non) permet de fusionner deux dataframe ou colonne ensemble; left_index et right_index permet de faire la jointure entre les deux

     print(toutModules)

groups = demandeGroupes()
groupsTrier = groupeTaleau(groups)
modules(groupsTrier)

