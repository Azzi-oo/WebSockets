from starlette.websockets import WebSocket


class Player:
    def __init__(self, ws: WebSocket, state: str = 'x') -> None:
        self.__ws = ws
        self.__state = state

    async def get_state(self):
        return self.__state


class Game:
    players = []
    current_player = ''
    active_game = False

    async def create(self, ws: WebSocket):
        player = await self.create_player(ws)
        self.players.append(player)
        self.current_player = await player.get_state()

    async def create_player(self, ws: WebSocket):
        return Player(ws, 'x')
