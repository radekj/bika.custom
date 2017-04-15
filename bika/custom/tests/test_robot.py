from bika.custom.testing import BIKA_CUSTOM_TESTING
from plone.testing import layered

import robotsuite
import unittest


ROBOT_TESTS = [
    'test_custom.robot',
]


def test_suite():
    suite = unittest.TestSuite()
    for RT in ROBOT_TESTS:
        suite.addTests([
            layered(robotsuite.RobotTestSuite(RT), layer=BIKA_CUSTOM_TESTING),
        ])
    return suite
