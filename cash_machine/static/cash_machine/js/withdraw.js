$( document ).ready(function() {
    $('table.keypad  tbody:last-child').append(
        '<tr class="key-row">' +
            '<td class="key-cell" colspan="3">' +
                '<a class="btn btn-danger btn-block btn-lg" href="/" role="button">' + 'Выход' + '</a>' +
            '</td>' +
        '</tr>'
    )

    var amount = $('input.amount');

    amount.keydown(function(event) {
        return false;
    });

    $('button.digit').click(function() {
            amount.val(amount.val() + this.value)
    });

    $('button.clear').click(function() {
        amount.val('');
    });

});
