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


from tests.homework.e_functions import test_functions


from tests.homework.h_strings.test_strings import Test_Config

if __name__ == '__main__':
    unittest.main()

from tests.homework.h_strings import test_strings

suite = unittest.TestLoader().loadTestsFromModule(test_strings)


from tests.homework.g_lists_and_tuples import tests_lists_and_tuples




import unittest
from tests.homework.i_dictionaries_and_sets.test_dictionaries_and_sets import Test_Config

suite = unittest.TestLoader().loadTestsFromTestCase(Test_Config)
unittest.TextTestRunner().run(suite)
