$(document).ready(function(){
    $("#room-link:first").addClass('active');
    $(".tab-pane:first").addClass('show active')

    $(':button').click(function(){
        const button_name = $(this).attr("name");
        const button_attribute = $(this).attr("value")
        console.log(button_name + " " + button_attribute);
    });
});