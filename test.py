import re
import exrex

while True:
    kpp = exrex.getone(r'(\d{9}|)')
    if kpp:
        break
print(kpp)
print('YES' if re.fullmatch(
    r'(\d{9}|)', kpp) else 'NO')
