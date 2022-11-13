from AndroidMessage import *

while True:
    fetching_sms = GetSMS(sms_session)
    print(fetching_sms)