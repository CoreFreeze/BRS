import json

def loadCaster():
    file = open('settings.json', encoding='UTF8')
    data = json.load(file)

    casterList = []
    if "caster" in data:
        for caster in data["caster"]:
            casterList.append(caster)

    return casterList

def loadSettings():
    file = open('ChatSettings.json', encoding='UTF8')
    data = json.load(file)
    
    retData = []
    if 'ip' in data:
        retData.append(data["ip"])
    if 'location' in data:
        retData.append(data["location"])
    return retData

def saveSettings(ip, location):
    data = {}
    data['ip'] = ip
    data['location'] = location
    with open('ChatSettings.json', 'w', encoding='UTF8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def saveCaster(casterList):
    data = {}

    data['caster'] = casterList

    with open('settings.json', 'w', encoding='UTF8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)