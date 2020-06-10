from sympy import *
from pyfcm import FCMNotification


def hook():
    return []


def getComponents(keyinput):
    return send(keyinput)


def send(keyinput):
    
    push_service = FCMNotification(api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")

    registration_ids = [
        "dSvcsDop4ek:APA91bFcfxJak8NLbyxjpXavu3RLbf28jNLRRcAcTTN7_dzg-MS8rzN3uRsPvMgpmPNvpJCaRIFMOliUDX169uf3cH2V7isYYMa0F6Hn5VZRunVhz_ZJBUot5m9V2HotGtbBxtAULUvM",
        #"fg09UzZglnc:APA91bHThBBv5LA-VmM3xrU1NkfCMqyZ5cR9_50PoiG_MNXpmJdoQ2XhX2s9hiFFQZnHirwLq032YH0HaTy_EBBX7YfKwiUr1disox8had4zU9Lo1DO9KP1PiExiYP9cMCd6LSNLdmP9"
                        ]
    message_title = "SToftware0 Call"
    message_body = keyinput
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

    return ""
