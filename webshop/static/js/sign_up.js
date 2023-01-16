function example() {
     //1 - Вікно повідомлення
    alert('Базове вікно повідомлень');

     //2 - Консоль розробника
    console.log('Повідомлення сценарію для JS-консолі');

     //3 - Вікно введення даних
    let client = prompt('Як вас звуть?');
    console.log('Будемо знайомі, ' + client + '!');

     //4 - Вікно підтвердження вибору
    let choice = confirm('Ви впевнені?');
    if (choice == true) {
        window.location = 'https://www.ukr.net';
    } else {
        alert('ну і не треба!')
    }
}


$(document).ready(() => {

    console.log('JQuery -> OK');

    let result1 = false; // -результат валідації логіна
    let result2 = false; // -результат валідації 1 пароля
    let result3 = false; // -результат валідації 2 пароля
    let result4 = false; // -результат валідації емайлу

    // 1 валідація логіна:
    $('#login').blur(() => {
        console.log('#login-blur -> OK');
        let loginX = $('#login').val();
        console.log('loginX -> ' + loginX);

        let loginRe = /^[a-zA-Z][a-zA-Z0-9_\-\.]{5,15}$/;
        if (loginRe.test(loginX)) {
            // перевірка зайнятості логіну
            $.ajax({
                url: '/accounts/ajax_reg',
                data: 'login=' + loginX,
                success: (result) => {
                    console.log('AJAX -> OK');
                    console.log(result.message);
                    if (result.message === 'зайнятий') {
                        $('#login_err').text('Логін зайнятий!');
                        result1 = false;
                    } else {
                        $('#login_err').text('');
                        result1 = true;
                    }
                }
            });
       } else {
            $('#login_err').text('Помилка формату логіна ');
            result1 = false;
       }
    });

    // 2 Валідація паролю 1
    $('#pass1').blur(() => {
        console.log('#pass1-blur -> OK');
        let pass1x = $('#pass1').val();
        console.log('pass1x -> ' + pass1x);

        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_\-\.]{6,}$/;
        if (passRe.test(pass1x)) {
            $('#pass1_err').text('');
            result2 = true;
       } else {
            $('#pass1_err').text('Помилка формату пароля. Від 6-ти символів. Хочаб одна буква і цифра! ');
            result2 = false;
       }
    });

    // 3 Валідація паролю 2

    $('#pass2').blur(() => {
        console.log('#pass2-blur -> OK');
        let pass1x = $('#pass1').val();
        let pass2x = $('#pass2').val();

        if (pass1x == pass2x) {
            $('#pass2_err').text('');
            result3 = true;
       } else {
            $('#pass2_err').text('Введені паролі не співпадають!');
            result3 = false;
       }
    });

    // 1 валідація логіна:
    $('#email').blur(() => {
        console.log('#email-blur -> OK');
        let emailX = $('#email').val();
        console.log('emailX -> ' + emailX);

        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        if (emailRe.test(emailX)) {
            // перевірка зайнятості email
            $.ajax({
                url: '/accounts/ajax_email',
                data: 'email=' + emailX,
                success: (result) => {
                    console.log('AJAX -> OK');
                    console.log(result.message);
                    if (result.message === 'зайнятий') {
                        $('#email_err').text('Користувач з таким Email вже існує!');
                        result4 = false;
                    } else {
                        $('#email_err').text('');
                        result4 = true;
                    }
                }
            });
       } else {
            $('#email_err').text('Помилка формату email! ');
            result4 = false;
       }

       $('#submit').click(() => {
            if (result1 && result2 && result3 && result4) {
                $('#form1').attr('onsubmit', 'return true');
            } else {
                $('#form1').attr('onsubmit', 'return false');
                alert('форма містить некоректні дані!\nВідправка даних заблокована!');
            }
       })
    });


})