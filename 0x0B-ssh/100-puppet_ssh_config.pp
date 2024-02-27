# To setup a ssh configuration file

file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  content => "
Host *
  PreferredAuthentications publickey
  IdentityFile ~/.ssh/school
  ",
}

file { '/root/.ssh':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0700'
}
