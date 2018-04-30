Digital Rebar Provision Role
=========

This role installs and configures Digital Rebar Provision.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Sample group_vars

```
provision_options:
  disable-dhcp: yes

provision_preferences:
  defaultBootEnv: local
  unknownBootEnv: discovery

provision_files_bootenvs_path: dr-provision/bootenvs
provision_files_templates_path: dr-provision/templates

provision_bootenvs_files:
  - shift-labs-debian-9-install.yaml

provision_templates_files:
  - shift-labs-net-seed.tmpl.yaml
  - shift-labs-select-kickseed.tmpl.yaml

provision_profiles:
  - Available: true
    Description: shift-labs profile for setting the access-keys and access-ssh-root-mode parameters
    Errors: []
    Meta:
      color: blue
      icon: key
    Name: shift-labs-root-access
    Params:
      access-keys:
        root: ssh-rsa ...
      access-ssh-root-mode: without-password
    ReadOnly: true
    Validated: true

provision_machines:
  - Name: host01.shift-labs.com
    Address: 10.10.10.10
    BootEnv: debian-9-install
    Description: host01.shift-labs.com host
  - Name: host02.shift-labs.com
    Address: 10.10.10.11
    BootEnv: debian-9-install
    Description: host02.shift-labs.com host
  - Name: host03.shift-labs.com
    Address: 10.10.10.12
    BootEnv: debian-9-install
    Description: host03.shift-labs.com host
  - Name: host04.shift-labs.com
    Address: 10.10.10.13
    BootEnv: debian-9-install
    Description: host04.shift-labs.com host
  - Name: host05.shift-labs.com
    Address: 10.10.10.14
    BootEnv: debian-9-install
    Description: host05.shift-labs.com host
  - Name: host06.shift-labs.com
    Address: 10.10.10.15
    BootEnv: debian-9-install
    Description: host06.shift-labs.com host
  - Name: host07.shift-labs.com
    Address: 10.10.10.16
    BootEnv: debian-9-install
    Description: host07.shift-labs.com host
  - Name: host08.shift-labs.com
    Address: 10.10.10.17
    BootEnv: debian-9-install
    Description: host08.shift-labs.com host
  - Name: host09.shift-labs.com
    Address: 10.10.10.18
    BootEnv: debian-9-install
    Description: host09.shift-labs.com host
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
- hosts: servers
  roles:
     - { role: dr-provision }
```

Testing Locally
---------------


To test on a local centos system with git and ansible already installed, do the following:

* Use git to clone the repo as ansible-role-dr-provision in a directory.
  * e.g. `git clone https://github.com/stanchan/ansible-role-dr-provision`
* cp drp-*.yml .

To install, do:

* `ansible-playbook drp-install.yml -i "localhost," -c local`

To clean, do:

* `ansible-playbook drp-clean.yml -i "localhost," -c local`


License and Author
------------------

* Author:: Stan Chan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

