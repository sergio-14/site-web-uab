(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Back to top button
    


    // Sidebar Toggler
    $('.sidebar-toggler').click(function () {
        $('.sidebar, .content').toggleClass("open");
        return false;
    });


    


    


    // Chart Global Color
   // Chart.defaults.color = "#6C7293";
    //Chart.defaults.borderColor = "#000000";


    // Worldwide Sales Chart
   

    // Salse & Revenue Chart
   
    


    

    // Single Bar Chart
    


  


    // Doughnut Chart
   

    
})(jQuery);

