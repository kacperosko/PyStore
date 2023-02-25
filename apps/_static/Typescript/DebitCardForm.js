function DebitCardForm() {
    var debit_card_input = document.getElementById('debit-card');
    var debit_card_form = document.getElementById('debit-card-form');
    var form_card_number = document.getElementById('card-number');
    var form_card_year = document.getElementById('card-year');
    var form_card_month = document.getElementById('card-month');
    var form_card_cvv = document.getElementById('card-cvv');
    if (debit_card_input.checked) {
        debit_card_form.classList.remove('hidden');
        form_card_number.required = true;
        form_card_year.required = true;
        form_card_month.required = true;
        form_card_cvv.required = true;
    }
    else {
        debit_card_form.classList.add('hidden');
        form_card_number.required = false;
        form_card_year.required = false;
        form_card_month.required = false;
        form_card_cvv.required = false;
    }
}
document.getElementById('payment-methods').addEventListener('change', function () {
    DebitCardForm();
});
