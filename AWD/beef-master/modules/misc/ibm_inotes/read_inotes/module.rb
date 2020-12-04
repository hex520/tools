#
#   Copyright (c) 2006-2020 Wade Alcorn wade@bindshell.net
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
class Read_inotes < BeEF::Core::Command
 def self.options
    return [
      {'type' => 'label', 'html' => 'Provide unid to retrieve details of a Note:' },
      {'type' => 'textfield', 'name' => 'unid', 'ui_label' => 'notes unid', 'value' => '1'}
    ]
  end 
  def post_execute
    save({'result' => @datastore['result']})
  end

end