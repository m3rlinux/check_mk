#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK Cloudmark Info Plugin
#
# Copyright 2019, Davide Gibilisco <m3rlinux.it@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

group = "checkparams"

subgroup_applications = _("Applications, Processes & Services")


register_check_parameters(
    subgroup_applications,
    "cloudmark",
    _("Settings for Cloudmark check"),
    Dictionary(
        elements = [
            ("Queue",
                Tuple(
                    title = _("Queue"),
                    elements = [
                        Integer(
                            title = _("Warning at"),
                            default_value = None,
                        ),
                        Integer(
                            title = _("Critical at"),
                            default_value = None,
                        ),
                    ],
                ),
            ),
            ("Concurrency",
                Tuple(
                    title = _("Concurrency"),
                    elements = [
                        Integer(
                            title = _("Warning at"),
                            default_value = None,
                        ),
                        Integer(
                            title = _("Critical at"),
                            default_value = None,
                        ),
                    ],
                ),
            ),
            ("Delivery",
                Tuple(
                    title = _("Delivery"),
                    elements = [
                        Integer(
                            title = _("Warning at"),
                            default_value = None,
                        ),
                        Integer(
                            title = _("Critical at"),
                            default_value = None,
                        ),
                    ],
                ),
            ),
        ],
        optional_keys = [ "Queue", "Concurrency", "Delivery" ],
    ),
    TextAscii( title = _("Cloudmark Name")),
    'dict'
)
