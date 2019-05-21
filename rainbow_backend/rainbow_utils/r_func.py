__all__ = ('rainbow_r', 'rainbow_iter')
from .util import md5_byte
from .fmt import fmt_int_8

def rainbow_r(hsh: bytes) -> int:
    res = 0

    for i in range(8):
        delta = hsh[i] % 10
        res *= 10
        res += delta

    return res

# 输入 8 位密码，返回 8 位密码
def rainbow_iter(orig: int) -> int:
    orig_fmt = fmt_int_8(orig)
    hsh = md5_byte(orig_fmt)
    return rainbow_r(hsh)
