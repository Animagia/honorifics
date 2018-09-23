#!/usr/bin/env python3
import sys
sys.path.insert(0, '../honorifics')

from honorifics.subtitle_file_helper import SubStationFileHelper
from honorifics.substation_utils import EventDialogueTiming

lines = sys.stdin.readlines()

helper = SubStationFileHelper(lines)
event_dialogue = EventDialogueTiming(helper.event_format)

sys.stdout.write(''.join(lines[:helper.pos_start_dialogue]))

for index in range(helper.pos_start_dialogue, len(lines)):
    sys.stdout.write(event_dialogue.apply_timing_offset(lines[index]))
