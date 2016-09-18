//variable initialization 
var current_page	=	0;
var loading			=	false;
var oldscroll		=	0;
$(document).ready(function(){
    $.ajax({
        'url':'loadtablemore.php',
        'type':'post',
        'data': 'p='+current_page,
        success:function(data){
            //var data    =   $.parseJSON(data);
            //alert(data);
            $('#content').append(data);
            //$jQuery(data).appendTo('#content');
            current_page++;
        }
    });
    
	$(window).scroll(function() {
		if( $(window).scrollTop() > oldscroll ){ //if we are scrolling down
			if( ($(window).scrollTop() + $(window).height() >= $(document).height() ) ) {
				   if( ! loading ){
						loading = true;
						$('#content').addClass('loading');
						$.ajax({
							'url':'loadtablemore.php',
							'type':'post',
							'data': 'p='+current_page,
							success:function(data){
								//var data	=	$.parseJSON(data);
								$alert($(window).scrollTop());
								$alert($(window).height());
								$alert($(document).height());
								$('#content').append(data);
								//$(data.html).hide().appendTo('#content').fadeIn(1000);
								current_page++;
								$('#content').removeClass('loading');
								loading = false;
							}
						});	
				   }
			}
		}
	});
	
});