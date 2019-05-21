__all__ = ('md5_byte', 'md5')
import hashlib


def md5_byte(s: str, encoding='utf-8'):
    return hashlib.md5(s.encode(encoding=encoding)).digest()


def md5(s: str, encoding='utf-8'):
    return hashlib.md5(s.encode(encoding=encoding)).hexdigest()
