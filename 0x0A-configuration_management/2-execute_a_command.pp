# Uses Puppet to  create a manifest that kills a process named killmenow.
# Requirements:
# - Must use the exec Puppet resource
# - Must use pkill

exec { 'start_killmenow':
  command   => '/bin/sleep 10 &',
  path      => '/bin',
  creates   => '/tmp/killmenow',
  logoutput => true,
}

exec { 'kill_killmenow':
  command   => 'pkill -f killmenow',
  path      => '/usr/bin/bin:/bin',
  require   => Exec['start_killmenow'],
  logoutput => true,
}

file { '/tmp/killmenow':
  ensure => 'absent',
}
