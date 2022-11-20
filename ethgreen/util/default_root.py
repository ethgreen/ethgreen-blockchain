from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("ETHGREEN_ROOT", "~/.ethgreen/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("ETHGREEN_KEYS_ROOT", "~/.ethgreen_keys"))).resolve()
