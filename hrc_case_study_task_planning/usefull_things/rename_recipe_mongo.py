import pymongo

# Connetti al server MongoDB in locale
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleziona il database "hrc_case_study"
db = client["hrc_case_study"]

# Seleziona la collezione "task_results_offline_real"
collection = db["merging"]

# Recupera tutti i documenti dalla collezione
documents = collection.find()

# Itera su tutti i documenti
for document in documents:
    if document["name"] == "go_home" or document["name"] == "end":
        collection.delete_one({"_id": document["_id"]})
        print(f"Documento eliminato con ID: {document['_id']}")

        continue
    continue
    # Estrai l'attributo "recipe" dal documento
    # recipe = document["recipe"]
    #
    # # Dividi la stringa utilizzando "rec_num_" come delimitatore
    # parts = recipe.split("BASIC_SOLVER_rec_")[1].split("_rep")[0]
    # # Verifica se la stringa è stata divisa correttamente
    # if len(parts) == 2 or len(parts)==1:
    #     # Estrai il numero dopo "rec_num_"
    #     num_part = parts
    #
    #     # Costruisci la nuova ricetta
    #     # new_recipe = f"{parts[0]}rec_num_2023_10_06_14:48_0_{num_part}"
    #     new_recipe = f"BASIC_SOLVER_rec_{num_part}_rep_0_2023_10_06_14:48_{num_part}"
    #     print(new_recipe)
    #     # Aggiorna il documento nel database con la nuova ricetta
    #     collection.update_one({"_id": document["_id"]}, {"$set": {"recipe": new_recipe}})
    #
    #     print(f"Documento aggiornato con ID: {document['_id']}")
    # else:
    #     print(f"La stringa non contiene 'rec_num_': {recipe}\n")
