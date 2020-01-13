from tornado import web
import tornado.ioloop
from peewee_async import Manager

from ZxForm.urls import urlpattern
from ZxForm.settings import settings, database

if __name__ == "__main__":

    #集成json到wtforms
    import wtforms_json
    wtforms_json.init()

    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)

    objects = Manager(database)
    # No need for sync anymore!
    database.set_allow_sync(False)
    app.objects = objects

    tornado.ioloop.IOLoop.current().start()