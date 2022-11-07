#!/usr/bin/env python
# coding: utf-8
#first comment

# In[13]:


from typing import List
#fdsgfstdth
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """

    if x < 0 or y < 0 or x >= len(input_board) or y >= len(input_board[x]):
        return None
    elif input_board[x][y] == ".":
        s = list(input_board[x])
        s[y] = '~'
        z = ''.join(s)
        input_board[x] = z
        flood_fill(input_board=board, old=".", new="~", x=x+1, y=y)
        flood_fill(input_board=board, old=".", new="~", x=x-1, y=y)
        flood_fill(input_board=board, old=".", new="~", x=x, y=y+1)
        flood_fill(input_board=board, old=".", new="~", x=x, y=y-1)
        return input_board

    modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)


    modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

    for a in modified_board:
        print(a)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....


# In[ ]:




