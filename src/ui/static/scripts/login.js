$(document).ready(function () {
    debugger;
    checkDarkMode();
    $('#loginBtn').click(function () {
      // Serialize form data into an object (dictionary)
      const formData = {};
      $('#loginForm').serializeArray().forEach(item => {
        formData[item.name] = item.value;
      });

      // Send the dictionary as JSON using jQuery's $.ajax
      $.ajax({
        url: '/api/authentication/login', // API endpoint
        type: 'POST',                     // HTTP method
        contentType: 'application/json',  // Data type being sent
        data: JSON.stringify(formData),   // Convert dictionary to JSON
        success: function (response) {
          console.log('Login successful:', response);
          // Handle success (e.g., redirect or show success message)
        },
        error: function (xhr, status, error) {
          console.error('Login failed:', status, error);
          // Handle failure (e.g., show error message)
        }
      });
    });
});


function checkDarkMode() {
    let theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
    }
}
