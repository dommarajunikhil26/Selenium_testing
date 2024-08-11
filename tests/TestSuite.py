import unittest
from tests.test_form_page import TestFormPage
from tests.test_locators_page import TestLocatorsPage

# Create the object of class using unittes
fp = unittest.TestLoader().loadTestsFromTestCase(TestFormPage)
lp = unittest.TestLoader().loadTestsFromTestCase(TestLocatorsPage)

# Create TestSuite
regressionTest = unittest.TestSuite([fp, lp])

# Call the Test Runner Method
unittest.TextTestRunner(verbosity=1).run(regressionTest)