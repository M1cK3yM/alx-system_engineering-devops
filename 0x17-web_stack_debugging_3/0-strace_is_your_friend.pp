exec { 'Fix wordpress site':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => ['/usr/local/bin', '/bin', '/usr/bin'],
  onlyif   => 'grep -q ".phpp" /var/www/html/wp-settings.php',
}

