from AndroidMessage import *

FirstRun() # It is used to not resend incoming sms.
while True:
    GetMessage(sms_session) # automatically sends the message to the server. there is no return
    time.sleep(2) # waits for 2 seconds to keep the server busy