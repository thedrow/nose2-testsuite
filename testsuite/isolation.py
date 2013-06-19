from testsuite.registry import NoModulesRegisteredError
from testsuite.testdoubles import TestDouble


class IsolationLevelError(AssertionError):
    def __init__(self, *args, **kwargs):
        pass


class IntegrationTestModuleIsolationLevelCalculator(object):
    def calculate_isolation_level(self, current_state, exclude=None):
        if not exclude: exclude = []

        if current_state == {}:
            raise NoModulesRegisteredError('Cannot calculate isolation level. No modules were registered.')

        if not issubclass(type(current_state), dict):
            raise TypeError("Expected dict. Got %s instead." % type(current_state))

        total = [(name, module) for name, module in current_state.items() if module and name not in exclude]
        live = [(name, module) for name, module in current_state.items()
                if module and not issubclass(type(module), TestDouble) and name not in exclude]
        total_count = float(len(total))
        live_count = float(len(live))

        if total_count == 0 and live_count == 0 and len(exclude) != 0:
            return 100

        return round((live_count / total_count) * 100.0, 2)