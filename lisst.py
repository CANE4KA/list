from typing import *


def funs(num: int, cc: str) -> Any | None:
    try:
        b = ''
        if cc == "bin":
            while int(num) > 0:
                b = str(num % 2) + b
                num = num // 2
        elif cc == "octal":
            while int(num) > 0:
                b = str(num % 8) + b
                num = num // 8
        elif cc == "dec":
            b = int(num)
        elif cc == "hex":
            h = '0123456789ABCDEF'
            while int(num) > 0:
                b = h[num % 16] + b
                num = num // 16
        else:
            print("ошибка")
    except (ValueError, TypeError):
        print("not a number")
        return None
    else:
        return b