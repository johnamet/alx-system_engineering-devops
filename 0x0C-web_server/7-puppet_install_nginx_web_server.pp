# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start and enable Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

# Redirect /redirect_me with a 301 Moved Permanently
nginx::resource::location { '/redirect_me':
  ensure    => present,
  location  => '/redirect_me',
  vhost     => 'default',
  www_root  => '/var/www/html',
  content   => 'return 301 https://www.tutorialspoint.com/http/http_methods.htm;',
}

