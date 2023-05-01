# This manifest makes changes to a configuration file

file_line { 'Turn off password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no'
  replace => true,
}

file_line { 'Declare an identity file':
  ensure => 'present',
  path   => '~/.ssh/school',
  line   => '   IdentityFile ~/.ssh/school',
  replace = true,
}
