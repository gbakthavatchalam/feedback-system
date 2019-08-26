import asyncio
import datetime
import json
import logging
import os
import sys
import tornado.ioloop
import tornado.web
from tornado.log import access_log
from tornado.options import define, options, parse_command_line
from custom_logger import LogHandler
import dbutils
import minio_utils
from models import Review
import settings


logging.basicConfig(level=settings.LOGLEVEL, format=settings.LOGFORMAT)
logger = logging.getLogger(__file__)

handler = LogHandler(settings.LOGFILE, **settings.LOG_ROTATION)
logger.addHandler(handler)


def generate_log_metadata(request_handler):
    """Given the request handler, returns a dictionary containing log details"""
    method, uri, remote_ip = request_handler._request_summary().split()
    return {
        "clientip": remote_ip,
        "method": method,
        "uri": uri,
        "status": request_handler.get_status(),
        "user_agent": request_handler.request.headers["User-Agent"],
        "timestamp": str(datetime.datetime.now())
    }


def update_log(func):
    """Decorator function to log request details into minio backed up log handle.
    """
    def inner(*args, **kwargs):
        request_handler = args[0]
        log_metadata = generate_log_metadata(request_handler)
        result = func(*args, **kwargs)
        logger.info("{clientip} ({user_agent}) : {uri} {method} {status}".format(**log_metadata))
        return result
    return inner


class MainHandler(tornado.web.RequestHandler):
    """Handler for index page"""
    _map = {
        "/": "index.html",
        "/list": "list.html"
    }
    @update_log
    def get(self):
        try:
            self.render(self._map[self.request.uri])
        except KeyError:
            raise tornado.web.HTTPError(status_code=404, log_message="Page not found")


class FeedbackAPIHandler(tornado.web.RequestHandler):
    """API Handler for feedback read and save actions"""
    @update_log
    async def post(self):
        """Async Handler to save the feedback"""
        data = tornado.escape.json_decode(self.request.body)
        # Can use wtforms based validation. I'am skipping it here
        review = Review(name=f"{data['firstname']} {data['lastname']}", emailid=data["emailid"], message=data["message"])
        await dbutils.save(review)
        await minio_utils.update_record_store(generate_log_metadata(self))
        self.write(review.to_dict())


    @update_log
    def get(self):
        reviews = settings.session.query(Review).all()
        self.write(json.dumps([row.to_dict() for row in reviews]))
    

def make_app():
    return tornado.web.Application([
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'js')}),
        (r"/api/feedback", FeedbackAPIHandler),
        (r"/", MainHandler),
        (r"/list", MainHandler)

    ], **settings.APP_SETTINGS)

define("port", default="8888")
parse_command_line()


if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
