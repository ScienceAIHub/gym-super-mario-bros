"""Registration code of Gym environments in this package."""
import warnings

# Suppress gym deprecation warnings for better user experience
warnings.filterwarnings('ignore', category=UserWarning, module='gym')

from .smb_env import SuperMarioBrosEnv
from .smb_random_stages_env import SuperMarioBrosRandomStagesEnv
from ._registration import make


# define the outward facing API of this package
__all__ = [
    make.__name__,
    SuperMarioBrosEnv.__name__,
    SuperMarioBrosRandomStagesEnv.__name__,
]
