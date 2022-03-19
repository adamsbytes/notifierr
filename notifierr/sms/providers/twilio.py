''' The provider client for Twilio '''
from os import environ as env
from twilio.rest import Client

class ProviderClient():
    ''' A client to send messages via the Twilio interface '''
    def __init__(self) -> None:
        self.client = Client(
            env['TWILIO_ACCOUNT_SID'],
            env['TWILIO_AUTH_TOKEN']
        )
        self.from_number = env['TWILIO_FROM_NUMBER']

    def send_message(self, receiver, message) -> dict:
        ''' Sends a SMS message via the Twilio client '''
        sent_message = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=receiver
        )
        assert sent_message.error_code is None # TODO: validate
        return {'provider_message_confirmation_token': sent_message.sid}
