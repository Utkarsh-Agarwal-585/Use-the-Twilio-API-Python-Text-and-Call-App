
import os
from twilio.rest import Client



# Your Account SID from twilio.com/console
account_sid = "your account_sid "
# Your Auth Token from twilio.com/console
auth_token  = "your auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='my cell number', 
                        from_='twilo number'
                    )

print(call.sid)
