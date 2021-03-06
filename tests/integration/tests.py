import unittest
from tests.integration.exchange import BacktestExchangeBaseIntegrationTest
from tests.integration.run import (
    ParseParamsAndExecuteAlgorithmIntegrationTests, MainLoopIntegrationTest,
    ExecuteAlgorithmIntegrationTests)


def test_suite():
    suite = unittest.TestSuite([
        unittest.makeSuite(BacktestExchangeBaseIntegrationTest),
        unittest.makeSuite(ExecuteAlgorithmIntegrationTests),
        unittest.makeSuite(MainLoopIntegrationTest),
        unittest.makeSuite(ParseParamsAndExecuteAlgorithmIntegrationTests),
    ])
    return suite
