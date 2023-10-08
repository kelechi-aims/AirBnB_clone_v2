# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { '/data':
  ensure => directory,
}

file { '/data/web_static':
  ensure => directory,
}

file { '/data/web_static/releases':
  ensure => directory,
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test':
  ensure => directory,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  content => 'Holberton School',
}

# Create symbolic link (remove if exists and recreate)
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
  require => File['/data/web_static/releases/test/index.html'],
}

# Set ownership to ubuntu user and group recursively
exec { 'set_permissions':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/usr/bin',
  user    => 'root',
  group   => 'root',
}

# Update Nginx configuration to serve content from /data/web_static/current/
file_line { 'nginx_alias_config':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'location /hbnb_static { alias /data/web_static/current/; }',
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/data/web_static/current'],
}
