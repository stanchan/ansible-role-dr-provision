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
  - shift-labs-net-post-install.sh.tmpl.yaml
  - shift-labs-net-seed.tmpl.yaml
  - shift-labs-part-scheme-default.tmpl.yaml
  - shift-labs-select-kickseed.tmpl.yaml

provision_profiles:
  - Available: true
    Description: Shift Labs profile for k8s cluster parameters
    Errors: []
    Meta:
      color: blue
      icon: key
    Name: shift-labs-k8s-install
    Params:
      access-keys:
        root: ssh-rsa ...
      access-ssh-root-mode: without-password
      dns-domain: shift-labs.com
      local-repo: true
      ntp-servers:
        - time.google.com
        - time2.google.com
        - time3.google.com
        - time4.google.com
      package-repositories:
        - tag: "centos-7-install" # Every repository needs a unique tag.
          # A repository can be used by multiple operating systems.
          # The usual example of this is the EPEL repository, which
          # can be used by all of the RHEL variants of a given generation.
          os:
            - "centos-7"
          # If installSource is true, then the URL points directly
          # to the location we should use for all OS install purposes
          # save for fetching kernel/initrd pairs from (for now, we will
          # still assume that they will live on the DRP server).
          # When installSounrce is true, the os field must contain a single
          # entry that is an exact match for the bootenv's OS.Name field.
          installSource: true
          # For redhat-ish distros when installSource is true,
          # this URL must contain distro, component, and arch components,
          # and as such they do not need to be further specified.
          url: "http://mirrors.kernel.org/centos/7/os/x86_64"
        - tag: "centos-7-everything"
          # Since installSource is not true here,
          # we can define several package sources at once by
          # providing a distribution and a components section,
          # and having the URL point at the top-level directory
          # where everything is housed.
          # DRP knows how to expand repo definitions for CentOS and
          # ScientificLinux provided that they follow the standard
          # mirror directory layout for each distro.
          os:
            - centos-7
          url: "http://mirrors.kernel.org/centos"
          distribution: "7"
          components:
            - atomic
            - centosplus
            - cloud
            - configmanagement
            - cr
            - dotnet
            - extras
            - fasttrack
            - opstools
            - os
            - paas
            - rt
            - sclo
            - storage
            - updates
        - tag: "debian-9-install"
          os:
            - "debian-9"
          installSource: true
          # Debian URLs always follow the same rules, no matter
          # whether the OS install flag is set.  As such,
          # you must always also specify the distribution and
          # at least the main component, although you can also
          # specify other components.
          url: "http://mirrors.kernel.org/debian"
          distribution: stretch
          components:
            - main
            - contrib
            - non-free
        - tag: "debian-9-backports"
          os:
            - "debian-9"
          url: "http://mirrors.kernel.org/debian"
          distribution: stretch-updates
          components:
            - main
            - contrib
            - non-free
        - tag: "debian-9-security"
          os:
            - "debian-9"
          url: "http://security.debian.org/debian-security/"
          securitySource: true
          distribution: stretch/updates
          components:
            - contrib
            - main
            - non-free
      zero-hard-disks-for-os-install: true
    ReadOnly: true
    Validated: true
  - Available: true
    Description: shift-labs profile for setting the access-keys and access-ssh-root-mode parameters
    Errors: []
    Meta:
      color: blue
      icon: key
    Name: shift-labs-debian-install
    Params:
      access-keys:
        root: ssh-rsa ...
      access-ssh-root-mode: without-password
      dns-domain: shift-labs.com
      local-repo: true
      ntp-servers:
        - time.google.com
        - time2.google.com
        - time3.google.com
        - time4.google.com
      zero-hard-disks-for-os-install: true
    ReadOnly: true
    Validated: true

provision_machines:
  - Name: host01.shift-labs.com
    Address: 10.10.10.10
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host01.shift-labs.com host
  - Name: host02.shift-labs.com
    Address: 10.10.10.11
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host02.shift-labs.com host
  - Name: host03.shift-labs.com
    Address: 10.10.10.12
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host03.shift-labs.com host
  - Name: host04.shift-labs.com
    Address: 10.10.10.13
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host04.shift-labs.com host
  - Name: host05.shift-labs.com
    Address: 10.10.10.14
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host05.shift-labs.com host
  - Name: host06.shift-labs.com
    Address: 10.10.10.15
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host06.shift-labs.com host
  - Name: host07.shift-labs.com
    Address: 10.10.10.16
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host07.shift-labs.com host
  - Name: host08.shift-labs.com
    Address: 10.10.10.17
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host08.shift-labs.com host
  - Name: host09.shift-labs.com
    Address: 10.10.10.18
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host09.shift-labs.com host
  - Name: host10.shift-labs.com
    Address: 10.10.10.19
    BootEnv: debian-9-install
    Profiles:
      - shift-labs-debian-install
    Description: host10.shift-labs.com host
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

