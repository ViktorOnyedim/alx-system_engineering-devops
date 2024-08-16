# Puppet manuscript to correct typo in wp-settings.php

# Replace instances of 'phpp' with 'php' within the file
exec { 'fix-typos-in-wp-settings':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => ['/bin', '/usr/bin'],
}
