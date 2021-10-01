# region License Declaration - GPL-3.0+ - Oliver Wilkes
"""
SPDX-License-Identifier: GPL-3.0-or-later
thecolorapi.py - A python api wrapper in python
Copyright (C) 2021-present  Oliver Wilkes - ooliver1

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
# endregion

__title__ = "colorapi"
__author__ = "Oliver Wilkes - ooliver1"
__license__ = "GPLv3+"
__copyright__ = "Copyright 2021-present - Oliver Wilkes [ooliver1]"
__version__ = "0.0.0a"


import logging
from typing import NamedTuple, Literal


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=0, micro=0, releaselevel="alpha", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
