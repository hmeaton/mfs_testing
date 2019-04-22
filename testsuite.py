import unittest
import add_customer
import edit_customer
import add_product
import edit_product
import add_service
import edit_service
import delete_service
import delete_product
import delete_customer


# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(add_customer))
suite.addTests(loader.loadTestsFromModule(edit_customer))
suite.addTests(loader.loadTestsFromModule(add_product))
suite.addTests(loader.loadTestsFromModule(edit_product))
suite.addTests(loader.loadTestsFromModule(add_service))
suite.addTests(loader.loadTestsFromModule(edit_service))
suite.addTests(loader.loadTestsFromModule(delete_service))
suite.addTests(loader.loadTestsFromModule(delete_product))
suite.addTests(loader.loadTestsFromModule(delete_customer))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)