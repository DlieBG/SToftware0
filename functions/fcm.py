from sympy import *
from pyfcm import FCMNotification

def hook(keyinput):
    #Keywords definieren
    if True:
        return getComponents(keyinput)
    return ""

def getComponents(keyinput):

    if  True: #Abbruchbedingung
        return send(keyinput)
    else:
        print("Fehler")
        return "Fehler"

def send(keyinput):
    
    push_service = FCMNotification(api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")

    registration_ids = [
        "czKru1lRZX4:APA91bE3VVc_iwDxTaYVtHljlA1OQebkZHyCGhKjwb-n9AeNwXGwMQOd71kHmwK20hFB5fDQCSfSRc-piirHH-swvYSrcURiMmLLXMq3EC3TSGW6cSstqPqpeNVKSi3hwOsQwGmN1SsM",
        #"fg09UzZglnc:APA91bHThBBv5LA-VmM3xrU1NkfCMqyZ5cR9_50PoiG_MNXpmJdoQ2XhX2s9hiFFQZnHirwLq032YH0HaTy_EBBX7YfKwiUr1disox8had4zU9Lo1DO9KP1PiExiYP9cMCd6LSNLdmP9"
                        ]
    message_title = "SToftware0 Call"
    message_body = keyinput
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    return ""
