import random
import string
import subprocess
import xml.etree.ElementTree as ET

import re
import exrex


class XMLChequeGenerator:
    def __init__(self):
        self.root = ET.Element("Cheque")

    def get_random_re(self, pattern):
        return exrex.getone(pattern)

    def get_random_string(length=128):
        characters = string.ascii_letters + string.digits + \
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        return ''.join(random.choice(characters) for _ in range(length))
    # Bottle

    def get_price():
        return round(random.uniform(100.00, 1001.00), 2)

    def get_barcode(self):
        return self.get_random_re(r'\d\dN\w{20}\d[0-1]\d[0-3]\d{10}\w{31}')

    def get_eans(self):
        with open('EAN.txt', 'r') as f:
            eans = f.read().splitlines()
        return eans

    def get_random_number(self, start=0.10000, end=3.0000, step=0.05):
        range_values = int((end - start) / step) + 1
        random_index = random.randint(0, range_values - 1)
        random_value = start + random_index * step
        return round(random_value, 4)

    def get_volume(self):
        return self.get_random_number(0.1000, 3.0000, 0.05)

    # Cheque
    def get_inns(self):
        with open('INN.txt', 'r') as f:
            inns = f.read().splitlines()
        return inns

    def get_kpp(self):
        return self.get_random_re(r'(\d{9}|)')

    def get_address(self):
        return self.get_random_string()

    def get_price(self):
        return self.get_random_re(r'[-]?\d+\.\d{0,2}')

    def get_name(self):
        return self.get_random_string()

    def get_kassa(self):
        return self.get_random_string()

    def get_shift(self):
        return random.randint(0, 100)

    def get_number(self):
        return random.randint(0, 100)

    def get_random_datetime(self):
        return self.get_random_re(r'[0-3][0-9][0-1][0-9][0-9]{2}[0-2][0-9][0-5][0-9]')

    def get_cheque(self):
        self.root.set('inn', random.choice(self.get_inns()))
        self.root.set('kpp', self.get_kpp())
        self.root.set('address', self.get_address())
        self.root.set('name', self.get_name())
        self.root.set('kassa', self.get_kassa())
        self.root.set('shift', self.get_shift())
        self.root.set('number', self.get_number())
        self.root.set('datetime', self.get_datetime())

    def get_random_bottle(self):
        num_bottles = random.randint(1, 10)
        for _ in range(num_bottles):
            bottle = ET.SubElement(self.root, "Bottle")
            bottle.set('price', self.get_price())
            bottle.set('barckode', self.get_barkode())
            bottle.set('ean', random.choice(self.get_eans()))
            bottle.set('volume', self.get_volume())

    def save_xml(self, filename='generated_cheque.xml'):

        tree = ET.ElementTree(self.root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)


x = XMLChequeGenerator()
x.save_xml('test.xml')
