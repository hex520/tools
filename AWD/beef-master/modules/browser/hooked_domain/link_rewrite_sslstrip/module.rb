#
# Copyright (c) 2006-2020 Wade Alcorn - wade@bindshell.net
# Browser Exploitation Framework (BeEF) - http://beefproject.com
# See the file 'doc/COPYING' for copying permission
#
class Link_rewrite_sslstrip < BeEF::Core::Command
  
  def post_execute
    save({'result' => @datastore['result']})
  end
  
end