import EasyBible
import unittest
from test import support

class EasyBibleTestCase(unittest.TestCase):
    def test__all__(self):
        support.check__all__(self, EasyBible)

# class OtherTestCase(unittest.TestCase):
#     def test__all__(self):
#         extra = {'MAIN_CONST'}
#         not_exported = {'EasyBible'}  
#         support.check__all__(self, EasyBible, ('bar', '_bar'),
#                              extra=extra, not_exported=not_exported)
EasyBibleTestCase()
#OtherTestCase()