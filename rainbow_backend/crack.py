__all__ = ('crack_md5_brute_force', )
from rainbow_backend.rainbow_utils.util import md5
from typing import Optional

# 暴力破解 6~8 位数字密码
def crack_md5_brute_force(hsh: str) -> Optional[str]:
    assert len(hsh) == 32

    for i in range(100000000):
        password = f'{i:0>6}'
        if md5(password) == hsh:
            return password

    return None
