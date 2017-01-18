Note to future self: unfortunately, packer does not support comments in templates as JSON does not understand comments. The following was cut from the template, from the builders::

    {
      "type": "null",
      "ssh_host": "127.0.0.1",
      "ssh_port": 2022,
      "ssh_username": "hisparc",
      "ssh_private_key_file": "../../.vagrant/machines/vagrant/virtualbox/private_key"
    }

and from the provisioners::

    {
      "type": "ansible-local",
      "playbook_file": "local.yml",
      "playbook_dir": "../../provisioning/",
      "inventory_file": "local_inventory"
    }

I originally inserted this to let packer provision the machine. Then ``vagrant up`` was *much* faster! However, building and testing the vpn machine resulted in problems. That machine should *not* include the public database software! Maybe packer should build multiple images, but I don't have the time to look into that now.

To look at the original file::

   $ git show df689a4:packer/CentOS6/template.json

Signing off, DF.
