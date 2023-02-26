from twilio.rest import Client


def send_sms(message,to):
    account_sid = 'ACc2e4a5f544e1f712046ff18f0162b5d5'
    auth_token = '593f4e8326ad40ae67081d9ee2eb6b72'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12706791996',
    body=message,
    to='+91'+str(to)
    )
    print(message.sid,to)

    return message.sid