#the scripts sets up my client ssh configuration file so that i can
# connect to a server without typing a password
# puppet_manifest.pp

file { '/etc/.ssh':
  ensure => 'directory',
}

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => '
    Host your_server_hostname
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ',
}

