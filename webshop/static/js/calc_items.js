const doCalculate = () => {
    let checkedCells = $('.check:checked');
    let totalPrice = 0;
    let selItemsList = '';

    for (let cell of checkedCells) {
        let parent = $(cell).parent().parent();
        totalPrice += parseFloat($(parent).find('td.price_cell').text());
        selItemsList += $(parent).find('td.id_cell').text() + ',';
    }
    selItemsList += totalPrice;

    console.log(`totalPrice = ${totalPrice}`);
    console.log(`selItemsList = ${selItemsList}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн.`);
    $('#bill-btn').attr('href', `/orders/bill/${selItemsList}`);
};


$(document).ready(() =>{

    console.log('calc items - start');
    doCalculate();

    $('.check').click((event) => {
        console.log('INPUT_CHECK -> Click');
        doCalculate();
    });
});