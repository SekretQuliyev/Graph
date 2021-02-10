# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved..

from graph.logger import logging  # noqa
from graph.config import Config, get_version  # noqa
from graph.core import (  # noqa
    Graph, filters, Message, get_collection, pool)

graph = Graph()  # userge is the client name
