(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space
M.AutoInit();

function Search(value){
      console.log(value)
	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
            var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            let data = JSON.parse(this.responseText)
            document.querySelector('.search-block').style.display = 'block';
            if(value === ''){
                document.querySelector('.search-block').style.display = 'none';
            }

            let title = document.querySelector('#movie-title')
            let div = '<div>'
            console.log(data['data'])
            for(let i = 0; i < data['data'].length; i++){
                let t = data['data'][i].title
                let s = data['data'][i].slug
                div += `<a href="/detail/${s}" class="collection-item">${t}</a>`
            }
            div += '</div>';
            title.innerHTML = div
        }else{
          console.log('not yet')
          }
      }

    var url = "/search/"
    xhttp.open("GET", url+`?data=${value}`, true);
    xhttp.send();
}
