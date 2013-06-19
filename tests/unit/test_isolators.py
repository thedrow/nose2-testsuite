import random
import sys
import itertools

from nose2.tools import such

from tests.common.layers import UnitTestsLayer
from tests.unit.support.isolators import BuiltinsWithFakeRound, samples
from testsuite.isolation import IntegrationTestModuleIsolationLevelCalculator
from testsuite.registry import NoModulesRegisteredError
from testsuite.testdoubles import TestDouble


with such.A('Integration Test Module Isolation Level Calculation') as it:
    it.uses(UnitTestsLayer)

    @it.should('raise a NoModulesRegisteredError when fetching isolation level and no modules are registered')
    def test_should_raise_no_modules_registered_error_when_fetching_isolation_level_and_no_modules_are_registered(case):
        sut = IntegrationTestModuleIsolationLevelCalculator()

        with case.assertRaises(NoModulesRegisteredError):
            sut.calculate_isolation_level({})

    for current_modules_state in itertools.chain.from_iterable(samples):
        random.seed()
        current_modules_state = dict(current_modules_state)
        total_count = float(len([module for module in current_modules_state.values() if module]))
        total_live = float(
            len([module for module in current_modules_state.values() if not issubclass(type(module), TestDouble)]))

        expected = (total_live / total_count) * 100.0

        with it.having("The following current modules state: %s" % str(current_modules_state)):
            @it.has_test_setup
            def setUp(case):
                case._old_builtins = __builtins__

                sys.modules['__builtins__'] = BuiltinsWithFakeRound()

            @it.has_test_teardown
            def tearDown(case):
                sys.modules['__builtins__'] = case._old_builtins

            @it.should('call round with {:5.2f}'.format(expected))
            def test_should_call_round():
                sut = IntegrationTestModuleIsolationLevelCalculator()

                sut.calculate_isolation_level(current_modules_state)

                round.assert_called_once_with(expected, 2)

    it.createTests(globals())
