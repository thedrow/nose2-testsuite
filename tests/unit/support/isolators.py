import binascii
import os
from random import choice
import itertools

from mock import Mock
from tests.common import is_executing_under_continuous_integration_server

from testsuite.testdoubles import TestDouble


class BuiltinsWithFakeRound(object):
    def __init__(self):
        self.__dict__ = __builtins__
        self.round = Mock()


class FakeModuleNameGenerator(object):
    def __repr__(self):
        return binascii.b2a_hex(os.urandom(15))


class FakeModule(object):
    def __new__(cls, *args, **kwargs):
        return choice([object(), TestDouble()])


class SamplesIterator(object):
    def __iter__(self):
        MAX_SAMPLE_LENGTH = 256 if is_executing_under_continuous_integration_server() else 6

        for sample_length in range(1, MAX_SAMPLE_LENGTH):
            combinations = ((FakeModuleNameGenerator(), FakeModule()) for i in range(0, sample_length))

            for r in range(1, sample_length):
                yield itertools.combinations_with_replacement(combinations, r)

samples = SamplesIterator()