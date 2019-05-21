__all__ = ('gen_rainbow_table', )
from typing import List, Tuple
from .rainbow_utils import rainbow_iter


def gen_visited_list() -> List[bool]:
    return [False] * 1_0000_0000


# 生成 8 位数字的彩虹表
# 彩虹表格式：[ (原文, 原文), ... ] （不包括哈希）
def gen_rainbow_table(loop_count=20, k_len=1000) -> Tuple[List[Tuple[int, int]], List[bool]]:
    vis = gen_visited_list()
    vis_count = 0

    def enter_rainbow_table(num: int):
        nonlocal vis, vis_count
        vis[num] = True
        vis_count += 1

    rainbow_table: List[Tuple[int, int]] = []
    buf = ['0'] * 8

    # while vis_count < 1_0000_0000:
    for i in range(loop_count):
        # 获取第一个还没进入彩虹表的数
        # 开始的原文
        start_orig = next(x for x in range(1_0000_0000) if not vis[x])

        orig = start_orig
        enter_rainbow_table(orig)

        for j in range(k_len):
            orig = rainbow_iter(orig)
            enter_rainbow_table(orig)

        rainbow_table.append((start_orig, orig))

    return rainbow_table, vis
