# This Puppet manifest increases the amount of traffic an Nginx server can handle by adjusting the file limit and ensuring Nginx is running with the correct settings.

# Ensure the ulimit is increased for Nginx
exec { 'increase_nginx_ulimit':
  path       => '/usr/local/bin/:/bin/'
  command    => 'sed -i "s/15/4096/" /etc/default/nginx',
}

# restart the Nginx service
-> exec { 'nginx-restart':
  command    => 'nginx-restart',
  path       => '/etc/init.d/',
}
