from nameko.web.handlers import http

from .dependencies import CacheClient


class HelloWorld(object):
    name = "hello"

    cache = CacheClient()

    @http("GET", "/greet/<string:friend>")
    def greet(self, request, friend):
        greeting = self.cache.get(friend)

        if greeting is None:
            greeting = "Hello {}!".format(friend)  # expensive
            self.cache.set(friend, greeting)

        return greeting
