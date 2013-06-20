import binascii
import logging
import os
import pickle
from random import choice
from tests.common.compat import *
from tests.common import is_executing_under_continuous_integration_server, get_support_path

from testsuite.testdoubles import TestDouble

logger = logging.getLogger(__name__)


class BuiltinsWithFakeRound(object):
    def __init__(self):
        self.__dict__ = __builtins__
        self.round = mock.Mock()


class FakeModuleNameGenerator(object):
    def __repr__(self):
        return str(binascii.b2a_hex(os.urandom(15)))


class FakeModule(object):
    def __new__(cls, *args, **kwargs):
        return choice([object(), TestDouble()])


class SamplesIterator(object):
    MAX_SAMPLE_LENGTH = os.getenv('MAX_SAMPLE_LENGTH', 36) if is_executing_under_continuous_integration_server() else 6

    def __iter__(self):
        for sample_length in range(1, SamplesIterator.MAX_SAMPLE_LENGTH):
            combinations = [(FakeModuleNameGenerator(), FakeModule()) for i in range(0, sample_length)]

            for r in range(1, sample_length + 1):
                logger.info("Generating sample in length %d with r=%d" % (sample_length, r))
                yield itertools.combinations_with_replacement(combinations, r)


def load_samples():
    if is_executing_under_continuous_integration_server() and os.getenv('USE_CACHES_SAMPLES', 'false') != 'true':
        list(itertools.chain.from_iterable(SamplesIterator()))

    samples_file = '%s%s' % (get_support_path(), 'modules_state.samples')

    if os.path.exists(samples_file) and os.path.getsize(samples_file) == 0 or not os.path.exists(samples_file):
        with open(samples_file, 'a+') as f:
            samples = list(itertools.chain.from_iterable(SamplesIterator()))

            try:
                return samples
            finally:
                pickle.dump(samples, f, pickle.HIGHEST_PROTOCOL)
    else:
        with open(samples_file, 'r') as f:
            return pickle.load(f)