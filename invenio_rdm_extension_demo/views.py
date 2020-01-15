# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio RDM Extension Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module to showcase how to add an extension to InvenioRDM"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    'invenio_rdm_extension_demo',
    __name__
)


@blueprint.route("/rdm-ext-demo")
def index():
    """RDM Extension Demo view"""
    return 'RDM Extension Demo!'
