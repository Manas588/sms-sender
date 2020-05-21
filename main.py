# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC2817dce9debc0797241dd726651f75e5'
auth_token = '17a7324036f9c49142bf2cf6d12a6a3a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12034578103',
                     to='+919819971211'
                 )

print(message.sid)
