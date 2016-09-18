<?php
require('db.php');
if( isset( $_POST['p'] ) )
{

	$page					=	intval( $_POST['p'] );
	$current_page			=	$page - 1;
	$records_per_page		=	12; // records to show per page
	$start					=	$current_page * $records_per_page;
	$query					=	"SELECT * from messages LIMIT $start, $records_per_page";
	$result					=	mysqli_query($db,$query);
	$html					=	"";
	while ( $row = mysqli_fetch_array($result,MYSQLI_ASSOC) ) 
	{
		$html	.='<li>'.$row['name'].': '.$row['message'].'</li>';
	}

	//returning data
	$data			=	array(
							'html'			=>	$html
						);
	echo json_encode($data);

}
?>