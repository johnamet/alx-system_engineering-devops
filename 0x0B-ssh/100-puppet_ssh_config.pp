#the scripts sets up my client ssh configuration file so that i can
# connect to a server without typing a password

file_line {'Config Identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}

file_line {'Log passless auth':
  path => '~/.ssh/school',
  line => 'PasswordAuthentication no'
}
