def hook():
    return ["kamel"]


def needsterm():
    return False


def getComponents(ignore):
    return output()


def output():
    print("Kamelrechner ist nur Online verfügbar!")
    return "<meta http-equiv='refresh' content='0; URL=https://benedikt-schwering.de/SToftware0/html/mobile/functions/kamel.html'>"
