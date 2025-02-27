$(document).ready(function () {
    checkDarkMode();
    initClickEvents();
});


function checkDarkMode() {
    let theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
    }
}

function initClickEvents() {
    $('#loginBtn').click(login);
}

function login() {
    // Serialize form data into an object (dictionary)
    const formData = {};
    $('#loginForm').serializeArray().forEach(item => {
        formData[item.name] = item.value;
    });

    // Send the dictionary as JSON using jQuery's $.ajax
    $.ajax({
        url: '/api/authentication/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function (response, status, xhr) {
            console.log('Login successful:', response);

            let sessionId = xhr.getResponseHeader("session_id");
            if (sessionId) {
                // Store it in a cookie (valid for 1 day)
                document.cookie = `session_id=${sessionId}; path=/; Secure; HttpOnly; SameSite=Lax`;
            }

            // check if the response contains a redirect URL
            var redirectUrl = xhr.getResponseHeader("X-Redirect-To");
            if (redirectUrl) {
                window.location.href = redirectUrl;  // Redirect to the new page
            } else {
                location.reload();  // If no redirect, just refresh
            }
        },
        error: function (xhr, status, error) {
            console.error('Login failed:', status, error);
        }
    });
}
