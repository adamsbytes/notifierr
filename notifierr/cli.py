''' A cli interface to startup the server '''
import argparse
import sys

from .core import app
from .version import __version__

def main():
    ''' Provides an entrypoint into the app via CLI '''
    parser = argparse.ArgumentParser(
        description="notifierr API server CLI"
    )

    parser.add_argument(
        '--host',
        default='localhost',
        type=str,
        help='The host the server will use. The default is: %(default)s'
    )

    parser.add_argument(
        '--port',
        default=8181,
        type=int,
        help='The port the server will use. The default is: %(default)s'
    )

    parser.add_argument(
        '--version',
        action='store_true',
        help='Print the version of the notiferr server'
    )

    args = parser.parse_args()

    if args.version:
        print(__version__)
        sys.exit()

    app.run(
        host=args.host,
        port=args.port,
    )

if __name__ == '__main__':
    main()
