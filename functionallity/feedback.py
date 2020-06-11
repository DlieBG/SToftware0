def hook():
    return ["feedback", "bewertung", "rezension", "fehler"]

def needsterm():
    return False

def getComponents(ignore):
    output()


def output():
    print("Bewertung ist nur Online verfügbar!\nWenn Sie so krass sind, dass sie die Kommandozeilenfunktion nutzen, können Sie uns Ihre Ideen einfach auf GitHub mitteilen!")
    return "<meta http-equiv='refresh' content='0; URL=http://benedikt-schwering.de/SToftware0/python/SToftware0/html/mobile/functions/bewertung.php'>"
