import keyboard
import json

print("Thanks for downloading my ha-- I mean lovely program!")

'''
    Documentation:
        Inside the key_remaps.json file is a list called "key_remaps". The values inside define which keys are remapped. Add nested tables such that the first value
        is a key, and the second is the value it gets assigned to. Ex: ['w', 'a']  will make it so that pressing 'w' is read as 'a'.
'''


def remap_keys():
    with open('key_remaps.json', 'r') as file:
        data = json.load(file)
        for v in data['key_remaps']:
            keyboard.remap_key(v[0], v[1])

remap_keys()

#Keeping the script running
while True:
    keyboard.wait()