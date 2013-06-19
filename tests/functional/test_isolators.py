import random
import itertools

from nose2.tools import such

from tests.common.layers import FunctionalTestsLayer
from tests.unit.support.isolators import samples
from testsuite.isolation import IntegrationTestModuleIsolationLevelCalculator
from testsuite.testdoubles import TestDouble


with such.A('Integration Test Module Isolation Level Calculation') as it:
    it.uses(FunctionalTestsLayer)

    for current_modules_state in itertools.chain.from_iterable(samples):
        random.seed()
        current_modules_state = dict(current_modules_state)
        total_count = float(len([module for module in current_modules_state.values() if module]))
        total_live = float(
            len([module for module in current_modules_state.values() if not issubclass(type(module), TestDouble)]))

        expected = (total_live / total_count) * 100.0

        with it.having("The following current modules state: %s" % str(current_modules_state)):
            @it.should('have the following isolation level {:5.2f}'.format(expected))
            def test_should_have_correct_isolation_level(case):
                sut = IntegrationTestModuleIsolationLevelCalculator()

                actual = sut.calculate_isolation_level(current_modules_state)

                case.assertEquals(actual, expected)

    it.createTests(globals())

