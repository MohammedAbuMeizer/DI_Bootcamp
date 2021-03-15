from faker import Faker

users = []
fake = Faker(['en_US','ja_JP'])

for _ in range(1):
    dic = {"name":fake.name()
          ,"address":fake.address()
          ,"language_code":fake.language_code()
           }
    users.append(dic)

    print(users)