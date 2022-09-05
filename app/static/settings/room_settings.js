function query_attached_devices(room_id) {

    if (typeof room_id !== 'undefined') {

        $.ajax({
            data: {
                rm_id: room_id
            },
            type: 'POST',
            url: '/settings/rooms/get-devices'
        }).done(function(data) {
            $('#roku_list').empty();
            $('#ir_list').empty();
    
            let text = '';
            for (let r in data.rks) {
                text += '<dt class="col-sm-3">' + data.rks[r]['name'] + '</dt>'
                text += '<dd class="col-sm-9">' + data.rks[r]['ip'] + '</dd>'
            }
            $('#roku_list').html(text);
            
            text = '';
            for (let r in data.irs) {
                text += '<dt class="col-sm-3">' + data.irs[r]['name'] + '</dt>'
                text += '<dd class="col-sm-9">' + data.irs[r]['ip'] + '</dd>'
            }
            $('#ir_list').html(text);
    
        }).fail(function() {
            console.log('Failed AJAX response')
        });
    };
};


$(document).ready(function() {
    let last_id = $('#detail_select').find(":selected").val();
    query_attached_devices(last_id);

    $('#detail_select').click(function() {
        const selection = $('#detail_select').find(":selected").val();
        if (selection != last_id) {
            query_attached_devices(selection)
            last_id = selection;
        };
    });
});
