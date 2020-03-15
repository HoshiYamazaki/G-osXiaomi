from argparse import ArgumentParser
from aiohttp import web, ClientSession

from json_utils import read_json_file

config = read_json_file('config.json')
parser = ArgumentParser()
parser.add_argument('--port')
parser.add_argument('--password', required=True)
args = parser.parse_args()


async def hello(request):
    """Return response and send message to discord."""
    if request.headers.get('pass', None) == args.password:
        async with ClientSession() as session:
            response = await session.post(config['webhook_uri'], json={
                'content': 'Xiaomi daje znak!',
            })
            if response and response.status in [200, 204]:
                return web.Response(text='GlosXiaomi SUCCESS.')
    return web.Response(text='GlosXiaomi FAILURE.')


async def post_info(request):
    """Return stupid message if somebody will call this port with post."""
    return web.Response(text='No voice of xiaomi here...')


app = web.Application()
app.add_routes([
    web.post('/', hello),
    web.get('/', post_info),
])
web.run_app(app, port=args.port)
