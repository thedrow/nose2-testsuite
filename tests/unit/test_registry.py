from nose2.tools import such
import sys
from tests.unit import UnitTestsLayer
from testsuite.registry import ModulesRegistry

with such.A("Modules Registry") as it:
    it.uses(UnitTestsLayer)

    @it.should('have nothing registered when initialized')
    def test_should_be_empty_on_initialization(case):
        sut = ModulesRegistry()
        expected = {}

        actual = sut.current_state()

        case.assertEquals(actual, expected)

    @it.should('raise a TypeError when attempting to register anything else other then a dictionary')
    def test_should_raise_type_error(case):
        sut = ModulesRegistry()

        with case.assertRaises(TypeError):
            sut.register(object())

    @it.should('have exactly one registered state when registering only once')
    def test_should_have_one_state(case):
        sut = ModulesRegistry()
        expected = 1

        sut.register({'FakeModule': object()})
        actual = len(sut._registry)

        case.assertEquals(actual, expected)

    @it.should('have the same registered state when registering only once')
    def test_should_have_one_state_when_registering(case):
        sut = ModulesRegistry()
        expected = {'FakeModule': object()}

        sut.register(expected)
        actual = sut.current_state()

        case.assertEquals(actual, expected)

    @it.should('raise an IndexError when unregistering from an empty modules registry')
    def test_should_raise_index_error_when_unregistering_from_empty_registry(case):
        sut = ModulesRegistry()

        with case.assertRaises(IndexError):
            sut.unregister()

    @it.should('unregister when a state was registered before')
    def test_should_unregister(case):
        sut = ModulesRegistry()

        expected = {}

        sut.register({'FakeModule': object()})
        sut.unregister()

        actual = sut.current_state()

        case.assertEquals(expected, actual)

    @it.should('have exactly zero registered states when unregistering only once')
    def test_should_have_zero_states_when_unregistering(case):
        sut = ModulesRegistry()

        expected = 0

        sut.register({'FakeModule': object()})
        sut.unregister()

        actual = len(sut._registry)

        case.assertEquals(expected, actual)

    @it.should('register the current state of the system modules')
    def test_should_register_system_modules(case):
        sut = ModulesRegistry()

        expected = sys.modules

        sut.register_modules()

        actual = sut.current_state()

        case.assertEquals(actual, expected)

    it.createTests(globals())