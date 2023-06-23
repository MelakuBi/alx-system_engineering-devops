#using pkill
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/',
  returns => [0,1],
}
