import pyperclip
import keyboard
import os
import json
import openai
import sys
from sys import argv

def load_template(key):
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"templates/{key}.json")
    print (f"templates/{key}.json")
    with open(json_path, 'r') as file:
        return json.load(file)

def get_reponse_from_gpt(key):
    sys.stdout.write('\a')
    clipboard = pyperclip.paste()
    template = load_template(key)
    system_message = f"{template['persona']}\n{template['request']}"
    response = openai.ChatCompletion.create(
              model="gpt-4",
              messages=[{"role": "system", "content": system_message},
                        {"role": "user", "content": clipboard}
              ])
    print(response["choices"][0]["message"]["content"])
    sys.stdout.write('\a\a')
    pyperclip.copy(response["choices"][0]["message"]["content"])

def init():
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"shortcuts/shortcuts.json")
    with open(json_path, 'r') as file:
        shortcuts = json.load(file)
        for i, shortcut in enumerate(shortcuts['shortcuts']):
            keyboard.add_hotkey(shortcut, lambda i=i: get_reponse_from_gpt(i))

if os.getenv('OPENAI_API_KEY') is None:
    if len(argv)<2 :
        print("OPENAI_API_KEY environment variable not set or OPENAI_API_KEY not passed as argument")
        sys.exit()
    else:
        print(f"Setting OPENAI_API_KEY to {argv[1]}")
        openai.api_key = argv[1]

init()
keyboard.wait('esc')
