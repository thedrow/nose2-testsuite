import binascii
import logging
import os
import pickle
from random import choice
import sys

from tests.common.compat import *
from tests.common import is_executing_under_continuous_integration_server, get_support_path
from testsuite.testdoubles import TestDouble

class BuiltinsWithFakeRound(object):
    def __init__(self):
        self.__dict__ = __builtins__.__dict__ if hasattr(__builtins__, '__dict__') else __builtins__
        self._old_round = self.round
        self.round = mock.Mock()


class FakeModuleNameGenerator(str):
    @classmethod
    def __new__(cls, *args, **kwargs):
        return str(binascii.b2a_hex(os.urandom(15)))


class FakeModule(object):
    @classmethod
    def __new__(cls, *args, **kwargs):
        return choice([object(), TestDouble()])


class SamplesIterator(object):
    MAX_SAMPLE_LENGTH = os.getenv('MAX_SAMPLE_LENGTH', 12) if is_executing_under_continuous_integration_server() else 6

    def __iter__(self):
        for sample_length in range(1, SamplesIterator.MAX_SAMPLE_LENGTH):
            combinations = [(FakeModuleNameGenerator(), FakeModule()) for i in range(0, sample_length)]

            for r in range(1, sample_length + 1):
                yield itertools.combinations_with_replacement(combinations, r)


def get_sample_file_name():
    import platform

    version = '%s.%s' % (
        sys.version_info[0], sys.version_info[1]) if platform.python_implementation() != 'PyPy' else 'pypy'
    samples_file = '%s%s' % (get_support_path(), 'modules_state.samples-%s' % version)
    return samples_file


def load_samples():
    if is_executing_under_continuous_integration_server() and os.getenv('USE_CACHES_SAMPLES', 'false') != 'true':
        list(itertools.chain.from_iterable(SamplesIterator()))

    samples_file = get_sample_file_name()

    if os.path.exists(samples_file) and os.path.getsize(samples_file) == 0 or not os.path.exists(samples_file):
        with open(samples_file, 'wb') as f:
            samples = list(itertools.chain.from_iterable(SamplesIterator()))

            try:
                return samples
            finally:
                pickle.dump(samples, f, pickle.HIGHEST_PROTOCOL)
    else:
        with open(samples_file, 'rb') as f:
            return pickle.load(f)