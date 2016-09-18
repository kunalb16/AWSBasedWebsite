<?php

//echo "Inside loadtable";

$conn = mysqli_connect('fbdatauserinstancesetup.cujqtxpepvpv.us-west-1.rds.amazonaws.com', 'kunal212', '', 'fbupload', 3306);
// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM fbtrendingdata ORDER BY posttime DESC LIMIT 10";
$result = $conn->query($sql);
//echo $result->num_rows;
echo "<table><tr bgcolor='#00FFFF'><b><h1><th>News</th><th>Article A</th><th>Article B</th></h1></b></tr>";
if ($result->num_rows > 0) {
	// output data of each row
	while($row = $result->fetch_assoc()) {
		echo "<tr>";
		echo "<td>";
		echo "<b><div class='titletext'>".$row['postTitle']."</b></div>";
		echo "<div class='descriptiontext'>".$row['description']."</div>";
		echo "</td>";
		echo "<td><a href='".$row['link1']."' target='_blank'><div class='myButton'><div class ='fbpic'>"."<img src="."kunalbansalftp/1".$row['posthash'].".png>"."</div>";
		echo "<div class='linktext'>".$row['art1']."<b>&nbsp;&nbsp;&nbsp;&nbsp;<u>+More</u>...</b>"."</div></div></a></td>";
		//echo "<td><div class ='fbpic'>"."<img src="."kunalbansalftp/2".$row['posthash'].".png>"."</div>";
		echo "<td><a href='".$row['link2']."' target='_blank'><div class='myButton'><div class ='fbpic'>"."<img src="."kunalbansalftp/2".$row['posthash'].".png>"."</div>";
		echo "<div class='linktext'>".$row['art2']."<b>&nbsp;&nbsp;&nbsp;&nbsp;<u>+More</u>...</b>"."</div></div></a></td>";		//echo "<td><div class ='fbpic'>"."<img src="."kunalbansalftp/2".$row['posthash'].".png>"."</div>";
		//echo "<div class ='fbpic'><a href =".$row['link2'].">"."<div class='linktext'>".$row['art2']."</div></a></div></td>";
		//echo "<td><a href =".$row['link2'].">".$row['art2']."</a>"."</td>";
		/*
		foreach($row as $attribute=>$value){
			if ($attribute=="link1" or $attribute=="link2"){continue;}
			echo "<td>".$value."</td>";
			//echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
			}
		*/
		echo "</tr>";
		}
	echo "</table>";
} else {
	echo "0 results";
}
$conn->close();
?>
