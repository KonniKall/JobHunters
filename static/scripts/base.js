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

var header = new Vue({
  delimiters: ["[[", "]]"],
  el: "#header",
  data() {
    return {};
  },
  created() {
    var vm = this;
    var r = sendRequest("", "get").then(function (response) {
      console.log("working");
    });
  },
  methods: {},
});
