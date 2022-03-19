# notifierr
notifierr is an SMS notification service used in conjunction with Radarr/Sonarr to send SMS notifications when movies and TV shows are available to watch.

## Installation
The easiest way to install notifierr is with pip
```sh
python3 -m pip install notifierr
```

You can also clone the repository directly and run setup.py manually
```sh
git clone https://github.com/adamsbytes/notifierr.git
cd notifierr
python3 setup.py install
```

## Usage

### Configuring the Server
You must edit `notifierr/config.py` with your own values before starting the API server. You'll also need to set some environment variables, depending on which SMS provider you're using.

#### *Twilio SMS provider*
The following environment variables are required:

`TWILIO_ACCOUNT_SID`: Twilio account SID

`TWILIO_AUTH_TOKEN`: Twilio auth token

`TWILIO_FROM_NUMBER`: the Twilio phone number you want to send messages from


### Starting the Server
For pip installs:
```sh
notifierr --host 0.0.0.0 --port 8181
```

For manual installs:
```sh
$appdir/cli.py --host 0.0.0.0 --port 8181
```