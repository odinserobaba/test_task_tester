import random
import string
import subprocess
import xml.etree.ElementTree as ET
import rstr
import numpy as np


class XMLChequeGenerator:
    def __init__(self):
        self.root = ET.Element("Cheque")

    def get_random_re(self, pattern):
        return rstr.xeger(pattern)

    def get_random_string(self, length=128):
        valid_characters = string.ascii_letters + string.digits.upper()
        return ''.join(random.choice(valid_characters) for _ in range(length))
    # Bottle
    # Цена открицательное число?????

    def get_price(self):
        return self.get_random_re(r'[-]?\d+\.\d{0,2}')

    def get_barcode(self):
        return self.get_random_re(r'\d\dN\w{20}\d[0-1]\d[0-3]\d{10}\w{31}')

    def get_eans(self):
        with open('EAN.txt', 'r') as f:
            eans = f.read().splitlines()
        return eans

    def get_random_number(self, start=0.1000, stop=3.0000, step=0.05):
        range_values = list(np.arange(start, stop, step))
        return round(random.choice(range_values), 4)

    def get_volume(self):
        return str(round(self.get_random_number(0.1000, 3.0000, 0.05), 4))

    # Cheque
    def get_inns(self):
        with open('INN.txt', 'r') as f:
            inns = f.read().splitlines()
        return inns

    def get_kpp(self):
        return str(random.randint(111111111, 999999999))

    def get_address(self):
        return self.get_random_string()

    def get_name(self):
        return self.get_random_string()

    def get_kassa(self):
        return self.get_random_string()

    def get_shift(self):
        return str(random.randint(0, 100))

    def get_number(self):
        return str(random.randint(0, 100))

    def get_datetime(self):
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
            bottle.set('barcode', self.get_barcode())
            bottle.set('ean', random.choice(self.get_eans()))
            bottle.set('volume', self.get_volume())

    def save_xml(self, filename='generated_cheque.xml'):
        self.get_cheque()
        self.get_random_bottle()
        tree = ET.ElementTree(self.root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    def send_xml(self, filename, url):
        command = ['curl', '-F', f'xml_file=@{filename}', url]
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print("XML файл успешно отправлен.")
        else:
            print("Ошибка при отправке XML файла.")
            print(result.stderr.decode('utf-8'))


x = XMLChequeGenerator()
x.save_xml('test.xml')
x.send_xml('test.xml', 'http://localhost:8080/xml')
