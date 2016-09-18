<!DOCTYPE HTML>

<html xmlns="http://www.w3.org/1999/xhtml" lang="en-US" xml:lang="en-US">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>Wobka</title>
<meta name="description" content="Just another Open Designs template." />
<meta name="robots" content="noodp,noydir" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" id="child-theme-css" href="css/style.css" type="text/css" media="all" />
<link rel="stylesheet" id="responsive-main-css-css" href="css/responsive-main.min.css" type="text/css" media="all" />
<link rel="stylesheet" id="responsive-css-css" href="css/responsive.css" type="text/css" media="all" />
<link rel="stylesheet" id="tb_styles-css" href="css/tb-styles.min.css" type="text/css" media="all" />
<link rel="stylesheet" type="text/css" href="main2.css">
<script src="jquery-1.11.1.min.js" type="text/javascript"></script>
<script src="load-more.js" type="text/javascript"></script>

<script type="text/javascript" src="js/jquery.js"></script>

<script type="text/javascript">
  jQuery(window).scroll(function (event) {
	  	
		var top = jQuery('#popular-upcoming').offset().top - jQuery(document).scrollTop();;
		// what the y position of the scroll is
		var y = jQuery(this).scrollTop();
		// whether that's below the form
		if (y >= top)  {
		// if so, add the active class to popular-upcoming and remove from content
		jQuery('.page-nav-popular-posts').addClass('active');
		jQuery('.page-nav-top-posts').removeClass('active');
		} else {
		// otherwise remove it
		jQuery('.page-nav-popular-posts').removeClass('active');
		jQuery('.page-nav-top-posts').addClass('active');
	   }
  });
  
  jQuery(document).ready(function (){
  jQuery('#popular-scroll').click(function (){
            //jQuery(this).animate(function(){
                jQuery('html, body').animate({
                    scrollTop: jQuery('#popular-upcoming').offset().top
                     }, 2000);
            //});
        });
		
		jQuery('#feature-scroll').click(function (){
            //jQuery(this).animate(function(){
                jQuery('html, body').animate({
                    scrollTop: jQuery('#inner').offset().top
                     }, 2000);
            //});
        });
		  });
	  </script>
</head>

<body class="home blog header-full-width full-width-content" bgcolor="#EBECED">
  <div id="header">
  <div class="site-header">
    <h1 class="site-header-logo-container">
    <a href="/"><span class="image-replace">Welcome to Wobka!!!</span>
    <img src="images/bigg-logo.png" id="bigg-logo" alt="Welcome to Wobka!!!" /></a>
    </h1>
    </div>
  </div>
  <div id="wrap">
<div id="inner">
<div id="loader"></div>

<div class="wrap">
<div id="content-sidebar-wrap">
<div id="content" class="hfeed">

<!--?php require 'loadtablenew.php';
#echo "XML parser initialised";
?-->


</body>
</html>