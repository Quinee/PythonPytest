import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("At last execution")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Quinee","Bhattacharjee","QA"]

@pytest.fixture(params=['chrome','edge','Bing'])
def selectBrowser(request):
    return request.param

@pytest.fixture(params=[('chrome','CH'),('edge','ED'),('Bing',"BI")])
def selectBrowserDetails(request):
    return request.param



