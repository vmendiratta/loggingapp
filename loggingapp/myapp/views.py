# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

logger = logging.getLogger('app.info')

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    logger.debug({'payload': {'mess': 'test debug', 'test': 'success'}})
    logger.info('test info')
    logger.warning('test warning')
    return HttpResponse("Hello, world. You're at the polls index.")
