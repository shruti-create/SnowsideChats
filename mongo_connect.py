import pymongo
from pymongo import MongoClient


try:
    # connecting
    uri = "mongodb+srv://JoshuaShruti:servicenow@clustersn0.aquderp.mongodb.net/"
    client = MongoClient(uri, server_api=pymongo.server_api.ServerApi(
        version="1", strict=True, deprecation_errors=True))
    client.admin.command("ping")
    print("Connected successfully")

    # inserting data
    database = client["user_data"]
    collection = database["content"]
    '''
    collection.insert_many([
            { "_id": 1, "user_name": "apples", "answers":"i like bananas"},
            { "_id": 2, "user_name": "apples2", "answers":"i like bananas2"},
            { "_id": 3, "user_name": "apples3", "answers":"i like bananas3"},       
        ])
    '''
    
    print("inserted successfully")
    
    # reading data
    results = collection.find({})
    for f in results: 
        print(f)

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)






