# Ensure that the Apache service is installed, running, and enabled to start on boot
package { 'apache2':
  ensure => 'installed',
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
}

# Ensure the /var/www/html directory exists and has the correct permission
file { '/var/www/html':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure the index.html file exists with the correct content and permissions
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<html><head><title>My Webpage</title></head><body><h1>Welcome to my Apache Server</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure Apache is configured correctly (optional configuration example)
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => 'file',
  content => template('apache/000-default.conf.erb'),  # Use a template to manage the Apache config
  notify  => Service['apache2'],  # Restart Apache if the config changes
}

# Enable the site (if necessary)
exec { 'enable_site':
  command => 'a2ensite 000-default',
  onlyif  => 'test ! -L /etc/apache2/sites-enabled/000-default.conf',
  notify  => Service['apache2'],
}

# Ensure Apache is reloaded if there are any changes to the configuration
exec { 'relaod_apache':
  command     => '/usr/sbin/apache2ctl graceful',
  refreshonly => true,
  subscribe   => File['/etc/apache2/sites-available/000-default.conf'],
}
