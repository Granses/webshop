$(document).ready(() =>{

    console.log('Del_item -> Start');

    $('.del-btn').click((event) =>{
        let itemId = $(event.target).prev().val();
        $.ajax({
            url: '/items/ajax_del_item',
            data: 'item_id=' + itemId,
            success: (result) => {
                alert(result.report);
                window.location = '/items';
            }
        });
    });

});