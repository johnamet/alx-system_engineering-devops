# executes a kill command to kill a process

exec { 'killmenow':
  command     => 'pkill killmenow',
  refreshonly => true,
}
