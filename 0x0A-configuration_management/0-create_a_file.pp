# Create a file in /tmp
file { '/tmp/holberton':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0774',
    content => 'I love Puppet'
}
