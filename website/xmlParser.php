<?php
require 'handlesql.php';
#echo "SQL Handled";

libxml_use_internal_errors(true);


$xml = simplexml_load_file("upload.xml") or die("Error: Cannot create object");
if ($xml === false) {
    echo "Failed loading XML: ";
    foreach(libxml_get_errors() as $error) {
        echo "<br>", $error->message;
    }
} else {
	foreach ($xml as $key) {
		
		# code...
    $h1=$key->heading;
    $h1=$mysqli->real_escape_string($h1);
    $d1=$key->Description;
    $d1=$mysqli->real_escape_string($d1);
	$sql = "INSERT INTO `u456292348_fb`.`posts` (`heading`, `Description`) VALUES ('$h1','$d1');";
    echo $sql;
    #$sql=str_replace("'","\'",$sql)
    #$sql=str_replace('"','\"',$sql)
    #$sql=str_replace("'","\'",$sql)
    #$sql=str_replace("'","\'",$sql)
    #$sql=$mysqli->real_escape_string($sql);
	#echo $key->link2;
    $h2=$key->heading1;
    $h2=$mysqli->real_escape_string($h2);
    $l2=$key->link1;
    $l2=$mysqli->real_escape_string($l2);
    $h3=$key->heading2;
    $h3=$mysqli->real_escape_string($h3);
    $l3=$key->link2;
    $l4=$mysqli->real_escape_string($l4);
	$sql2 = "INSERT INTO `u456292348_fb`.`articles` (`heading1`, `link1`,`heading2`, `link2`) VALUES ('$h2','$l2','$h3','$l3');";
    echo $sql2;
    #$sql2=str_replace("'","\'",$sql2)
    #$sql2=str_replace('"','\"',$sql2)
    #$sql2=$mysqli->real_escape_string($sql2);
if ($mysqli->query($sql) === TRUE) {
    #echo "New record created successfully";
} else {
    echo "Errorwwww: " . $sql . "<br>" . $mysqli->error;
}

if ($mysqli->query($sql2) === TRUE) {
    #echo "New record created successfully";
} else {
    echo "Errorwwwww: " . $sql2 . "<br>" . $mysqli->error;
}
sleep(0);
	}



$mysqli->close();
    #print_r($xml);
}
?> 