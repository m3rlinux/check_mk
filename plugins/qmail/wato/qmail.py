#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# Check_MK Qmail Queue Plugin
#
# Copyright 2021, Davide Gibilisco <m3rlinux.it@gmail.com>
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

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Transform,
    Tuple,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)

mailqueue_params = Dictionary(
    elements=[
        (
            "local",
            Tuple(
                title=_("Mails injected locally"),
                help=_("This rule is applied to the number of E-Mails currently "
                       "in the local mail queue."),
                elements=[
                    Integer(title=_("Warning at"), unit=_("mails"), default_value=1000),
                    Integer(title=_("Critical at"), unit=_("mails"), default_value=2000),
                ],
            ),
        ),
        (
            "remote",
            Tuple(
                title=_("Mails received remotely"),
                help=_("This rule is applied to the number of E-Mails currently "
                       "in the remote mail queue"),
                elements=[
                    Integer(title=_("Warning at"), unit=_("mails"), default_value=8000),
                    Integer(title=_("Critical at"), unit=_("mails"), default_value=10000),
                ],
            ),
        ),
    ],
)


def _parameter_valuespec_mailqueue_length():
    return Transform(
        mailqueue_params,
        forth=lambda old: not isinstance(old, dict) and {"deferred": old} or old,
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="qmail_queue_length",
        group=RulespecGroupCheckParametersApplications,
        is_deprecated=False,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_mailqueue_length,
        title=lambda: _("Number of mails in local/remote qmail queues"),
    ))
