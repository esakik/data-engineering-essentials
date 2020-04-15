from person_pb2 import Person

person = Person()
person.id = 1234
person.name = "Jhon"
person.email = "jhon@example.com"
print(person.SerializeToString())
