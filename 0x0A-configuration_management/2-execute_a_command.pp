exec { 'kill_killmenow':
  command => 'pkill killmenow',
  refreshonly => true,
}
