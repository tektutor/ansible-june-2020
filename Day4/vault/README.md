You may execute the playbook as shown below

In case, you prefer typing the vault password manually, you may try the below
ansible-playbook vault-playbook.yml --ask-vault-pass

In case, you prefer automatically supplying the vault password then
  Create ansible.cfg file, you may check the ansible.cfg content in this git repo
  This ansible.cfg file will help ansible in locating the vault_password_file. From there ansible will pick the 
  vault password and perform the requested activitiy.

Regarding ansible-vault

1. Create a vault protected file
   ansible-vault create contacts.yml
   
2. Edit an existing vault protected file
   ansible-vault edit contacts.yml
   
3. Decrypt an existing vault protected file
   ansible-vault decrypt contacts.yml
   
4. Encrypt a plain file using ansible vault
   ansible-vault encrypt contacts.yml
   
For all the above commands, you will prompted for vault password and you need to manually them. In case ansible.cfg file
has the vault_password_file property defined then, ansible will not prompt for any password.
