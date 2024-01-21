# installs a flask package

package {'flask':
  ensure   => '2.1.0',
  path     => '/usr/bin'
  provider => 'pip3'
}
