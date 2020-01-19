;(function($) {
    "use strict";

    var nav_offset_top = $('.search_area').height();
    /*-------------------------------------------------------------------------------
	  Navbar
	-------------------------------------------------------------------------------*/

  	//* Navbar Fixed
    var nv = function navbarFixed(){
        if ( $('.search_area').length ){
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top ) {
                    $(".search_area").addClass("sb_fixed");
                } else {
                    $(".search_area").removeClass("sb_fixed");
                }
            });
        };
    };
    nv()





})(jQuery)
