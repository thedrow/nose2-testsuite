from nose2.tools import such
from tests.common import layers
from testsuite.layers import UnitTestsLayer, FunctionalTestsLayer, IntegrationTestsLayer

with such.A('Unit Tests Layer') as it:
    it.uses(layers.UnitTestsLayer)

    @it.should("have 'Unit Tests Layer:' as the description")
    def test_should_have_correct_description(case):
        case.assertEquals(UnitTestsLayer.description, 'Unit Tests:')

    it.createTests(globals())
        
with such.A('Functional Tests Layer') as it:
    it.uses(layers.UnitTestsLayer)

    @it.should("have 'Functional Tests Layer:' as the description")
    def test_should_have_correct_description(case):
        case.assertEquals(FunctionalTestsLayer.description, 'Functional Tests:')

    it.createTests(globals())
        
with such.A('Integration Tests Layer') as it:
    it.uses(layers.UnitTestsLayer)

    @it.should("have 'Integration Tests Layer:' as the description")
    def test_should_have_correct_description(case):
        case.assertEquals(IntegrationTestsLayer.description, 'Integration Tests:')

    it.createTests(globals())