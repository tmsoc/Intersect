$(document).ready(function() {
    $("#room-link:first").addClass('active');
    $(".tab-pane:first").addClass('show active')

    $(':button').click(function() {
        const device_type = $(this).attr('name');
        if (device_type == "tv" || device_type == 'roku' || device_type == 'receiver') {
            const device_function = $(this).attr("value");

            $.ajax({
                data: {
                    device_type: device_type,
                    function: device_function
                },
                type: 'POST',
                url : '/UR/remote/transmit'
            }).done(function(data) {
                // do nothing
            }).fail(function() {
                console.log('Failed AJAX resonse')
            });
        };
    });
});