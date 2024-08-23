# fix nginx to accept and serve more requests

#exec {'modify max open files limit setting':
#  command => 'sed -i "s/15/4096" /etc/default/nginx && sudo nginx restart',
#  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
#}

exec { 'modify max open files limit setting':
  command => 'sed -i "s/#worker_rlimit_nofile.*/worker_rlimit_nofile 4096;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

exec { 'modify worker processes':
  command => 'sed -i "s/worker_processes.*/worker_processes auto;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

exec { 'modify worker connections':
  command => 'sed -i "s/worker_connections.*/worker_connections 4096;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

exec { 'restart nginx':
  command => 'sudo systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  require => [Exec['modify max open files limit setting'], Exec['modify worker processes'], Exec['modify worker connections']],
}

