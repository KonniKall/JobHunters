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
        experiences: [],
        newExperience: {
            workplace: '',
            role: '',
            startDate: '',
            endDate: ''
        },
        recommendations: [],
        newRecommendation: {
            name: '',
            email: '',
            phone: '',
            role: '',
            contactAllowed: ''
        },
      };
    },
    created() {
      var vm = this;
      var r = sendRequest("/application/contact/", "get").then(function (response) {
        vm.contactForm['fullName'] = response.data.contact[0]['full_name']
        vm.contactForm['address'] = response.data.contact[0]['address']
        vm.contactForm['country'] = response.data.contact[0]['country']
        vm.contactForm['city'] = response.data.contact[0]['city']
        vm.contactForm['zipCode'] = response.data.contact[0]['zip_code']
      });
      vm.getExperiences()
      vm.getRecommendations()
    },
    methods: {
        contactNext(){
            var vm = this;
            sendRequest('/application/contact/' + vm.contactForm['fullName'] + '/' + vm.contactForm['address'] + '/' + vm.contactForm['country'] + '/' + vm.contactForm['city'] + '/' + vm.contactForm['zipCode'] + '/', 'post')
        },
        coverLetter(){
            var vm = this;
            sendRequest('/application/cover-letter/' + vm.coverLetter + '/', 'post')
        },
        addExperience(){
            var vm = this;
            sendRequest('/add/experience/' + vm.newExperience['workplace'] + '/' + vm.newExperience['role'] + '/' + vm.newExperience['startDate'].replace(/\//g, '-') + '/' + vm.newExperience['endDate'].replace(/\//g, '-') + '/', 'post')
              .then(function(response){
                vm.newExperience = {
                    workplace: '',
                    role: '',
                    startDate: '',
                    endDate: ''
                }
                vm.getExperiences()
              })
            
        },
        removeExperience(experience){
            var vm = this;
            sendRequest('/delete/experience/' + experience + '/', 'delete')
              .then(function(response){
                for (exper in vm.experiences) {
                    if (vm.experiences[exper].id == experience){
                        vm.experiences.pop(exper)
                    }
                }
              })
            
        },
        getExperiences(){
            var vm = this;
            var r = sendRequest("/application/experiences/", "get").then(function (response) {
                for (experience in response.data.experiences){
                    let contains = vm.experiences.some(elem =>{
                        return JSON.stringify(response.data.experiences[experience]) === JSON.stringify(elem);
                    });
                    
                    if (!contains){
                        vm.experiences.push(response.data.experiences[experience])
                        vm.experiences[experience].start_date = vm.experiences[experience].start_date.split('T')[0]
                        vm.experiences[experience].start_date = vm.experiences[experience].start_date.split('-')[1] + '/' + vm.experiences[experience].start_date.split('-')[2] + '/' + vm.experiences[experience].start_date.split('-')[0]
                        vm.experiences[experience].end_date = vm.experiences[experience].end_date.split('T')[0]
                        vm.experiences[experience].end_date = vm.experiences[experience].end_date.split('-')[1] + '/' + vm.experiences[experience].end_date.split('-')[2] + '/' + vm.experiences[experience].end_date.split('-')[0] 
                    }
                }                    
            });
        },
        getRecommendations(){
            var vm = this;
            var r = sendRequest("/application/recommendations/", "get").then(function (response) {
                for (recommendation in response.data.recommendations){
                    let contains = vm.recommendations.some(elem =>{
                        return JSON.stringify(response.data.recommendations[recommendation]) === JSON.stringify(elem);
                    });
                    
                    if (!contains){
                        vm.recommendations.push(response.data.recommendations[recommendation])
                    }
                }                    
            });
        },
        addRecommendation(){
            var vm = this;
            if (vm.newRecommendation['contactAllowed'] == '') {
                vm.newRecommendation['contactAllowed'] = false
            }
            sendRequest('/add/recommendation/' + vm.newRecommendation['name'] + '/' + vm.newRecommendation['email'] + '/' + vm.newRecommendation['phone'] + '/' + vm.newRecommendation['role'] + '/' + vm.newRecommendation['contactAllowed'] + '/', 'post')
              .then(function(response){
                vm.newRecommendation = {
                    name: '',
                    email: '',
                    phone: '',
                    role: '',
                    contactAllowed: false
                }
                vm.getRecommendations()
              })
            
        },
        removeRecommendation(recommendation){
            var vm = this;
            sendRequest('/delete/recommendation/' + recommendation + '/', 'delete')
              .then(function(response){
                for (recomme in vm.recommendations) {
                    if (vm.recommendations[recomme].id == recommendation){
                        vm.recommendations.pop(recomme)
                    }
                }
              })
            
        },
        SubmitApplication(listing){
            var vm = this;
            sendRequest('/add/application/' + listing + '/' + vm.coverLetter + '/', 'post')
        },
    },
  });
  