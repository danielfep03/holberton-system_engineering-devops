# Manifest that kills a process
exec { 'pkill':
command => 'pkill -x killmenow',
path    => '/usr/bin'
}
