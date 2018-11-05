# -*- coding: utf-8 -*-

"""Main module."""

from abc import ABC, abstractmethod

class CookingProtocol(ABC):
    mex_type = None
    message = None


class coocking_protocol_message_factory(ABC):
    # Create based on class name:
    def factory(rawInMex):
        pass

    def convertInMex(rawInMex, mexType):
        pass

    def convertOutMex(rawInMex, mexType):
        pass

    def defineMex(rawInMex):
        pass

    factory = staticmethod(factory)
    defineMex = staticmethod(defineMex)
    convertInMex = staticmethod(convertInMex)
    convertOutMex = staticmethod(convertOutMex)
