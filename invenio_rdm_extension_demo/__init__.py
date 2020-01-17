# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio RDM Extension Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module to showcase how to add an extension to InvenioRDM."""

from __future__ import absolute_import, print_function

from .ext import InvenioRDMExtensionDemo
from .version import __version__

__all__ = ('__version__', 'InvenioRDMExtensionDemo')
