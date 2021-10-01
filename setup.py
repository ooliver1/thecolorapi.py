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

from setuptools import setup, find_packages
import re

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = ""
with open("colorapi/__init__.py") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(),
        re.MULTILINE
    ).group(1)

if not version or version == "":
    raise RuntimeError("version is not set")

if version.endswith(("a", "b", "rc")):
    # append version identifier based on commit count
    try:
        import subprocess
        p = subprocess.Popen(
            ["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode("utf-8").strip()
        p = subprocess.Popen(
            ["git", "rev-parse", "--short", "HEAD"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += "+g" + out.decode("utf-8").strip()
    except Exception:
        pass

readme = ""
with open("README.rst") as f:
    readme = f.read()

setup(
    name="thecolorapi.py",
    description="thecolorapi python wrapper",
    version=version,
    long_description=readme,
    long_description_content_type="text/x-rst",
    project_urls={
        "Issue tracker": "https://github.com/ooliver1/thecolorapi.py/issues",
    },
    author="Oliver Wilkes - ooliver1",
    url="https://github.com/ooliver1/thecolorapi.py",
    download_url="https://github.com/ooliver1/thecolorapi.py.git",
    packages=find_packages(),
    license="GNU General Public License GPL v3 or later",
    license_files=["LICENSE"],
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved ::\
            GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Internet"
        "Topic :: Sofrware Development :: Libraries",
        "Topic :: Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ]
)
