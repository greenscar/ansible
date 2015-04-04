# requires outbound port 80 (yum), 22 (ssh), & 443 (pip) open.
# For pip to talk to pypi.python.org, I opened 23.235.39.223/32
sudo yum install -y python-devel
sudo yum install -y telnet
sudo yum install -y git
sudo yum-config-manager --enable epel
sudo pip install ansible --upgrade
sudo pip install boto
sudo pip install markupsafe

# Now for git hookup
ssh-keygen -f ~/.ssh/id_rsa -t rsa -N ''
# Add the generated key to the repo
mkdir ~/workspaces
cd ~/workspaces
git clone git@github.com:/sandlinjames/ansible.git
cd ansible

git config --global user.email "jamess@cloudcruiser.com"
git config --global user.name "james"
                                                                               100% 1692     1.7KB/s   00:00    

export AWS_ACCESS_KEY_ID='AKIAI6NRUKYA36Y5L2LA'
export AWS_SECRET_ACCESS_KEY='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'
export ANSIBLE_HOST_KEY_CHECKING=False
# Then back on ec2 instance:











# From my box, put the ssh key here.
| => scp ~/.ssh/bravo-infra.pem ec2-user@52.5.41.21:/home/ec2-user/.ssh
bravo-infra.pem       
ansible-playbook -i envs/localhost ./cc-elasticsearch.yml -vvvv --private-key=~/.ssh/bravo-infra.pem 


BastionHost AMI
The AMI ID is ami-a61626ce