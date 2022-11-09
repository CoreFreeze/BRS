import json

def loadCaster():
    file = open('settings.json', encoding='UTF8')
    data = json.load(file)

    retData = []
    casterList = []
    if "caster" in data:
        for caster in data["caster"]:
            casterList.append(caster)
        retData.append(casterList)
    if "portInfo" in data:
        retData.append(data["portInfo"])
    if "position" in data:
        retData.append(data["position"])
    if "locationList" in data:
        locationList = []
        for location in data["locationList"]:
            locationList.append(location)
        retData.append(locationList)

    return retData

def loadSettings():
    file = open('ChatSettings.json', encoding='UTF8')
    data = json.load(file)
    
    retData = []
    if 'ip' in data:
        retData.append(data["ip"])
    if 'port' in data:
        retData.append(data["port"])
    if 'location' in data:
        retData.append(data["location"])
    if 'locationList' in data:
        locationList = []
        for location in data['locationList']:
            locationList.append(location)
        retData.append(locationList)
    return retData

def saveSettings(ip, port, location, locationList):
    data = {}
    data['ip'] = ip
    data['port'] = int(port)
    data['location'] = location
    data['locationList'] = locationList
    with open('ChatSettings.json', 'w', encoding='UTF8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

def saveCaster(casterList, portInfo, position, locationList):
    data = {}

    data['caster'] = casterList
    data['portInfo'] = int(portInfo)
    data['position'] = position
    data['locationList'] = locationList

    with open('settings.json', 'w', encoding='UTF8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)