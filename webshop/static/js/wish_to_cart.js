function addToCart () {
    console.log('JQuery -> OK');


        console.log('Add-to-cart => ok');

        const userId = $('#user_id').val();
        console.log('UserId -> '+ userId);

        if (userId == 'None') {
            alert('Для використання кошика Ви повинні авторизуватись');
            window.location = '/accounts/sign_in';
        } else {


            let productId = $(event.target).prev().val();
            let productName = $(event.target).parent().prev().find('h3').text();
            let productPrice = $(event.target).parent().prev().find('h4').text();

            console.log('product name -> '+ productName);
            console.log('product price -> '+ productPrice);
            console.log('product Id -> '+ productId);

                // AJAX
            $.ajax({
               url: '/items/ajax_cart',
               data: `uid=${userId}&pid=${productId}&price=${productPrice}`,
               success: (result) => {

                       console.log('AJAX Work OK -> ' +result.test_mess);
                       console.log(result.uid);
                       console.log(result.pid);
                       console.log(result.price);
                       console.log(result.create_mess);

                       $('#cart-count').text(result.count);
                       $('.cart-summary').find('h5').text(result.count + ' товарів обрано.');
                       $('.cart-summary').find('h4').text('ВАРТІСТЬ: ' +result.amount + ' грн.');
                   }
               });
             }

             };
function delWish () {
            let itemId = $(event.target).prev().val();
            $.ajax({
                url: '/items/ajax_del_wish',
                data: 'item_id=' + itemId,
                success: (result) => {
                    alert(result.report);
                    window.location = '/items/wish';
                }
            });
        }

function main() {
    addToCart().delay( 800 );
    delWish();
};

$(document).ready(() => {
    $('.products').on('click', '.add-to-cart-btn', (event) => {
        main();
        });
});