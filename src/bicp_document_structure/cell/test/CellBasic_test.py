import unittest

from bicp_document_structure.cell.DataCell import DataCell
from bicp_document_structure.cell.address.CellIndex import CellIndex


class DataCellTest(unittest.TestCase):

    def test_assigningValue(self):
        c = DataCell(CellIndex(1, 1))
        self.assertIsNone(c.value)
        self.assertIsNone(c.script)
        c.value = 123
        self.assertEqual(123,c.value)
        self.assertIsNone(c.script)

        c.script = "x=10;x=x+1;x;"
        self.assertIsNone(c.bareValue())
        self.assertTrue(c.isValueEqual(11))
        self.assertEqual(11,c.value)


    def test_caching(self):
        self.exCount = 0
        def increaseExCount(a,b):
            self.exCount += 1
        c = DataCell(CellIndex(1, 1), onCellMutation=increaseExCount)
        c.script = "x=345;\"abc\""
        oldCount = self.exCount
        c.value
        self.assertEqual("abc",c.value)
        self.assertEqual(oldCount+1,self.exCount)

        # access value a second time
        # cell mutation callback should not be invoked this time
        # because the run result was cache, the script should not run this time
        c.value
        self.assertEqual(oldCount + 1, self.exCount)

    def test_Cell(self):
        c = DataCell(CellIndex(1, 1), 123)
        self.assertEqual(123,c.value)
        self.assertEqual(None,c.script)
        c.value= 345
        c.script = "x=345;\"abc\""
        self.assertEqual("abc",c.value)
        self.assertEqual("x=345;\"abc\"",c.script)

    def test_isValueEqual(self):
        c1 = DataCell(CellIndex(1, 1), 123)
        c2 = DataCell(CellIndex(4, 2), 123)

        self.assertTrue(c1.isValueEqual(c2))
        self.assertTrue(c2.isValueEqual(c1))
        self.assertTrue(c2.isValueEqual(c2))
        c3 = DataCell(CellIndex(2, 3), -234)
        self.assertFalse(c2.isValueEqual(c3))
        self.assertFalse(c3.isValueEqual(c2))

    def test_runCode(self):
        c1 = DataCell(CellIndex(1, 1), 123, "x=1;y=x*2+3;y")
        c1.runScript(globals(), None)
        self.assertEqual(5,c1.value)
