import boto.cloudformation
conn = boto.cloudformation.connect_to_region('us-east-1')  # or your favorite region
stacks = conn.describe_stacks('BravoInfrastructure-integration')
if len(stacks) == 1:
    stack = stacks[0]
else:
   sys.exit(0)
    # Raise an exception or something because your stack isn't there
for output in stack.outputs:
    print('%s=%s (%s)' % (output.key, output.value, output.description))