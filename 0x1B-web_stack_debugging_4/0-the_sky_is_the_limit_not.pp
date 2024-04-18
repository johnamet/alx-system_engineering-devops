# The puppet file fixes server requests by increasing
# the worker processes in the server conf file

exec { 'fix--for-nginx':
command => "sed -i 's/worker_processes 4/worker_processes 7/g' /etc/nginx/nginx.conf; sudo service nginx restart",
unless  => "grep 'worker_processes 7' /etc/nginx/nginx.conf",
path    => ['/bin', '/usr/bin']
}
