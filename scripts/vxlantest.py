#!/bin/env python
"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Simon Hart"
__email__ = "sihart@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

# To get a logger for the script
import logging
import json
# To build the table at the end
from tabulate import tabulate

# Needed for aetest script
from ats import aetest
from ats.log.utils import banner

# Genie Imports
from genie.conf import Genie
from genie.abstract import Lookup

from vxlanops import Vxlan
# import the genie libs
from genie.libs import ops # noqa

# Get your logger for your script
log = logging.getLogger(__name__)


###################################################################
#                  COMMON SETUP SECTION                           #
###################################################################

class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    # CommonSetup have subsection.
    # You can have 1 to as many subsection as wanted

    # Connect to each device in the testbed
    @aetest.subsection
    def connect(self, testbed):
        genie_testbed = Genie.init(testbed)
        self.parent.parameters['testbed'] = genie_testbed
        device_list = []
        for device in genie_testbed.devices.values():
            log.info(banner(
                "Connect to device '{d}'".format(d=device.name)))
            try:
                device.connect()
            except Exception as e:
                self.failed("Failed to establish connection to '{}'".format(
                    device.name))

            device_list.append(device)

        # Pass list of devices the to testcases
        self.parent.parameters.update(dev=device_list)

###################################################################
#                     TESTCASES SECTION                           #
###################################################################

class Vxlan_Up_And_Working(aetest.Testcase):
    """ This is user Testcases section """

    @ aetest.test
    def learn_vxlan(self):
        """ Sample test section. Only print """

        self.all_vxlan_info = {}
        for dev in self.parent.parameters['dev']:
            log.info(banner("Gathering VXLAN Information from {}".format(
                dev.name)))
            #abstract = Lookup.from_device(dev)
            vxlan = Vxlan(dev)
            vxlan.learn()
            self.all_vxlan_info[dev.name] = vxlan.info

        log.info(self.all_vxlan_info)

    @ aetest.test
    def check_vxlan(self):
        failed_dict = {}
        mega_tabular = []
        for device, vni in self.all_vxlan_info.items():
            for intf, props in vni.items():
                state = props.get('VNIstate')
                if state:
                    tr = []
                    tr.append(device)
                    tr.append(props['VNIstate'])
                    tr.append(props['VNI'])
                    tr.append(props['Peer-IP'])
                    if state == 'Up':
                        tr.append('Passed')
                    else:
                        failed_dict[device] = {}
                        failed_dict[device] = props['VNIstate']

                        tr.append('Failed')
                    mega_tabular.append(tr)
        log.info(tabulate(mega_tabular,
                          headers=['Device', 'State',
                                   'VNI','Peer', 'Pass/Fail'],
                          tablefmt='orgtbl'))
            # log.info(dev)
            # log.info(state)
        if failed_dict:
            log.error(json.dumps(failed_dict, indent=3))
            self.failed("A device has VXLAN interface down")

        else:
            self.passed("VXLAN is up")







# #####################################################################
# ####                       COMMON CLEANUP SECTION                 ###
# #####################################################################

# This is how to create a CommonCleanup
# You can have 0 , or 1 CommonCleanup.
# CommonCleanup can be named whatever you want :)
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsections as wanted
    # here is an example of 1 subsection

    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__':  # pragma: no cover
    aetest.main()