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
            console.log(username)

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
                    console.log('username attempted')
                    vm.usernameCheck = response.data.user
                    console.log(vm.usernameCheck)

                    var userField = document.querySelector("#id_username");
                    if (vm.usernameCheck == false) {
                        userField.style.borderBottom = `2px solid rgb(199, 37, 37)`;
                    }
                    else {
                        userField.style.borderBottom = `0px`;
                    }
                    vm.sectionCheck()
                })
            }, 500);
            

        },

        isEmail: function() {
            vm = this;
            
            email = vm.email
            console.log(email)

            if (email === ''){
                var emailField = document.querySelector("#id_email");
                emailField.style.borderBottom = `0px`;
                vm.emailCheck = true
            }
            
            sendRequest('email/' + email + '/', 'get')
                .then(function(response){
                    console.log('email attempted')
                    vm.emailCheck = response.data.email
                    console.log(vm.emailCheck)

                    var emailField = document.querySelector("#id_email");
                    if (vm.emailCheck == false) {
                        emailField.style.borderBottom = `2px solid rgb(199, 37, 37)`;
                    }
                    else {
                        emailField.style.borderBottom = `0px`;
                    }
                    vm.sectionCheck()
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
            this.sectionCheck()
        },

        sectionCheck() {
            var signUpSection = document.querySelector(".signUpSection");
            timesX = 0
            if (!vm.usernameCheck) timesX++
            if (!vm.emailCheck) timesX++
            if (!vm.passwordCheck) timesX++
            signUpSection.style.height = `${98 + ((14/3) * timesX)}%`
            console.log(timesX)
        },
        
    },
})