from person_pb2 import Person

person = Person()
print('before', person)
person.ParseFromString(b'\n\x04Jhon\x10\xd2\t\x1a\x10jhon@example.com')
print('after', person)
