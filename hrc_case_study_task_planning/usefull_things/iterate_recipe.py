import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleziona il database "hrc_case_study"
db = client["hrc_case_study"]

# Seleziona la collezione "task_results_offline_real"
collection = db["real_test_results_test_finished"]


# Aggregazione
pipeline = [
    {
        "$group": {
            "_id": "$recipe",
            "n": {"$sum": 1}
        }
    }
]

result = collection.aggregate(pipeline)

for doc in result:
    if doc['n'] != 9:
        print(doc)



# Filtra e ordina i documenti
sorted_docs = sorted(result, key=lambda x: x.get('t_start', 0))  # Ordina per il campo "t_start"

RECIPES = ["BASIC_SOLVER", "RELAXED_HA_SOLVER","COMPLETE_SOLVER", "NOT_NEIGHBORING_TASKS"]
count = dict.fromkeys(RECIPES,0)
for doc in sorted_docs:
    recipe_name = [recipe for recipe in RECIPES if recipe in doc["_id"]]
    print(recipe_name)
    if len(recipe_name) != 1:
        print("Errore")
    count[recipe_name[0]] += 1
print(count)
