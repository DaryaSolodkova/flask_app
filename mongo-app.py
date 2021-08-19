import pymongo

client = pymongo.MongoClient('localhost', 27017)

# database = client['users'] #создание базы данных
database = client.users #создание базы данных

# collection = client['users'] #создание коллекции
collection = database.users #создание коллекции

user = {
    'name': 'some_name',
    'age': 40
}

#collection.insert_one(user)

#result = collection.insert_one(user) #работа с самими документами
#print(result.inserted_id)

result = collection.find(user) #возвращаем курсор(указатель на какой-то элемент в текущей последовательности)
print(result)

for i in result: #получаем всё, что в result
    print(i)