# Here we will discuss fixtures, fixtures are nothing but the preresquisites
# or programs that run post execution

import pytest
# In case a fixture is applicable for many TCs, It's good to wrap them in a class
# It's good to wrap them in a class and use a fixture as mentioned

@pytest.mark.usefixtures("scope")

class Test_example: # Class name must start with Test not test

    def test_fixtureDemo(self):
        print("I'll be executed second !!!") 

    def test_fixtureDemo1(self):
        print("I'll be executing in demo1 !!!") 

    def test_fixtureDemo2(self):
        print("I'll be executing in demo2 !!!") 

    def test_fixtureDemo3(self):
        print("I'll be executing in demo3 !!!") 

# Testing fixture that has returning values

class TestDataLoad: # Must start with Test
    def test_checkdataLoad(self, dataLoad): # Arg as the fixture name
        print(dataLoad)
        print(dataLoad[0])

# Testing the cross browser fixture
def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    #print(crossBrowser[1]) will mean first element in the tuple if we are sending
    # multiple data in one go
