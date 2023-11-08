import pandas as pd
import pymongo

# Connessione al database MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleziona il database "hrc_case_study"
db = client["hrc_case_study"]

# Seleziona la collezione "task_results_offline_real"
collection = db["real_test_results_test_finished"]

# Eseguire l'aggregazione
pipeline = [
    {
        '$group': {
            '_id': '$recipe',
            'tot': {'$sum': 1}
        }
    }
]

result = list(collection.aggregate(pipeline))


# Carica il file CSV in un DataFrame
csv_file_path1 = '/home/galois/projects/cells_ws/src/hrc_case_study_cell/hrc_case_study/hrc_case_study_task_planning/statistics/distance_monitoring_real_test_distance_results (copy).csv'  # Sostituire con il percorso del file CSV
csv_file_path2 = '/home/galois/projects/cells_ws/src/hrc_case_study_cell/hrc_case_study/hrc_case_study_task_planning/statistics/distance_monitoring_real_test_distance_results_last (copy).csv'  # Sostituire con il percorso del file CSV

df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)
# Crea un nuovo DataFrame per le righe corrispondenti

print(len(df1))
len_num = [len(r["_id"][-5:].split("_")[1]) for r in result]
print(len_num)
res_new = []
for id,r in enumerate(result):
    print(r)
    res_new.append(r["_id"][:-len_num[id]-1])
result = res_new
new_df1 = df1[df1['Recipe'].isin([r for r in result])]
print(len(new_df1))
# print(df1['Recipe'].isin([r['_id'][:-2] for r in result]))
new_df2 = df2[df2['Recipe'].isin([r for r in result])]

new_df = pd.concat([new_df1, new_df2])
for recipe in result:
    print(recipe)
    print(recipe in new_df['Recipe'].values)
    print(recipe in df1['Recipe'])
    print(recipe in df2['Recipe'])
    print("---------------")
    if recipe not in new_df['Recipe'].values:
        print("male")
        print(recipe)
        input()

        # if recipe == "_":
        #     print(recipe['_id'][:-3])
        #     if recipe['_id'][:-3] not in new_df['Recipe'].values:
        #         print("male")
        #         input()
# print([(recipe, recipe['_id'][:-2] in new_df['Recipe'].values) for recipe in result])
# print(len(new_df))
# Salva il nuovo DataFrame in un nuovo file CSV
new_csv_file_path = '/home/galois/projects/cells_ws/src/hrc_case_study_cell/hrc_case_study/hrc_case_study_task_planning/statistics/distanze_filtrate.csv'  # Sostituire con il percorso del nuovo file CSV
new_df.to_csv(new_csv_file_path, index=True)

# Chiudi la connessione al database MongoDB
client.close()
