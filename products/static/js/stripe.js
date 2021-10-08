let stripe_checkout = document.getElementById("stripe-checkout-button");

stripe_checkout.addEventListener("click", () => {
    let config = {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({name: product_name, price: parseInt(product_price)*100})
    }
    
    fetch(`${base_url}/stripe/create-checkout-session`, config)
        .then(res => {
            return res.json();
        })
        .then(session => {
            console.log(session)
            return stripe.redirectToCheckout({sessionId:session.id});
        })
        .then(result => {
            if(result.error){
                alert(result.error.message);
            }
        })
})