import pandas as pd

def demandeGroupes():
     td = input("Quel est votre groupe (1ATDA, 1ATDB, 1ATDC) ? ")
     tp = input("Quel est votre groupe (1ATP1, 1ATP2, 1ATP3, 1ATP4, 1ATP5) ? ")
     groups = []
     
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

     # Regrouper par MATIERE et agréger les heures de début et de fin
     moduleDateMin = groupsTrier.groupby('Summary').agg({'Date': 'min'})
     moduleDateMax = groupsTrier.groupby('Summary').agg({'Date': 'min'})
     
     # Afficher le résultat
     print(moduleDateMin)
     print(moduleDateMax)

groups = demandeGroupes()
groupsTrier = groupeTaleau(groups)
modules(groupsTrier)

