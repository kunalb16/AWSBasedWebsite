
<?php
$mysqli = new mysqli("mysql.serversfree.com", "u456292348_fb", "", "u456292348_fb");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
echo $mysqli->host_info . "\n";
?>
