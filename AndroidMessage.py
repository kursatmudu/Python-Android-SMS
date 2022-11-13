import time, re, os

SMS_FILTER = "" # sms filter by sms name

try:
    import androidhelper
except ImportError:
    import android as androidhelper
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
    
sms_list = []
droid = androidhelper.Android()

###################################### FIRST RUN ONLY ##################################################### 

def FirstRun():
    received_id = droid.smsGetMessageIds(True, "inbox") # getting sms id by android sms DB true represents unread messages, false represents read messages
    for _id in received_id[1]:
        sms = droid.smsGetMessageById(_id, ["address", "body"]) # getting android sms by sms id
        sms_address = sms[1]["address"] # shows who the sms is from
        sms_body = sms[1]["body"] # shows the content of the sms
        if sms_address == SMS_FILTER: # sms sender filter by sms name or phone number
            code = re.compile(r"(.\d*).(Para)").findall(sms_body) # filters if there is a password in the sms. Detail: https://pynative.com/python-regex-compile/
            if code:
                OTP_code, _ = code[0]
                sms_list.append(OTP_code)

################################## SAME CODE FOR WHILE LOOP ###########################################                

def GetMessage(session):
    received_id = droid.smsGetMessageIds(True, "inbox")
    for _id in received_id[1]:
        sms = droid.smsGetMessageById(_id, ["address", "body"])
        sms_address = sms[1]["address"]
        sms_body = sms[1]["body"]
        if sms_address == SMS_FILTER: # sms sender filter by sms name or phone number
            card_add_code = re.compile(r"(\d*).(dogrulama)").findall(sms_body) # filters if there is a password in the sms. Detail: https://pynative.com/python-regex-compile/
            purchase_code = re.compile(r"(\d*).(sifresi)").findall(sms_body) # filters if there is a password in the sms. Detail: https://pynative.com/python-regex-compile/
            if card_add_code:
                OTP_code, _ = card_add_code[0]
                if OTP_code not in sms_list:
                    sms_list.append(OTP_code)
                    AddSMS(session, OTP_code)
            if purchase_code:
                OTP_code, _ = purchase_code[0]
                if OTP_code not in sms_list:
                    sms_list.append(OTP_code)
                    AddSMS(session, OTP_code)

#################################### SEND THE MESSAGE TO THE SERVER #####################################             

def AddSMS(session, sms_code):
    sms_params = {"sms_code": sms_code}
    return session.post("YOUR SERVER ADDRESS", params = sms_params)

################################## FETCH THE MESSAGE TO THE SERVER ######################################

def GetSMS(session):
    return session.get("YOUR SERVER ADDRESS").json()

sms_session = requests.Session()
