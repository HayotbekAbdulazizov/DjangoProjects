function AddToCart(product_id){
    let qty = document.getElementById('product_qty').value;
    qty = parseInt(qty)
    let d = {
        product_id:product_id,
        count:qty,
        }
    let data = JSON.stringify(d)
	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      var data = JSON.parse(this.responseText);

    }else{
      console.log('not yet')

      }
    }
    var url = "/cart/add/"
    xhttp.open("GET", url+`?data=${data}`, true);
    xhttp.send();
}
