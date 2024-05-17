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
  
  var filter = new Vue({
    delimiters: ["[[", "]]"],
    el: "#container",
    data() {
      return {
        search: {
          jobName: '',
          companyName: ''
        },
        orderBy: 'due_date',
        filters: {
            category: '',
            alreadyApplied: false,
        },
        jobListings: [],
        users: {}
      };
    },
    created() {
      var vm = this;
      vm.getJobListings()
    },
    methods: {
      getJobListings(){
        var vm = this;
        jobName = vm.search['jobName']
        if (jobName == '') {
          jobName = 'none'
        }
        companyName = vm.search['companyName']
        if (companyName == '') {
          companyName = 'none'
        }
        orderBy = vm.orderBy
        if (orderBy == '') {
          orderBy = 'none'
        }
        category = vm.filters['category']
        if (category == '') {
          category = 'all'
        }
        alreadyApplied = vm.filters['alreadyApplied']
        if (alreadyApplied == '') {
          alreadyApplied = false
        }

        var r = sendRequest("/filter/" + jobName + '/' + companyName+ '/' + orderBy+ '/' + category + '/' + alreadyApplied + '/', "get")
         .then(function (response) {
            vm.users = response.data.user_list

            for (jobListing in response.data.job_listings){
              //console.log(response.data.job_listings[jobListing]['user_id'])
              vm.jobListings.push(response.data.job_listings[jobListing])
              vm.jobListings[jobListing].username = vm.users[response.data.job_listings[jobListing]['user_id']]
              vm.jobListings[jobListing].start_date = vm.jobListings[jobListing].start_date.split('T')[0]
              vm.jobListings[jobListing].start_date = vm.jobListings[jobListing].start_date.split('-')[1] + '/' + vm.jobListings[jobListing].start_date.split('-')[2] + '/' + vm.jobListings[jobListing].start_date.split('-')[0] 
              vm.jobListings[jobListing].due_date = vm.jobListings[jobListing].due_date.split('T')[0]
              vm.jobListings[jobListing].due_date = vm.jobListings[jobListing].due_date.split('-')[1] + '/' + vm.jobListings[jobListing].due_date.split('-')[2] + '/' + vm.jobListings[jobListing].due_date.split('-')[0]
            } 
            console.log(vm.jobListings)
          });
        },

      filterChange(){
        var vm = this;
        //vm.search['jobName'] = jobName
        const timeoutId = window.setTimeout(() => {}, 0);
        for (let id = timeoutId; id >= 0; id -= 1) {
          window.clearTimeout(id);
        }

        setTimeout(() => {
          vm.jobListings = []
          vm.getJobListings()
        }, 500);
        }
        
    },
  });
  