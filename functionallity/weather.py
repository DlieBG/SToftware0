from expr import BASE_URL


def hook():
    return ["wetter"]


def needsterm():
    return False


def getComponents(parts):
    ort = parts[0]
    return output(ort)


def output(ort):
    print("Wetter für "+ort+" ist nur Online verfügbar.")
    return "<meta http-equiv='refresh' content='0; URL="+BASE_URL+"/SToftware0/html/mobile/functions/weather.html?"+ort+"'>"
