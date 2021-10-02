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

import sys
import time
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Tuple,
    Union
)

import requests

from . import utils
from . import __version__
from .types import Response
from .errors import HTTPException


class Route:
    BASE: ClassVar[str] = "https://www.thecolorapi.com"

    def __init__(self, method: str, path: str) -> None:
        self.path: str = path
        self.method: str = method
        url: str = self.BASE + self.path
        self.url: str = url


def json_or_text(response: requests.Response) -> Union[Dict[str, Any], str]:
    text = response.text(encoding='utf-8')
    try:
        if response.headers['content-type'] == 'application/json':
            return utils._from_json(text)
    except KeyError:
        # Thanks Cloudflare
        pass

    return text


class HTTPClient:
    def __init__(self) -> None:
        user_agent = "https://github.com/ooliver1/thecolorapi.py \
            {0} Python/{1[0]}.{1[1]}"
        self.user_agent: str = user_agent.format(
            __version__, sys.version_info_)
        self.__session: requests.Session = requests.Session()

    def request(
        self,
        route: Route,
        **kwargs: Any
    ) -> Optional[Union[Dict[str, Any], str, Any]]:
        method = route.method
        url = route.url

        headers: Dict[str, str] = {
            "User-Agent": self.user_agent,
        }

        kwargs["headers"] = headers

        for tries in range(5):
            try:
                with self.__session.request(method, url, **kwargs) as response:
                    data = json_or_text(response)
                    if 300 > response.status >= 200:
                        return data

            except OSError as e:
                # Connection reset by peer
                if tries < 4 and e.errno in (54, 10054):
                    time.sleep(1 + tries * 2)
                    continue
                raise

        if response is not None:
            raise HTTPException(response, data)

    def fetch_color(
        self,
        params: Union[Dict[str, str], List[Tuple[str, str]]]
    ) -> Response:
        return self.request(Route("GET", "/id"), params=params)

    def fetch_scheme(
        self,
        params: Union[Dict[str, str], List[Tuple[str, str]]]
    ) -> Response:
        return self.request(Route("GET", "/scheme"), params=params)
