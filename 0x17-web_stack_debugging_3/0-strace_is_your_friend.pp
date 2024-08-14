exec { 'Fix wordpress site':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => '/usr/local/bin/:/bin/'
}
