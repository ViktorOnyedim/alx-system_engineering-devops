# This manifest kills a process named 'killmenow'
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}
