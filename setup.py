#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""workout_analysis setup script"""
from setuptools import setup

import versioneer

if __name__ == "__main__":
    setup(
        name="workout_analysis",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        zip_safe=False,
    )
