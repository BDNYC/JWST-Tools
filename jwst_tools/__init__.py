"""
JWST-Tools: Python package to analyze JWST data.

This package provides tools for reducing and analyzing JWST data products.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("jwst-tools")
except PackageNotFoundError:
    __version__ = "unknown"

# Import key dependencies to verify they are available
try:
    import astropy
    import matplotlib
    import jwst
    import astroquery
    import specutils
except ImportError as e:
    import warnings
    warnings.warn(f"Some dependencies are not available: {e}")

__all__ = ["__version__"]
