



import pytest


@pytest.mark.usefixtures("setup")
class TestClass:

    def test_fixturedemo1(self):
        print(" Fixture demo 1 it running")

    def test_fixturedemo2(self):
        print(" Fixture demo 2 it running")

    def test_fixturedemo3(self):
        print(" Fixture demo 3 it running")

    def test_fixturedemo4(self):
        print(" Fixture demo 4 it running")