"""
JWST-Tools: Python package to analyze JWST data.

This package provides tools for reducing and analyzing JWST data products.
"""

__version__ = "0.1.0"
__author__ = "BDNYC"

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

__all__ = ["__version__", "__author__"]
