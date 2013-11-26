#http://chrisadams.me.uk/2010/05/10/setting-up-a-centos-base-box-for-development-and-testing-with-vagrant/
#kernel source is needed for vbox additions

date > /etc/vagrant_box_build_time

yum -y install gcc bzip2 make kernel-devel-`uname -r`
#yum -y update
#yum -y upgrade

yum -y install gcc-c++ zlib-devel openssl-devel readline-devel sqlite3-devel
yum -y erase wireless-tools gtk2 hicolor-icon-theme avahi freetype bitstream-vera-fonts
yum -y clean all

#Installing vagrant keys
mkdir /home/vagrant/.ssh
chmod 700 /home/vagrant/.ssh
cd /home/vagrant/.ssh
wget --no-check-certificate 'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -O authorized_keys
chown -R vagrant /home/vagrant/.ssh

#Installing the virtualbox guest additions
VBOX_VERSION=$(cat /home/vagrant/.vbox_version)
cd /home/vagrant
wget -c http://download.virtualbox.org/virtualbox/$VBOX_VERSION/VBoxGuestAdditions_$VBOX_VERSION.iso
mount -o loop VBoxGuestAdditions_$VBOX_VERSION.iso /mnt
sh /mnt/VBoxLinuxAdditions.run
umount /mnt

rm VBoxGuestAdditions_$VBOX_VERSION.iso

sed -i "s/^.*requiretty/#Defaults requiretty/" /etc/sudoers
sed -i "s/^\(.*env_keep = \"\)/\1PATH /" /etc/sudoers

# Add the puppet group.
#/usr/sbin/groupadd puppet

#poweroff -h

#Add user hisparc with sudo access
/usr/sbin/adduser hisparc
echo "hisparc"|passwd --stdin hisparc
echo "hisparc        ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

#Installing vagrant keys for hisparc user
mkdir /home/hisparc/.ssh
chmod 700 /home/hisparc/.ssh
cd /home/hisparc/.ssh
wget --no-check-certificate 'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -O authorized_keys
chown -R hisparc /home/hisparc/.ssh

exit
