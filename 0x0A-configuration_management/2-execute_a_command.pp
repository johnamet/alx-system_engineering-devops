# executes a kill command to kill a process

exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  refreshonly => true,
}
