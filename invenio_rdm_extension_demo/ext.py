# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Invenio RDM Extension Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module to showcase how to add an extension to InvenioRDM."""

from __future__ import absolute_import, print_function

from flask_babelex import gettext as _

from . import config


class InvenioRDMExtensionDemo(object):
    """Invenio RDM Extension Demo extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-rdm-extension-demo'] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('INVENIO_RDM_EXTENSION_DEMO_'):
                app.config.setdefault(k, getattr(config, k))
