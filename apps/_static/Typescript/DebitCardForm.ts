function DebitCardForm(){
    let debit_card_input = document.getElementById('debit-card') as HTMLInputElement;
    let debit_card_form = document.getElementById('debit-card-form') as HTMLFormElement;
    let form_card_number = document.getElementById('card-number') as HTMLInputElement
    let form_card_expiry = document.getElementById('cc-expiry-input') as HTMLInputElement
    let form_card_cvv = document.getElementById('card-cvv') as HTMLInputElement
    if (debit_card_input.checked){
        debit_card_form.classList.remove('hidden');
        form_card_number.required = true;
        form_card_expiry.required = true;
        form_card_cvv.required = true;
    }else {
        debit_card_form.classList.add('hidden');
        form_card_number.required = false;
        form_card_expiry.required = false;
        form_card_cvv.required = false;
    }
}

DebitCardForm();

document.getElementById('payment-methods').addEventListener('change', function (){
    DebitCardForm();
})