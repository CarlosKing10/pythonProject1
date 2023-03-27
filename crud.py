import json

from stream_conection import collection


def read_books(id=None):
    if id is not None:
        query = {"id": id}
        document = collection.find_one(query)
        print(json.dump(document))
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def create_books(book):
    result = collection.insert_one(book)
    print(result.inserted_id)


def update_books(code, json_indices_values):
    query = {"code": code}
    new_values = {"$set": json_indices_values}
    result = collection.update_one(query, new_values)
    print(result.modified_count)


def delete_books(book):
    result = collection.delete_one(book)
    print(result.deleted_count)



