<?php

//echo "Inside loadtable";
$page=intval( $_POST['p'] );
$conn = mysqli_connect('fbdatauserinstancesetup.cujqtxpepvpv.us-west-1.rds.amazonaws.com', 'kunal212', '', 'fbupload', 3306);
// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

$offsetvalue=$page*12;
$sql = "SELECT * FROM fbtrendingdata ORDER BY posttime DESC LIMIT ".$offsetvalue." , 12";
$result = $conn->query($sql);

//echo $result->num_rows;
//echo "<table><tr bgcolor='#00FFFF'><b><h1><th>News</th><th>Article A</th><th>Article B</th></h1></b></tr>";
if ($result->num_rows > 0) {
	// output data of each row
	$repcount=0;
	while($row = $result->fetch_assoc()) {
		if ($repcount%3==0){
			echo '<div class="post-1 post type-post status-publish format-standard hentry category-featured category-uncategorized entry fourcol first one-third teaser first">';
		}
		else{
			echo '<div class="post-1 post type-post status-publish format-standard hentry category-featured category-uncategorized entry fourcol one-third teaser">';
		}
		echo '<h2 class="entry-title">'.$row['postTitle'].'</a></h2>';
		echo '<div class="entry-content"><p>'.$row['description']."</p>";
		echo "<div class='fbarticle'><p><div class ='fbpic'>"."<img src="."kunalbansalftp/1".$row['posthash'].".png>"."</div><div class='linktext'><p><b>".$row['art1'];
		$hostname=parse_url($row['link1'],PHP_URL_HOST);
		echo "</b><br/><u>".$hostname."</u>";
		echo '<a class="bigg-read-more" href="'.$row['link1'].'" target="_blank">Read Article</a></div></p></div>';
		echo "<div class='fbarticle'><p><div class ='fbpic'>"."<img src="."kunalbansalftp/2".$row['posthash'].".png>"."</div><div class='linktext'><p><b>".$row['art2'];
		$hostname=parse_url($row['link2'],PHP_URL_HOST);
		echo "</b><br/><u>".$hostname."</u>";
		echo '<a class="bigg-read-more" href="'.$row['link2'].'" target="_blank">Read Article</a></div></p></div>';
		echo '</div></div>';
		$repcount+=1;
		}
//	echo "</table>";
} else {
	echo "0 results";
}
$conn->close();
?>
