"""Imports for package imgaug."""
from __future__ import absolute_import

import numpy as _np

if not hasattr(_np, "sctypes"):
    # np.sctypes was removed in NumPy 2.0. Recreate it before the submodules
    # (which read np.sctypes at import time) are loaded.
    _np.sctypes = {
        "int": [_np.int8, _np.int16, _np.int32, _np.int64],
        "uint": [_np.uint8, _np.uint16, _np.uint32, _np.uint64],
        "float": [_np.float16, _np.float32, _np.float64]
                 + ([_np.longdouble] if _np.dtype(_np.longdouble).itemsize > 8 else []),
        "complex": [_np.complex64, _np.complex128],
        "others": [bool, object, bytes, str, _np.void],
    }

# np.bool was removed in NumPy 1.24 and re-added in 2.0. Cover 1.24 to 1.26.
if not hasattr(_np, "bool"):
    _np.bool = bool

# this contains some deprecated classes/functions pointing to the new
# classes/functions, hence always place the other imports below this so that
# the deprecated stuff gets overwritten as much as possible
from imgaug.imgaug import *  # pylint: disable=redefined-builtin

import imgaug.augmentables as augmentables
from imgaug.augmentables import *
import imgaug.augmenters as augmenters
import imgaug.parameters as parameters
import imgaug.dtypes as dtypes
import imgaug.data as data

__version__ = '0.4.0'
