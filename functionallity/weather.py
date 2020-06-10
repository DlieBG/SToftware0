def hook():
    return ["wetter"]


def getComponents(parts):
    ort = parts[0]
    return output(ort)


def output(ort):
    print("Wetter für "+ort+" ist nur Online verfügbar.")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/weather.html?"+ort+"'>"    
