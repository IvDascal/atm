$( document ).ready(function() {
    var pin = $('input.pin');

    pin.keydown(function(event) {
        return false;
    });

    $('button.digit').click(function() {
        if (pin.val().length < 4) {
            pin.val(pin.val() + this.value)
        }
    });

    $('button.clear').click(function() {
        card_number.val('');
    });

});
