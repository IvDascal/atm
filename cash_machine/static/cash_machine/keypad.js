$( document ).ready(function() {
    var number = $('input.num');

    number.keydown(function(event) {
        return false;
    });

    var digit_counter = 0;
    $('button.digit').click(function() {
        if (digit_counter < 16 ) {
            number.val(number.val() + this.value);
            digit_counter += 1;
            if (digit_counter % 4 == 0 && digit_counter < 16) {
                number.val(number.val() + "-");
            }
        }
    });

    $('button.clear').click(function() {
        number.val('');
        digit_counter = 0;
    });
});