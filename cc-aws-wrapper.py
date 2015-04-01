import boto.cloudformation
import ansible.runner
import ansible.playbook
import ansible.inventory
conn = boto.cloudformation.connect_to_region('us-east-1')  # or your favorite region
stacks = conn.describe_stacks('BravoInfrastructure-integration')

stack_data = {}
if len(stacks) == 1:
    stack = stacks[0]
else:
   sys.exit(0)
    # Raise an exception or something because your stack isn't there
print "----------------"
for output in stack.outputs:
   stack_data[output.key] = output.value
   print('%s=%s (%s)' % (output.key, output.value, output.description))
   
print "----------------"
"""
Bastion=52.5.67.47 (IP Address of the Bastion host)
EnvironmentName=integration (Name of deployment environment)
InstanceSecurityGroup=sg-5285eb36 (The ID of a VPC Security Group that has ingress access to the NAT instance.)
PrivateSubnet1=subnet-d84629af (A private VPC subnet ID.)
PrivateSubnet2=subnet-8e2792a5 (A private VPC subnet ID. Must be in a different AZ than PrivateSubnet1)
PublicSubnet1=subnet-c74629b0 (A public VPC subnet ID.)
PublicSubnet2=subnet-8d2792a6 (A public VPC subnet ID. Must be in a different AZ than PublicSubnet1)
VPCAvailabilityZone1=us-east-1a (The AZ that (Public|Private)Subnet1 is launched into.)
VPCAvailabilityZone2=us-east-1d (The AZ that (Public|Private)Subnet2 is launched into.)
"""
#pb = ansible.playbook.PlayBook(
#   playbook="cloudcruiser-es.yml",
#   inventory="envs/localhost",
#   check=True
#)
#pb.vars = extra_vars
#pb.run()
#runner = ansible.runner.Runner)
hosts = ["localhost ansible_connection=local"]
inv = ansible.inventory.Inventory(hosts)
args = {'VPCId':stack_data['VPCId'],'private_subnet_1':stack_data['PrivateSubnet1'],'private_subnet_2':stack_data['PrivateSubnet2']}
runner = ansible.runner.Runner(
   is_playbook=True,
   inventory = inv,
   extra_vars=args
   )
#get_facts = runner.run()   
#print get_facts
print "ansible-playbook -i envs/localhost ./cloudcruiser-es.yml -vvvv -e \"vpcid=" + stack_data['VPCId'] \
      + " private_subnet_1=" + stack_data['PrivateSubnet1'] \
      + " private_subnet_2=" + stack_data['PrivateSubnet2'] + "\""
