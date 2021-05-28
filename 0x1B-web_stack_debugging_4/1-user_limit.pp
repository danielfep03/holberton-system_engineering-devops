# Fix server number of open files
exec {
  '/usr/bin/env sed -i s/holberton/daniel/ /etc/security/limits.conf':
}
