# python3


import random
class Phonebook():

    def __init__(self, m):
        self.m = m
        self.array = ['not found' for x in range(m)]
        
    #     # hash info
    #     self.p = 10888869450418352160768000001 # prime number used for hashing
    #     random.seed(0)
    #     self.a = random.randint(1, self.p-1)
    #     self.b = random.randint(0, self.p-1)

    # def hash(self, phone_number):
    #     return ((self.a * phone_number + self.b) % self.p) % self.m
    
    def add(self, phone_number, name):
        self.array[phone_number] = name

    
    def find(self, phone_number):
        return self.array[phone_number]
    
    def delete(self, phone_number):
        self.array[phone_number] = "not found"


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phone_book = Phonebook(10**7)
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            phone_book.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            phone_book.delete(cur_query.number)
        else:
            response = phone_book.find(cur_query.number)
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

