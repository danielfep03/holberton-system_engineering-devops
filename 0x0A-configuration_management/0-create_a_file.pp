# Create a file in /tmp
file { '/tmp/holberton':
    ensure   => 'present'
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0774',
    content => 'I love Puppet'
}
