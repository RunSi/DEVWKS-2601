# To run the job:
# easypy vxlancheckjob.py -html_logs -no_archive -testbed_file <testbed_file.yaml>
# Description: This job file shows the Vxlan State Checker
import os
from ats.easypy import run

def main():
    # Find the location of the script in relation to the job file
    vxlan_tests = os.path.join('./vxlantest.py')
    # Execute the testscript
    run(testscript=vxlan_tests)