var stripe = Stripe('pk_test_51KTPH3Hhpp9pM3a6NdazrbU7xMfk6lYOMP1ug9mPmqiXowuRxn3W0Y7hHEbBKJDVUJh0LUgZqqkC61RHu1CshP9s00P2E0EUXX')
var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        lineHeight: '2.4',
        fontSize: '16px',
    }
};

var card = elements.create('card', {style:style})
card.mount('#card-element')

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error){
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    }else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert aler-info')
    }
})