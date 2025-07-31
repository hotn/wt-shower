#!/usr/local/bin/python3.7

# -*- coding: utf-8 -*-

import sys
import piplates.RELAYplate as RELAY

num = int(sys.argv[1])

RELAY.relayTOGGLE(3,num)

