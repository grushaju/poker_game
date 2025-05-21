import sys
from typing import List, Optional, Union, TypedDict, Literal


class PokerConfig(TypedDict):
    num_players: Union[int, Literal["rnd"]]
    num_streets: int
    blinds: Union[int, List[int]]
    antes: Union[int, List[int]]
    raise_sizes: Union[
        int, Literal["pot", "inf"], List[Union[int, Literal["pot", "inf"]]]
    ]
    num_raises: Union[int, Literal["inf"], List[Union[int, Literal["inf"]]]]
    num_suits: int
    num_ranks: int
    num_hole_cards: int
    num_community_cards: Union[int, List[int]]
    num_cards_for_hand: int
    mandatory_num_hole_cards: int
    start_stack: int
    low_end_straight: bool
    order: Optional[List[str]]


NO_LIMIT_HOLDEM_NINE_PLAYER: PokerConfig = {
    "num_players": 9,
    "num_streets": 4,
    "blinds": [1, 2],
    "antes": 0,
    "raise_sizes": "inf",
    "num_raises": "inf",
    "num_suits": 4,
    "num_ranks": 13,
    "num_hole_cards": 2,
    "num_community_cards": [0, 3, 1, 1],
    "num_cards_for_hand": 5,
    "mandatory_num_hole_cards": 0,
    "start_stack": 100,
    "low_end_straight": True,
    "order": None,
}

NO_LIMIT_HOLDEM_RANDOM_PLAYER: PokerConfig = {
    "num_players": "rnd",
    "num_streets": 4,
    "blinds": [1, 2],
    "antes": 0,
    "raise_sizes": "inf",
    "num_raises": "inf",
    "num_suits": 4,
    "num_ranks": 13,
    "num_hole_cards": 2,
    "num_community_cards": [0, 3, 1, 1],
    "num_cards_for_hand": 5,
    "mandatory_num_hole_cards": 0,
    "start_stack": 100,
    "low_end_straight": True,
    "order": None,
}
