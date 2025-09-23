"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .gc_design import GoldenConfigDesign

__all__ = [
    "GoldenConfigDesign",
]
