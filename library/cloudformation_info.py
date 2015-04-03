#!/usr/bin/python
# (c) 2015, James Sandlin <jamess@cloudcruiser.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

import boto.cloudformation
import shlex
import sys
import json
import ansible.utils as utils
import ansible.errors as errors
#class CloudFormationInfo(object):
   

region_name = None
stack_name = None

# read the argument string from the arguments file
args_file = sys.argv[1]
args_data = file(args_file).read()

# for this module, we're going to do key=value style arguments
# this is up to each module to decide what it wants, but all
# core modules besides 'command' and 'shell' take key=value
# so this is highly recommended

arguments = shlex.split(args_data)
for arg in arguments:
   # ignore any arguments without an equals in it
   if "=" in arg:
      (key, value) = arg.split("=")
      if key == "region":
         region_name = value
      elif key == "stack_name":
         stack_name = value
         
if region_name is None:
   print json.dumps({
                    "failed" : True,
                    "msg"    : "region_name is required"
                })
   sys.exit(1)
if stack_name is None:
   print json.dumps({
                    "failed" : True,
                    "msg"    : "stack_name is required"
                })
   sys.exit(1)

conn = boto.cloudformation.connect_to_region(region_name)  # or your favorite region
stacks = conn.describe_stacks(stack_name)
if len(stacks) == 1:
   stack = stacks[0]
   results = {}
   for output in stack.outputs:
       results[output.key] = output.value
   
   json_string = json.dumps(results)
   print json_string
   sys.exit(0)
else:
   print json.dumps({
                    "failed" : True,
                    "msg"    : "No data returned"
                })
   sys.exit(1)