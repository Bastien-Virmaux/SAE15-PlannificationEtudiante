import pandas as pd

# Créer un DataFrame avec vos données
data = {'MATIERE': ['cour1', 'cour2', 'cour1', 'cour2'],
        'HEURE DEBUT': ['1h', '2h', '2h', '5h'],
        'HEURE FIN': ['2h', '3h', '3h', '6h']}
df = pd.DataFrame(data)

# Convertir les colonnes HEURE DEBUT et HEURE FIN en datetime pour faciliter la manipulation
df['HEURE DEBUT'] = pd.to_datetime(df['HEURE DEBUT'], format='%Hh')
df['HEURE FIN'] = pd.to_datetime(df['HEURE FIN'], format='%Hh')

# Regrouper par MATIERE et agréger les heures de début et de fin
result_df = df.groupby('MATIERE').agg({'HEURE DEBUT': 'min', 'HEURE FIN': 'max'}).reset_index()

# Convertir les colonnes HEURE DEBUT et HEURE FIN en format d'heure
result_df['HEURE DEBUT'] = result_df['HEURE DEBUT'].dt.strftime('%Hh')
result_df['HEURE FIN'] = result_df['HEURE FIN'].dt.strftime('%Hh')

# Afficher le résultat
print(result_df)