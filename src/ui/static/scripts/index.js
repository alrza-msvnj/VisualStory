var isLoggedIn = false;


$(document).ready(function () {
    debugger;
    isLoggedIn = isAuthenticated();
    initLoginLogoutButtons();
    checkDarkMode();
    initClickEvents();
});


function isAuthenticated() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
        const [key, value] = cookie.split('=');
        if (key === 'session_id') {
            return true;
        }
    }

    return false;
}

function initLoginLogoutButtons() {
    if (isLoggedIn) {
        $('#loginBtn').hide();
        $('#logoutBtn').show();
    } else {
        $('#loginBtn').show();
        $('#logoutBtn').hide();
    }
}

function checkDarkMode() {
    const theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
        $('#lightModeBtn').remove();
        if ($('#darkModeBtn').length === 0) {
            $('<li id="darkModeBtn"><a href="#"><i class="bi bi-moon-stars"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#darkModeBtn').click(function () {
                toggleDarkMode('darkModeBtn');
            })
        }

    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
        $('#darkModeBtn').remove();
        let b = $('#darkModeBtn')
        if ($('#lightModeBtn').length === 0) {
            $('<li id="lightModeBtn"><a href="#"><i class="bi bi-brightness-high" style="font-size: 16px;position: relative; top: 0.5px;"></i></a></li>').insertBefore($('#nav-buttons li:eq(1)')); // Insert before the second <li>
            $('#lightModeBtn').click(function () {
                toggleDarkMode('lightModeBtn');
            })
        }
    }
}

function initClickEvents() {
    $('#darkModeBtn').click(function () {
        toggleDarkMode('darkModeBtn');
    });
    $('#lightModeBtn').click(function () {
        toggleDarkMode('lightModeBtn');
    });

    $('#postBtn').click(post);

    $('#logoutBtn').click(function (event) {
        logout(event);
    });
}

function toggleDarkMode(elementId) {
    debugger;
    if (elementId === 'darkModeBtn') {
        localStorage.setItem('theme', 'dark');
    } else if (elementId === 'lightModeBtn') {
        localStorage.setItem('theme', 'light');
    }
    checkDarkMode();
}

function post() {
    debugger;
    if (!isLoggedIn) {
        window.location.href = '/login';
    }

    // Serialize form data into an object (dictionary)
    const formData = {};
    formData.content = $('#postContent').val();

    $.ajax({
        url: '/api/post',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(formData),
        success: function (response) {
            debugger;
            console.log('Login successful:', response);
            location.reload();
        },
        error: function (error) {
            debugger;
            console.error('Login failed:', error);
        }
    });
}

function logout(event) {
    debugger;
    event.preventDefault();

    $.ajax({
        url: 'api/authentication/logout',
        type: 'GET',
        success: function (response, status, xhr) {
            console.log('Logout successful:', response);

            // check if the response contains a redirect URL
            const redirectUrl = xhr.getResponseHeader("X-Redirect-To");
            if (redirectUrl) {
                window.location.href = redirectUrl;  // Redirect to the new page
            } else {
                location.reload();  // If no redirect, just refresh
            }
        },
        error: function (xhr, status, error) {
            console.error('Logout failed:', status, error);
        },
        complete: function () {
            console.log('Request completed.');
        }
    });
}
