file_line { 'Append to a file':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no\nIdentityFile ~/.ssh/holberton'
}
