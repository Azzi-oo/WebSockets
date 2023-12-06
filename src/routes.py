from starlette.routing import Route, Mount, WebSocketRoute
from .endpoints import Homepage
from starlette.staticfiles import StaticFiles
from .ws import WSGame


routes = [
    Route('/', Homepage),
    WebSocketRoute('/ws', WSGame),
    Mount('/static', app=StaticFiles(directory='static'))
]
