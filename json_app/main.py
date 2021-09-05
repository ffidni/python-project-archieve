import json

with open('json_app/data.json') as f:
    data = json.load(f)

def write():
    name = input("Input your name: ")
    password = input("Input a password: ")
    data[str(len(data)+1)] = {'name':name, 'password':password}
    with open('json_app/data.json', 'w') as f:
        json.dump(data, f)
    print("Your info has been added to the data!")
    choice = input("Read / Exit: ").lower()
    if choice == 'read':
        read()

def read():
    for items in data.items():
        print(f"ID: {items[0]}\nNAME: {items[1]['name']}\nPASSWORD: {'*'*len(items[1]['password'])}\n")
        
if __name__ == '__main__':
    x = input("Welcome to JSON Writer/Reader!\nRead / Write: ").lower()
    if x == 'read':
        read()
    else:
        write()
