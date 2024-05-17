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
  
  var deleteJobListing = new Vue({
    delimiters: ["[[", "]]"],
    el: "#deleteJobListing",
    data() {
      return {};
    },
    created() {
      var vm = this;
      var r = sendRequest("", "get").then(function (response) {
      });
    },
    methods: {
        deleteListing(jobListing){
            var vm = this;
            sendRequest('/delete/job-listing/' + jobListing + '/', 'delete')
            
        },
    },
  });
  