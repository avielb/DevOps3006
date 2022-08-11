import ast
my_file = open("config.json")

a = "{'name': 'amatzia'}"
c = list(ast.literal_eval(my_file.read()))
if c["name"] == "aviel":
    print("i love devops experts")

with open("names.txt", "a+") as my_file:
    for name in my_file.readlines():
        print(name.strip())
