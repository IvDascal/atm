$( document ).ready(function() {
    $('table.keypad  tbody:last-child').append(
        '<tr class="key-row">' +
            '<td class="key-cell" colspan="3">' +
                '<a class="btn btn-danger btn-block btn-lg" href="/" role="button">' + 'Выход' + '</a>' +
            '</td>' +
        '</tr>'
    )

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
        pin.val('');
    });

});
