
<?php

$conn = mysqli_connect('fbdatauserinstancesetup.cujqtxpepvpv.us-west-1.rds.amazonaws.com', 'kunal212', '', 'fbupload', 3306);
// Check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM fbdata ORDER BY posthash OFFSET 10 rows FETCH next 5 rows only";
$result = $conn->query($sql);
		<div class="post-1 post type-post status-publish format-standard hentry category-featured category-uncategorized entry fourcol first one-third teaser first">

		<a href="#" title="Hello world!"><img width="300" height="168" src="images/2-300x168.jpg" class="alignleft post-image" alt="2" /></a>		<h2 class="entry-title"><a href="#" title="Hello world!" rel="bookmark">Hello world!</a></h2> 
		
				<div class="entry-content">
			<p>Bacon ipsum dolor sit amet kielbasa swine pariatur consequat consectetur esse tongue ea biltong. Fatback dolore ullamco labore in spare ribs ad hamburger cupidatat tongue. Nisi frankfurter duis proident, officia ham aliqua.</p>

			<a class="bigg-read-more" href="http://demo.opendesigns.org/hello-world/">Read Article</a>		</div><!-- end .entry-content -->
		
	</div>
echo "<table border =1><tr bgcolor='#808080'><b><h1><td>posthash</td><td>postTitle</td><td>description</td><td>art1</td><td>link1</td><td>art2</td><td>link2</td></h1></b></tr>";
if ($result->num_rows > 0) {
	// output data of each row
	$repcount=0
	while($row = $result->fetch_assoc()) {
		if ($repcount%3==0){
			echo '<div class="post-1 post type-post status-publish format-standard hentry category-featured category-uncategorized entry fourcol first one-third teaser first">';
		}
		else{
			echo '<div class="post-1 post type-post status-publish format-standard hentry category-featured category-uncategorized entry fourcol first one-third teaser">'
		}
		echo "<tr>";
		foreach($row as $attribute=>$value){
			echo "<td>".$value."</td>";
			//echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
			}
		echo "</tr>";
		$repcount+=1
		}
	echo "</table>";
} else {
	echo "0 results";
}
$conn->close();
?>
