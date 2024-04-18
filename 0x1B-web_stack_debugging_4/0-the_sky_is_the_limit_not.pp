exec { 'fix_failed_reqs':
   command => "sed -i 's/worker_processes 4/worker_processes 7/g' /etc/nginx/nginx.conf",
   unless  => "grep 'worker_processes 7' /etc/nginx/nginx.conf",
   path    => ['/bin', '/usr/bin']
}
