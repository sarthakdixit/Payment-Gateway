let paypal_checkout = document.getElementById("paypal-checkout-button");

paypal_checkout.addEventListener("click", () => {
    paypalGetToken();
});

const paypalGetToken = async () => {
    let urlencoded = new URLSearchParams();
    urlencoded.append("grant_type", "client_credentials");
    let config = {
        method : 'POST',
        headers : {
            "Content-type": "application/x-www-form-urlencoded",
            "Access-Control-Allow-Credentials": true,
            Authorization :`Basic ${btoa(paypal_client_key + ":" + paypal_secret_key)}`
        },
        body : urlencoded
    }
    try{
        let result = await fetch('https://api-m.sandbox.paypal.com/v1/oauth2/token', config)
        let res = await result.json();
        paypalMakePayment(res.access_token);
    }catch(e){
        alert(e);
    }
}

const paypalMakePayment = async (access_token) => {
    let body = JSON.stringify({
        intent: "sale",
        payer: {
          payment_method: "paypal",
        },
        transactions: [
          {
            amount: {
              total: parseInt(product_price),
              currency: "INR",
            },
          },
        ],
        note_to_payer: product_name,
        redirect_urls: {
          return_url: `${base_url}/success`,
          cancel_url: `${base_url}/cancel`,
        },
    });
    let config = {
        method : 'POST',
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${access_token}`,
        },
        body : body
    }
    try{
        let result = await fetch('https://api.sandbox.paypal.com/v1/payments/payment', config);
        let res = await result.json();
        let links = res.links;
        let approval = links.find((data) => data.rel == "approval_url").href;
        window.location.assign(approval);
    }catch(e){
        alert(e);
    }
}