Please replace authorized_keys file with your own public key

In case you wish to create rsa key pair, you may use 

 ssh-keygen

and accept all default values by hitting enter.

Later once your key pair is created, you may  copy the public keys as shown  below

git clone https://github.com/tektutor/ubuntu-ansible.git

cd ubuntu-ansible.git

cp /root/.ssh/id_rsa.pub authorized_keys

docker build -t tektutor/ansible-ubuntu .
