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
      return {
        contactForm: {
            fullName: '',
            address: '',
            country: '',
            city: '',
            zipCode: ''
        },
        coverLetter: '',
        experiences: []
      };
    },
    created() {
      var vm = this;
      var r = sendRequest("/application/contact/", "get").then(function (response) {
        console.log(response.data.contact)
        console.log(response.data.contact[0]['full_name'])
        vm.contactForm['fullName'] = response.data.contact[0]['full_name']
        vm.contactForm['address'] = response.data.contact[0]['address']
        vm.contactForm['country'] = response.data.contact[0]['country']
        vm.contactForm['city'] = response.data.contact[0]['city']
        vm.contactForm['zipCode'] = response.data.contact[0]['zip_code']
      });
      var r = sendRequest("/application/experiences/", "get").then(function (response) {
        console.log(response.data.experiences)
        console.log(vm.experiences)
        for (experience in response.data.experiences){
            //console.log(experience.role)
            //experience['start_date'] = experience['start_date'].split("T")
            vm.experiences.push(response.data.experiences[experience])
        }
        console.log(vm.experiences)
        
      });
    },
    methods: {
        contactNext(){
            //contactForm = this.$route.params.contact_form
            console.log('w2')
            //this.contactForm = JSON.parse(document.getElementById('json_data').textContent)
            var vm = this;
            sendRequest('/application/contact/' + vm.contactForm['fullName'] + '/' + vm.contactForm['address'] + '/' + vm.contactForm['country'] + '/' + vm.contactForm['city'] + '/' + vm.contactForm['zipCode'] + '/', 'post')
              .then(function(response){
                console.log(response)
              })
        },
        coverLetter(){
            var vm = this;
            sendRequest('/application/cover-letter/' + vm.coverLetter + '/', 'post')
              .then(function(response){
                console.log(response)
              })
        },
    },
  });
  