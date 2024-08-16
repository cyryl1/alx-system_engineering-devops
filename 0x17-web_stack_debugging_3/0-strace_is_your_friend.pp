# Ensure the /var/www/html directory exists and has the correct permission
file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Optionally, ensure that Apache is running
service { 'apache2':
  ensure => 'running',
  enable => true,
}
