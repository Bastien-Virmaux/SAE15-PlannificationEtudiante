import pandas as pd


def demandeGroupes():
     """Fonction qui demande à l'utilisateur sont groupe de TD et TP, retourne un tableau avec en premier index le TD et en deuxième index le TP.
     """

     td = input("Quel est votre groupe (1ATDA, 1ATDB, 1ATDC) ? ")
     tp = input("Quel est votre groupe (1ATP1, 1ATP2, 1ATP3, 1ATP4, 1ATP5) ? ")
     groups = []
     
     groupeTD = ""
     groupeTP = ""
     

     #formatage des groupe de TD et TP saisie par l'utilisateur et gestion des erreur
     if td == "1ATDA": #SI le groupe de TD est le TDA
          if tp == "1ATP1" or tp == "1ATP2": #SI le groupe de TP est le TP1 ou TP2
               groupeTD = " 1ATDA " #on affecte à la variable "groupeTD" le formatage de "1ATDA"
               if tp == "1ATP1": #SI le groupe de TP est le TP1
                    groupeTP = " 1ATP1 "
               else: #SINON le groupe de TP est le TP2
                    groupeTP = " 1ATP2 "
               
               groups.append(groupeTD) #ajouts du groupe de TD après formatage dans le tableau "groups"
               groups.append(groupeTP) #ajouts du groupe de TP après formatage dans le tableau "groups"
          else: #SINON le groupe de TP n'est pas le 1 ou 2 alors erreur de TD
               print("Erreur de saisie, veuillez taper un groupe valide ou faire correspondre le groupe de TD au groupe de TP (Ex : 1ATDA/1ATP1 ou 1ATDA/1ATP2)")
     elif td == "1ATDB": #SI le groupe de TD est le TDB
          if tp == "1ATP3" or tp == "1ATP4": #SI le groupe de TP est le TP3 ou TP4
               groupeTD = " 1ATDB " #on affecte à la variable "groupeTD" le formatage de "1ATDB"
               if tp == "1ATP3": #SI le groupe de TP est le TP3    
                    groupeTP = " 1ATP3 "
               else:  #SINON le groupe de TP est le TP4
                    groupeTP = " 1ATP4 "
                    
               groups.append(groupeTD) #ajouts du groupe de TD après formatage dans le tableau "groups"
               groups.append(groupeTP) #ajouts du groupe de TP après formatage dans le tableau "groups"
          else: #SINON le groupe de TP n'est pas le 3 ou 4 alors erreur de TD
               print("Erreur de saisie, veuillez taper un groupe valide ou faire correspondre le groupe de TD au groupe de TP (Ex : 1ATDB/1ATP3 ou 1ATDB/1ATP4)")
     elif td == "1ATDC": #SI le groupe de TD est le TDC
          if tp == "1ATP5": #SI le groupe de TP est le TP5
               groupeTD = " 1ATDC " #on affecte à la variable "groupeTD" le formatage de "1ATDC"
               groupeTP = " 1ATP5 " #SI le groupe de TP est le TP5
               
               groups.append(groupeTD) #ajouts du groupe de TD après formatage dans le tableau "groups"
               groups.append(groupeTP) #ajouts du groupe de TP après formatage dans le tableau "groups"
          else: #SINON le groupe de TP n'est pas le 5 alors erreur de TD
               print("Erreur de saisie, veuillez taper un groupe valide ou faire correspondre le groupe de TD au groupe de TP (Ex : 1ATDC/1ATP5)")     

     if len(groups) == 2: #SI la logueur du tableau vaut 2 
          return groups

def groupeTaleau(groups):
     """Fonction qui permet de crée un nouveau dataframe et le retourne avec seulement les cour d'un TD, TP, CM
     
     PARAMÉTRES : 
     groups => array, contient le groupe de TD à l'index 0 et le groupe de TP à l'index 1
     """     

     #Enregistrement dans une variable "data" des données du fichier ADECAL_officiel.csv au format pandas.core.frame.DataFrame
     data = pd.DataFrame(pd.read_csv("ADECAL_officiel.csv"))

     #Enregistrement dans une variable "dataTD" de l'ensemble des cours ayant comme groupe le td choisi par l'utilisateur
     td = "TDC"
     dataTD = data.query("Type == @td") #la méthode ".query" (s'implique sur un objet de type dataframe) permet de selectionner toutes les lignes d'un dataframe respectant la condition entre guillement (@ => référence à une variable)
     #Enregistrement dans une variable "dataTP" de l'ensemble des cours ayant comme groupe le tp choisi par l'utilisateur
     tp = "TP5"
     dataTP = data.query("Type == @tp")
     #Enregistrement dans une variable "dataCM" de l'ensemble des cours en CM (commun à tout TD ou TP)
     cm = "Cours"
     dataCM = data.query("Type == @cm")
     
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
if groups: #SI groups existe et n'est pas vide
     groupsTrier = groupeTaleau(groups)
     modules(groupsTrier)
