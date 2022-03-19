''' The primary sms handler for the application '''
class SMSHandler():
    ''' An agnostic interface to multiple SMS providers '''
    def __init__(self, provider) -> None:
        import importlib
        provider_module = importlib.import_module(
            name=f'.providers.{provider}',
            package='sms'
        )
        self.client = provider_module.ProviderClient()

    def send_message(self, receiver, message) -> None:
        ''' Send an SMS message '''
        # TODO: remove debug code before commit
        #print(f'Message send activated for {receiver}')
        #print(f'Message: {message}')
        self.client.send_message(receiver, message)
        #print('Success???')
