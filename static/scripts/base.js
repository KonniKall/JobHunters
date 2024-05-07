function sendRequest(url, method, data){
    var req = axios({
      method: method,
      url: url,
      data: data,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    return req
}

var profile = new Vue({
    delimiters: ["[[", "]]"],
    el: "#profile",
    data() {
        return{
     
        }

    },
    created(){
        var vm = this;
        var req = sendRequest('', 'get')
        .then(function(response){
          console.log('working')
        })
        
      },
      methods: {
        
      },
  })