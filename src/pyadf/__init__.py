"""pyadf - A Python library for converting Atlassian Document Format (ADF) to Markdown."""

from .document import Document
from ._logger import set_debug_mode

__version__ = "0.1.0"
__all__ = ["Document", "set_debug_mode"]
