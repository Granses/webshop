$(document).ready(() => {

    console.log('JQueryWISH -> OK');

    $('.add-to-wishlist').on('click',  (event) => {
    console.log('Add-to-wishlist => OK');


    console.log(event.target)

    const userId = $('#user_id').val();


    if (userId == 'None') {
        alert('Щоб переглянути обрані товари Ви повинні авторизуватись');
        window.location = '/accounts/sign_in';
    } else {
        const wishId = $(event.target).parent().parent().parent().find('.add-to-cart').find('input').val()
        console.log('WishId => '+ wishId);

        $.ajax({
            url: '/items/ajax_wish',
            data: `uid=${userId}&wid=${wishId}`,
            success: (result) => {

                console.log('AJAX Work OK -> ' +result.test_mess);
                console.log(result.uid);
                console.log(result.wid);
                $('#wish-count').text(result.count);
            }
        });



//    let oldWishCount = parseInt($('#wish-count').text());
//    let newWishCount = oldWishCount +1;
//    $('#wish-count').text(newWishCount);
        };
    });
});
