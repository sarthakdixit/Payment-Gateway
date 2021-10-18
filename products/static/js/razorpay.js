let razorpay_checkout = document.getElementById("razorpay-checkout-button");

razorpay_checkout.addEventListener("click", async () => {
    let config = {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({name: product_name, price: parseInt(product_price)*100})
    }
    try{
        let result = await fetch(`${base_url}/razorpay/checkout`, config);
        let res = await result.json();
        createCheckout(res.response.id);
    }catch(e){
        console.log(e);
    }
})

const createCheckout = (order_id) => {
    var options = {
        "key": razorpay_key,
        "amount": product_price,
        "currency": "INR",
        "name": product_name,
        "description": "Test Transaction",
        "order_id": order_id,
        "handler": function (response){
            alert(response.razorpay_payment_id);
            alert(response.razorpay_order_id);
            alert(response.razorpay_signature)
        }
    };
    
    var rzp1 = new Razorpay(options);
    rzp1.open();
    e.preventDefault();
}