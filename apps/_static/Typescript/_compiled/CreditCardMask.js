var ccNumberInput = document.getElementById('card-number'), ccNumberPattern = /^\d{0,16}$/g, ccNumberSeparator = " ", ccNumberInputOldValue, ccNumberInputOldCursor, ccExpiryInput = document.getElementById('cc-expiry-input'), ccExpiryPattern = /^\d{0,4}$/g, ccExpirySeparator = "/", ccExpiryInputOldValue, ccExpiryInputOldCursor, mask = function (value, limit, separator) {
    var output = [];
    for (var i = 0; i < value.length; i++) {
        if (i !== 0 && i % limit === 0) {
            output.push(separator);
        }
        output.push(value[i]);
    }
    return output.join("");
}, unmask = function (value) { return value.replace(/[^\d]/g, ''); }, checkSeparator = function (position, interval) { return Math.floor(position / (interval + 1)); }, ccNumberInputKeyDownHandler = function (e) {
    var el = e.target;
    ccNumberInputOldValue = el.value;
    ccNumberInputOldCursor = el.selectionEnd;
}, ccNumberInputInputHandler = function (e) {
    var el = e.target, newValue = unmask(el.value), newCursorPosition;
    if (newValue.match(ccNumberPattern)) {
        newValue = mask(newValue, 4, ccNumberSeparator);
        newCursorPosition =
            ccNumberInputOldCursor - checkSeparator(ccNumberInputOldCursor, 4) +
                checkSeparator(ccNumberInputOldCursor + (newValue.length - ccNumberInputOldValue.length), 4) +
                (unmask(newValue).length - unmask(ccNumberInputOldValue).length);
        el.value = (newValue !== "") ? newValue : "";
    }
    else {
        el.value = ccNumberInputOldValue;
        newCursorPosition = ccNumberInputOldCursor;
    }
    el.setSelectionRange(newCursorPosition, newCursorPosition);
    highlightCC(el.value);
}, highlightCC = function (ccValue) {
    var ccCardType = '', ccCardTypePatterns = {
        amex: /^3/,
        visa: /^4/,
        mastercard: /^5/,
        disc: /^6/,
        genric: /(^1|^2|^7|^8|^9|^0)/
    };
    for (var cardType in ccCardTypePatterns) {
        if (ccCardTypePatterns[cardType].test(ccValue)) {
            ccCardType = cardType;
            break;
        }
    }
    var activeCC = document.querySelector('.cc-types__img--active'), newActiveCC = document.querySelector(".cc-types__img--".concat(ccCardType));
    if (activeCC)
        activeCC.classList.remove('cc-types__img--active');
    if (newActiveCC)
        newActiveCC.classList.add('cc-types__img--active');
}, ccExpiryInputKeyDownHandler = function (e) {
    var el = e.target;
    ccExpiryInputOldValue = el.value;
    ccExpiryInputOldCursor = el.selectionEnd;
}, ccExpiryInputInputHandler = function (e) {
    var el = e.target, newValue = el.value;
    newValue = unmask(newValue);
    if (newValue.match(ccExpiryPattern)) {
        newValue = mask(newValue, 2, ccExpirySeparator);
        el.value = newValue;
    }
    else {
        el.value = ccExpiryInputOldValue;
    }
};
ccNumberInput.addEventListener('keydown', ccNumberInputKeyDownHandler);
ccNumberInput.addEventListener('input', ccNumberInputInputHandler);
ccExpiryInput.addEventListener('keydown', ccExpiryInputKeyDownHandler);
ccExpiryInput.addEventListener('input', ccExpiryInputInputHandler);
