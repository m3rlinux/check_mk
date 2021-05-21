#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# | Copyright m3rlinux 2021                    m3rlinux.it@gmail.com |
# +------------------------------------------------------------------+
#
# This file extend check snmp for Check_MK
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Author: Davide Gibilisco <m3rlinux.it@gmail.com>
# Damocles
# '.1.3.6.1.4.1.21796.3.4.1.1.3' => Check Name
# '.1.3.6.1.4.1.21796.3.4.1.1.2' => Check Value
# '.1.3.6.1.4.1.21796.3.4.1.1.4' => Alarm ON/OFF
# '.1.3.6.1.4.1.21796.3.4.1.1.6' => Pulse Counter

from .agent_based_api.v1 import *


def parse_damocles_in(string_table):
    section = []
    for line in string_table:
        alarm = int(line[3])
        if alarm != 0:
            section.append(line)

    return section


def discover_damocles_in(section):
    for line in section:
        yield Service(item=line[1])


def check_damocles_in(item, section):
    for id, check, state, enable, pulseCount in section:
        if check == item:
            yield Metric('pulseCount', int(pulseCount))
            if state == "0":
                yield Result(state=State.OK, summary=f"{check} Ok!")
            else:
                yield Result(state=State.CRIT, summary=f"{check} allarmato!")


register.snmp_section(
    name="damocles_in.py",
    detect=startswith(".1.3.6.1.2.1.1.1.0", "Damocles"),
    parse_function=parse_damocles_in,
    fetch=SNMPTree(
        base='.1.3.6.1.4.1.21796.3.4.1.1',
        oids=[
            OIDEnd(),
            '3',  # Sensor Name
            '2',  # Sensor Value
            '4',  # Sensor alarm State (ON/OFF)
            '6',  # Sensor Pulse Counter
        ],
    ),
)

register.check_plugin(
    name="damocles_in.py",
    service_name="%s",
    discovery_function=discover_damocles_in,
    check_function=check_damocles_in,
)
