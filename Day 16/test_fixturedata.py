
import pytest
"""
@pytest.mark.usefixtures("newdata")
class Fixdata:
    def test_myfixdata(self,newdata):
        print(newdata)

"""

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])