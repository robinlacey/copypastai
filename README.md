# CopyPastAI

## What is this?
Send text from your clipboard inside a predefined temaplte to ChatGTP and paste the reponse.

## Execution
Either: 
- set OPEN_API_KEY enviornment variable run `run.sh` 
- run `run.sh <OPEN_API_KEY>` 

## How to use
1. Copy text
2. Press the shortcut key linked to the template. One beep will sound.
3. Wait for two beeps
4. Paste response

The teplate numerical name (`0.json`, `1.json`) directly corresponds to the array position within `shortcuts.json`

### Templates
Inside the templates folder are a series of json templates. Each includes a `persona` and a `request` field. The following will be sent to GPT: 
```persona \n request \n CONTENTS OF CLIPBOARD```


### Shortcuts
Update shortcuts.json file with shortcuts for triggering. These are sent to python [keyboard](https://github.com/boppreh/keyboard) library. 
NOTE: Arm based Macbooks does not suport character keys. Hence why linked to F1-F9 keys by default.