$( document ).ready(function() {
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
