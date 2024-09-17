import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.b_input_process_output import tests_input_process_output


suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)
unittest.TextTestRunner(verbosity=2).run(suite)


from tests.homework.c_decisions import test_decisions

suite = unittest.TestLoader().loadTestsFromModule(test_decisions)


# tests/homework/d_repetition/run_tests.py

import unittest
from tests.homework.d_repetition import test_decisions

suite = unittest.TestLoader().loadTestsFromModule(test_decisions)
unittest.TextTestRunner().run(suite)
