import re
import exrex
import unittest
from main import XMLChequeGenerator


class TestXMLChequeGenerator(unittest.TestCase):
    def setUp(self):
        self.cheque = XMLChequeGenerator()

    def test_generate_random_kpp(self):
        kpp = self.cheque.get_kpp()
        self.assertIsInstance(kpp, str)
        self.assertTrue(len(kpp) == 9)
        self.assertTrue(re.fullmatch(r'(\d{9}|)', kpp))

    def test_generate_random_inn(self):
        inn = self.cheque.get_inns()
        for i in inn:
            self.assertIsInstance(i, str)
            self.assertTrue(len(i) == 10)
        with open('INN.txt', 'r') as f:
            inns = f.read().splitlines()
        self.assertTrue(inn == inns)

    def test_generate_random_ean(self):
        ean = self.cheque.get_eans()
        for e in ean:
            self.assertIsInstance(e, str)
            self.assertTrue(len(e) == 13)
        with open('EAN.txt', 'r') as f:
            eans = f.read().splitlines()

        self.assertTrue(ean == eans)

    def test_generate_address(self):
        address = self.cheque.get_address()
        self.assertIsInstance(address, str)
        self.assertTrue(len(address) > 0 and len(address) <= 128)

    def test_get_random_number(self):
        number = self.cheque.get_random_number(0.1, 3, 0.05)
        self.assertIsInstance(number, float)
        self.assertTrue(number >= 0.1)
        self.assertTrue(number <= 1)
        self.assertTrue(round(number % 0.05, 2) <= 0.05)

    def test_get_get_barcode(self):
        barcode = self.cheque.get_barcode()
        self.assertIsInstance(barcode, str)
        self.assertTrue(re.fullmatch(
            r'\d\dN\w{20}\d[0-1]\d[0-3]\d{10}\w{31}', barcode))

    def test_get_datetime(self):
        datetime = self.cheque.get_datetime()
        self.assertIsInstance(datetime, str)
        self.assertTrue(re.fullmatch(
            r'[0-3][0-9][0-1][0-9][0-9]{2}[0-2][0-9][0-5][0-9]', datetime))
