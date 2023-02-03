people = [
    {"name": "carla", "house": "prebo"},
    {"name": "rodolfo", "house": "trigal"},
    {"name": "victoria", "house": "jessie"},
]

# long way to write a one line function instead we can use a lambda function. check lambda funtion below
# def f(person):
#     return person["house"]


# telling to sort all the people by the key name given at the function f defined above which is returning person name
# using long way of function on line 8
# people.sort(key=f)
# print(people)

# using lambda function
people.sort(key=lambda person: person['name'])
print(people)
