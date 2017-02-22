from nameko.rpc import rpc


class HelloWorld(object):
    name = "hello"

    @rpc
    def greet(self, friend):
        return "Hello {}!".format(friend)
