from aiohttp import web

from settings import SETTINGS
from application.modules.db.DB import DB
from application.modules.mediator.Mediator import Mediator
# user
# chat
# audio ?
# pirates
from application.router.Router import Router

db = DB(SETTINGS['DB'])
mediator = Mediator(SETTINGS['MEDIATOR']['EVENTS'], SETTINGS['MEDIATOR']['TRIGGERS'])
mediator.set('GET_USER_BY_ID', db.getUserById)
mediator.set('GET_USER_BY_TOKEN', db.getUserByToken)
mediator.get('GET_USER_BY_ID', '1')

app = web.Application()
Router(app, web, mediator)

web.run_app(app)