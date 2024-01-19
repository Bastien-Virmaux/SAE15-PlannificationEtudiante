import pandas as pd

def demandeGroupes():
     td = input("Quel est votre groupe (1ATDA, 1ATDB, 1ATDC) ? ")
     tp = input("Quel est votre groupe (1ATP1, 1ATP2, 1ATP3, 1ATP4, 1ATP5) ? ")
     groups = []
     
     while td == "1ATDA" and td == "1ATDB" and td == "1ATDC":
          td = input("Erreur, veuillez saisir un groupe valide (1ATDA, 1ATDB, 1ATDC) ? ")


     while tp == "1ATP1" and tp == "1ATP2" and tp == "1ATP3" and tp == "1ATP4" and tp == "1ATP5":
          td = input("Erreur, veuillez saisir un groupe valide (1ATDA, 1ATDB, 1ATDC) ? ")

     groupeTD = ""
     if td == "1ATDA":
          groupeTD = " 1ATDA "
     elif td == "1ATDB":
          groupeTD = " 1ATDB "
     else:
          groupeTD = " 1ATDC "

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
     
     groups.append(groupeTD)
     groups.append(groupeTP)
     return groups

def groupeTaleau(groups):
     data = pd.DataFrame(pd.read_csv("ADECAL_officiel.csv"))

     td = groups[0]
     dataTD = data.query("Groupe == @td")
     tp = groups[1]
     dataTP = data.query("Groupe == @tp")
     
     courGroup = []
     
     for lineTD in range(len(dataTD)):
          courGroup.append(dataTD.iloc[lineTD, :])
          
     for lineTP in range(len(dataTP)):
          courGroup.append(dataTP.iloc[lineTP, :])
          
     return pd.DataFrame(courGroup)

def modules(groupsTrier):

     # Exclure les lignes avec "Exam" dans la colonne sumary
     groupsTrier = groupsTrier[~groupsTrier['Summary'].str.contains('Exam')]

     # Regrouper par MATIERE et agréger les heures de début et de fin
     moduleDateMin = groupsTrier.groupby('Summary').agg({'Date': 'min'})
     moduleDateMax = groupsTrier.groupby('Summary').agg({'Date': 'max'})

     moduleDateMin.rename(columns = {'Date':'DtStart'}, inplace = True)
     moduleDateMax.rename(columns = {'Date':'DtFin'}, inplace = True)
     
     # Fusionner les DataFrames pour créer toutModules
     toutModules = pd.merge(moduleDateMin, moduleDateMax[['DtFin']], left_index=True, right_index=True)

     # Afficher le résultat
     print(toutModules)

groups = demandeGroupes()
groupsTrier = groupeTaleau(groups)
modules(groupsTrier)

