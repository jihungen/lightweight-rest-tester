from . import TestFunction, TestFunctionBuilder


class FailTestFunctionBuilder(TestFunctionBuilder):
    """Build test function to let unittest know failure."""
    def __init__(self, msg, file_name):
        self._file_name = file_name
        self._msg = msg

    def build(self):
        def test_function(test_self):
            test_self.fail(self._msg)

        test_function_name = 'test_%s' % self._file_name
        return TestFunction(test_function_name, test_function)
