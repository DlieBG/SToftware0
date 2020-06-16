from expr import BASE_URL


def hook():
    return ["kamel"]


def needsterm():
    return False


def getComponents(ignore):
    return output()


def output():
    print("Kamelrechner ist nur Online verfügbar!")
    return str("<meta http-equiv='refresh' content='0; URL='"+BASE_URL+"/SToftware0/html/mobile/functions/kamel.html'>")
