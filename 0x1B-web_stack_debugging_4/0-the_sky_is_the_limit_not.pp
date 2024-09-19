# This Puppet manifest increases the amount of traffic an Nginx server can handle by adjusting the file limit and ensuring Nginx is running with the correct settings.

# Ensure the ulimit is increased for Nginx
file_line { 'increase_nginx_ulimit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT=4096',
  match => '^ULIMIT=',
  notify => Service['nginx'],  # Ensure Nginx restarts if the file is changed
}

# Manage the Nginx service
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
}
