import redis #импортируем паркет и устанавливаем его через pip install redis


#1)
client = redis.Redis(host="localhost", port="6379", db=0) # создаём объект(наш комп - локал, порт, на котором раб рэдис и БД(от 0 до 16)
# client_1 = redis.Redis(host="localhost", port="6379", db=1)  создаём ещё одного клиента и работаем с ним в БД 1, если надо
client.set("new-key", 123) # передаём ключ-значение

print(client.get("new-key")) #возвращаем

#2)
#some_dict = {    #сохранить словарь в рэдисе
#        'a': 1,
#        'b': 2
#}

#client.hmset('my_dict', some_dict) #сохраняется в хэш

print(client.hgetall('my_dict')) #получить словарь назад

#3)
some_list = [1, 2, 3]

client.lset('key', some_list)