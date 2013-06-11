import sys


class ModulesRegistry(object):
    def __init__(self):
        self._registry = []

    def current_state(self):
        try:
            return self._registry[-1]
        except IndexError:
            return {}

    def register(self, state):
        if not isinstance(state, dict):
            raise TypeError('Expected dictionary. Got %s instead.' % type(state))

        self._registry.append(state)

    def unregister(self):
        self._registry.pop()

    def register_modules(self):
        self.register(sys.modules)