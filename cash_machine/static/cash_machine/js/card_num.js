$( document ).ready(function() {
    var card_number = $('input.card_num');

    card_number.keydown(function(event) {
        return false;
    });

    var digit_counter = 0;
    $('button.digit').click(function() {
        if (digit_counter < 16 ) {
            card_number.val(card_number.val() + this.value);
            digit_counter += 1;
            if (digit_counter % 4 == 0 && digit_counter < 16) {
                card_number.val(card_number.val() + "-");
            }
        }
    });

    $('button.clear').click(function() {
        card_number.val('');
        digit_counter = 0;
    });

    var pin = $('input.pin');

    pin.keydown(function(event) {
        return false;
    });

    $('button.digit').click(function() {
        if (pin.val().length < 4) {
            pin.val(pin.val() + this.value)
        }
    });

});