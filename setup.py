#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""python_course setup script"""
from setuptools import setup

import versioneer

if __name__ == "__main__":
    setup(
        name="python_course",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        zip_safe=False,
    )
