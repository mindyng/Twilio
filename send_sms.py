from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

tClient= Client(account_sid, auth_token)

my_msg = ''.join(['silly Mindy\n' for i in range(5)])

message = tClient.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
