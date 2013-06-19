from testsuite.registry import NoModulesRegisteredError
from testsuite.testdoubles import TestDouble


class IsolationLevelError(AssertionError):
    def __init__(self, *args, **kwargs):
        pass


class IntegrationTestModuleIsolationLevelCalculator(object):
    def calculate_isolation_level(self, current_state):
        if current_state == {}:
            raise NoModulesRegisteredError('Cannot calculate isolation level. No modules were registered.')

        total = [module for module in current_state.values() if module]
        live = [(name, module) for name, module in current_state.items()
                if module and not issubclass(type(module), TestDouble)]
        total_count = float(len(total))
        live_count = float(len(live))

        return round((live_count / total_count) * 100.0, 2)