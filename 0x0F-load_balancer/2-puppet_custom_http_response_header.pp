#!/usr/bin/env bash
# Automate the configuration of servers
# with a custom response header

# File: 2-puppet_ustom_http_response_header.pp

#define server group

node group 'hbnb_servers' {
    members => ['246179-web-01', '246179-web-02']
}

#Package and service management for Nginx
package { 'nginx' }
service { 'nginx' }
    ensure => running,
    enable => true

# Create a directory for the custom configuration file (optional)
file { '/etc/nginx/conf.d/custom.conf':
  ensure  => directory,
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
}

# Define the custom configuration file
file { '/etc/nginx/conf.d/custom.conf/custom.conf':
  ensure => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => <<EOF
  server {
    listen       80;
    server_name  _;

    location / {
      root   /var/www/html;
      index  index.html index.htm;

      # Add "Hello World!" to index.html
      add_before_body "<p>Hello World!</p>";

      # Add custom header
      add_header X-Served-By $hostname;
    }
  }
EOF
}

# Include the custom configuration file in the main Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => present,
  line   => /^include +(.*)$/,
  insert_before => eof,
  content => "include /etc/nginx/conf.d/custom.conf/custom.conf;",
}

# Reload Nginx to apply changes
exec { 'reload_nginx':
  command => '/etc/init.d/nginx reload',
  unless  => '/etc/init.d/nginx status | grep -q running',  # Only reload if Nginx is running
}

# Schedule a resource refresher to ensure configuration stays in sync
schedule { 'refresh_config':
  ensure => present,
  minute  => 0,
}
