function sendRequest(url, method, data){
    var r = axios({
      method: method,
      url: url,
      data: data,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    return r
}

var sign_up = new Vue({
    delimiters: ["[[", "]]"],
    el: "#sign_up",
    data: {
        username: "",
        usernameCheck: 'None',
        email: "",
        emailCheck: 'None',
        password1: "",
        password2: "",
        passwordCheck: 'None',
    },
      
    methods: {
        isUser: function() {
            vm = this;
            
            username = vm.username

            if (username === ''){
                var userField = document.querySelector("#id_username");
                userField.style.borderBottom = `0px`;
                vm.usernameCheck = true
            }
            
            
            const timeoutId = window.setTimeout(() => {}, 0);
            for (let id = timeoutId; id >= 0; id -= 1) {
            window.clearTimeout(id);
            }

            setTimeout(() => {
                sendRequest('user/' + username + '/', 'get')
                .then(function(response){
                    vm.usernameCheck = response.data.user

                    var userField = document.querySelector("#id_username");
                    if (vm.usernameCheck == false) {
                        userField.style.borderBottom = `2px solid rgb(199, 37, 37)`;
                    }
                    else {
                        userField.style.borderBottom = `0px`;
                    }
                })
            }, 500);
            

        },

        isEmail: function() {
            vm = this;
            
            email = vm.email

            if (email === ''){
                var emailField = document.querySelector("#id_email");
                emailField.style.borderBottom = `0px`;
                vm.emailCheck = true
            }
            
            sendRequest('email/' + email + '/', 'get')
                .then(function(response){
                    vm.emailCheck = response.data.email

                    var emailField = document.querySelector("#id_email");
                    if (vm.emailCheck == false) {
                        emailField.style.borderBottom = `2px solid rgb(199, 37, 37)`;
                    }
                    else {
                        emailField.style.borderBottom = `0px`;
                    }
            })
            
        },

        isPassword: function() {
            vm = this;
            var passwordField = document.querySelector("#id_password2");

            if (vm.password1 != '' && vm.password2 != '' && vm.password1 != vm.password2) {
                passwordField.style.borderBottom = `2px solid rgb(199, 37, 37)`;
                vm.passwordCheck = false
            }
            else {
                passwordField.style.borderBottom = `0px`;
                vm.passwordCheck = true
            }
        },

       
        
    },
})