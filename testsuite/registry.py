import sys


class NoModulesRegisteredError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super(NoModulesRegisteredError, self).__init__(*args, **kwargs)


class ModulesRegistry(object):
    def __init__(self):
        self._registry = []

    @property
    def current_modules_state(self):
        try:
            return self._registry[-1]
        except IndexError:
            return {}

    def register_modules(self, state):
        if not isinstance(state, dict):
            raise TypeError('Expected dictionary. Got %s instead.' % type(state))

        self._registry.append(state)

    def unregister_last_modules_state(self):
        if len(self._registry) == 0:
            raise NoModulesRegisteredError('Cannot unregister last modules state. No modules are registered.')

        self._registry.pop()

    def register_current_modules_state(self):
        self.register_modules(sys.modules)