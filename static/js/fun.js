$(document).ready(function(){

	onmousemove = function(e){
		$(".curs-circ").animate({left: e.clientX-4, top: e.clientY-4}, 10, "linear");
		$(".curs-c-outl").animate({left: e.clientX-9, top: e.clientY-9}, 16, "swing");
	}

}); 