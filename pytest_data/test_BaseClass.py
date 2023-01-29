import pytest

from pytest_data.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestDataLoad(BaseClass): # Must start with Test
    def test_checkdataLoad(self, dataLoad): # Arg as the fixture name (dataLoad)
        logger = self.getLogger()
        #print(dataLoad)
        logger.info(dataLoad)
        #print(dataLoad[0])
        logger.info(dataLoad[0])