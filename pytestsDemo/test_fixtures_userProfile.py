import pytest

@pytest.mark.usefixtures('dataLoad')
class TestExampleUserProfile:
    @pytest.mark.skip
    def test_userProfile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])

@pytest.mark.skip
def test_crossBrowser(selectBrowser):
    print('Browser selected is '+selectBrowser)


def test_crossBrowserDetails(selectBrowserDetails):
    print('BrowserName is '+selectBrowserDetails[0]+' and Initial is '+selectBrowserDetails[1])