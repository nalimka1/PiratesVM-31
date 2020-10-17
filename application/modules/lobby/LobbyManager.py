from application.modules.BaseManager import BaseManager


class LobbyManager(BaseManager):
    def __init__(self, mediator, sio, MESSAGES):
        super().__init__(
            mediator=mediator,
            sio=sio,
            MESSAGES=MESSAGES
        )

        # __teams = {
        #             'teamId': [user1, user2, ...],
        #             'teamId': [user1, user2, ...]
        #         }
        # teamId == creatorToken
        # user = {
        #   token: '',
        #   sio: '',
        #   readyToStart: False
        # }

        self.__teams = {}

        self.sio.on(self.MESSAGES['READY_TO_START'], self.readyToStart)

    async def readyToStart(self, sid, data):
        user, teamId = self.__findUserInTeams(data['token'])
        if user:
            user['readyToStart'] = True
        if teamId and self.__checkTeamIsReady(teamId):
            for user in self.__teams[teamId]:
                await self.sio.emit(self.MESSAGES['READY_TO_START'], {}, user['sid'])

    def __findUserInTeams(self, token):
        for teamKey in self.__teams:
            for user in self.__teams[teamKey]:
                if user['token'] == token:
                    return user, teamKey
        return None, None

    def __checkTeamIsReady(self, teamId):
        for user in self.__teams[teamId]:
            if not user['readyToStart']:
                return False
        return True
