''' The primary application file '''
import json
import os

from flask import (
    Flask,
    Blueprint,
    abort,
    current_app,
    make_response,
    request
)
from . import strings
from .sms import handler
from .version import __version__

api = Blueprint('api', __name__)
app = Flask('notifierr')
app.config.from_pyfile(os.getenv('NOTIFIERR_CONFIG_FILEPATH', 'config.py'))
smshandler = handler.SMSHandler(provider=str(app.config['SMS_PROVIDER']).lower())
logger = app.logger

@api.before_request
def block_on_user_agent():
    ''' Block requests with a user agent string matching one in FORBIDDEN_USER_AGENTS'''
    user_agent = request.user_agent.string
    forbidden_uas = current_app.config.get('FORBIDDEN_USER_AGENTS', [])
    if user_agent in forbidden_uas:
        abort(429)

@api.route('/version')
def get_version():
    ''' Responds to GET /version with the application __version__ '''
    response = make_response(
        f'notifierr {__version__}',
        200
    )
    return response

@api.route(
    '/message/movie/<uid>',
    methods=['POST']
)
def send_movie_message(uid):
    ''' Responds to POST /message/movie/{uid} by sending an SMS to the associated number'''
    try:
        server_name = app.config['MEDIA_SERVER_NAME']
        requestdata = json.loads(request.data)
        moviedata = requestdata['movie']
        movie_name = moviedata['title']
        movie_year = str(moviedata['year'])
        smsmessage = strings.MSGTEMPL_MOVIE_READY.format(
            movie_name=movie_name,
            movie_year=movie_year,
            server_name=server_name
        )
        for number in app.config['CONTACTS'][uid]:
            smshandler.send_message(
                receiver=number,
                message=smsmessage
            )
    except Exception as err:
        result = make_response(
            f'Failure: {str(err)}',
            400
        )
    else:
        result = make_response(
            'Success!',
            200
        )
    finally:
        return result

@api.route(
    '/message/tv/<uid>',
    methods=['POST']
)
def send_tv_message(uid):
    ''' Responds to POST /message/tv/{uid} by sending an SMS to the associated number'''
    try:
        requestdata = json.loads(request.data)
        show_name = requestdata['series']['title']
        server_name = app.config['MEDIA_SERVER_NAME']
        if len(requestdata['episodes']) == 1: # single episode
            episode_num = str(requestdata['episodes'][0]['episodeNumber'])
            episode_title = requestdata['episodes'][0]['title']
            season_num = str(requestdata['episodes'][0]['seasonNumber'])
            smsmessage = strings.MSGTEMPL_TV_SHOW_READY.format(
                tv_show_name=show_name,
                season_number=season_num,
                episode_number=episode_num,
                episode_title=episode_title,
                server_name=server_name
            )
        elif len(requestdata['episodes']) > 1: # multi episode
            requestepisodes = []
            for episode in requestdata['episodes']:
                episodestr = f"S{str(episode['seasonNumber'])}E{str(episode['episodeNumber'])}"
                requestepisodes.append(episodestr)
            smsmessage = strings.MSGTEMPL_TV_SHOW_MULTI_READY.format(
                episode_list=', '.join(requestepisodes),
                tv_show_name=show_name,
                server_name=server_name
            )
        else:
            raise ValueError
        for number in app.config['CONTACTS'][uid]:
            smshandler.send_message(
                receiver=number,
                message=smsmessage
            )
    except Exception as err:
        result = make_response(
            f'Failure: {str(err)}',
            400
        )
    else:
        result = make_response(
            'Success!',
            200
        )
    finally:
        return result

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8282',
        debug=True
    )
