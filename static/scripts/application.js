function sendRequest(url, method, data) {
    var r = axios({
      method: method,
      url: url,
      data: data,
      xsrfCookieName: "csrftoken",
      xsrfHeaderName: "X-CSRFToken",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    });
    return r;
  }
  
  var application = new Vue({
    delimiters: ["[[", "]]"],
    el: "#application",
    data() {
      return {};
    },
    created() {
      var vm = this;
      var r = sendRequest("", "get").then(function (response) {
        console.log("working");
      });
    },
    methods: {
        contactNext(fullName, address, country, city, zipCode){
            //contactForm = this.$route.params.contact_form
            console.log('w2')
            //this.contactForm = JSON.parse(document.getElementById('json_data').textContent)
            console.log(fullName)
            console.log(address)
            console.log(country)
            console.log(city)
            console.log(zipCode)
            var vm = this;
            sendRequest('/application/contact/' + fullName + '/' + address + '/' + country + '/' + city + '/' + zipCode + '/', 'post')
              .then(function(response){
                console.log(response)
                vm.sortby_data = sortby
                vm.opps['opportunities'] = response.data.opportunities
                //vm.opportunities.push(response.data.opportunities);
              })
          },
    },
  });
  