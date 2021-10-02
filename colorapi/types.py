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

from typing import (
    Dict,
    Union
)

Response = Union[
    str,
    Dict[
        str,
        Dict[
            str,
            Union[str, int, None, Dict[str, Union[str, int, float, None]]]
        ]
    ]
]
