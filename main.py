import os
import sys
import json
from sys import argv
import platform

import pyperclip
import keyboard
import openai

def beep():
    print (chr(7))

def load_template(key):
    print(f"Loading template with key: {key}")
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", f"{key}.json")
    with open(json_path, 'r') as file:
        return json.load(file)

def get_response_from_gpt(key):
    print("Getting response from GPT...")
    beep()
    clipboard = pyperclip.paste()
    template = load_template(key)
    system_message = f"{template['persona']}\n{template['request']}"
    response = openai.ChatCompletion.create(
              model="gpt-4",
              messages=[{"role": "system", "content": system_message},
                        {"role": "user", "content": clipboard}
              ])
    print(f"Received response: {response['choices'][0]['message']['content']}")
    beep()
    beep()
    pyperclip.copy(response["choices"][0]["message"]["content"])

def add_hotkey(i, shortcut):
    print(f"Adding hotkey for shortcut {shortcut}")
    keyboard.add_hotkey(shortcut, lambda: get_response_from_gpt(i))

def init():
    print("Initializing shortcuts...")
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shortcuts", "shortcuts.json")
    with open(json_path, 'r') as file:
        shortcuts = json.load(file)
        for i, shortcut in enumerate(shortcuts['shortcuts']):
            add_hotkey(i, shortcut)

def check_api_key():
    print("Checking OpenAI API Key...")
    try:
        openai.api_key = os.environ['OPENAI_API_KEY']
    except KeyError:
        if len(argv) < 2:
            print("OPENAI_API_KEY environment variable not set or OPENAI_API_KEY not passed as an argument")
            sys.exit()
        else:
            print(f"Setting OPENAI_API_KEY to {argv[1]}")
            openai.api_key = argv[1]


check_api_key()
init()
keyboard.wait('esc')

