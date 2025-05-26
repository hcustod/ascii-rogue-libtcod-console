from sqlite3 import DateFromTicks
from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),             
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", bool),
        ("transparent", bool),
        ("dark", graphic_dt),
        ("light", graphic_dt),
    ]
)

def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
    light: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]]  #may need a comma here?
) -> np.ndarray:
    return np.array((walkable,transparent,dark, light), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255,255,255), (0,0,0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True, 
    dark=(ord(" "), (255,255,255), (50,50,100)),
    light=(ord(" "), (255,255,255), (200,180,50))
)

wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord(" "), (255,255,255), (0,0,150)),
    light=(ord(" "), (255,255,255), (130,110,50))
)

down_staris = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (0, 0, 100), (50, 50, 150)),
    light=(ord(">"), (255, 255, 255), (200, 180, 50)),
)