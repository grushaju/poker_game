__version__ = "1.0.0"
__author__ = "Pavel Grushin"
__license__ = "GPL-3.0"
__copyright__ = f"2025, {__author__}"
__homepage__ = "https://github.com/grushaju/poker_game"
__docs__ = (
    "poker_game is a general purpose python poker engine for running arbitrary poker "
    "configurations with a built-in fast hand evaluator."
)

try:
    # This variable is injected in the __builtins__ by the build
    # process. It is used to enable importing subpackages when
    # the binaries are not built
    __CLUBS_SETUP__
    __CLUBS_SETUP__: bool = True
except NameError:
    __CLUBS_SETUP__ = False

if __CLUBS_SETUP__:
    pass  # pragma: no cover
else:
    from . import configs, poker, render
    from .poker import Card, Dealer, Deck, Evaluator, LookupTable

__all__ = [
    "configs",
    "poker",
    "render",
    "Card",
    "Dealer",
    "Deck",
    "Evaluator",
    "LookupTable",
]
