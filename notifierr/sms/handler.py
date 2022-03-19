''' The primary sms handler for the application '''
import importlib

class SMSHandler():
    ''' An agnostic interface to multiple SMS providers '''
    def __init__(self, provider) -> None:
        provider_module = importlib.import_module(
            name=f'.providers.{provider}',
            package='sms'
        )
        self.client = provider_module.ProviderClient()

    def send_message(self, receiver, message) -> None:
        ''' Send an SMS message '''
        self.client.send_message(receiver, message)
