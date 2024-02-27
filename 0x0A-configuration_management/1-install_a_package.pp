# Uses Puppet to install flask from pip3.
# Requirements
# - Install flask
# - Version must be 2.1.0

package {'python3-pip':
  ensure => 'installed',
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}
