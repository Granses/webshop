$(document).ready(() => {

    console.log('JQuery -> OK');

    $('.products').on('click', '.add-to-cart-btn', (event) => {
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

//        let oldCartCount = parseInt($('#cart-count').text());
//        let newCartCount = oldCartCount +1;
//        $('#cart-count').text(newCartCount);
//        $('.cart-summary').find('h5').text(newCartCount + ' товарів обрано');
//
//        let oldCartPrice = $('.cart-summary').find('h4').text().split(':')[1];
//        oldCartPrice = parseFloat(oldCartPrice);
//        let newCartPrice = oldCartPrice + productPrice;
//        $('.cart-summary').find('h4').text('ВАРТІСТЬ: ' +newCartPrice + 'грн.');
    });

});