import re
import exrex

x = exrex.getone('[0-3][0-9][0-1][0-9][0-9]{2}[0-2][0-9][0-5][0-9]')
print('YES' if re.fullmatch(
    r'[0-3][0-9][0-1][0-9][0-9]{2}[0-2][0-9][0-5][0-9]', x) else 'NO')
