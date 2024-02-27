# This Puppet manifest creates a file in 
# /tmp named 'school' with the following properties:
# - File path is /tmp/school
# - File permission is 0744
# - File owner is www-data
# - File group is www-data
# - File contains the text 'I love Puppet python'

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet python\n",
}
