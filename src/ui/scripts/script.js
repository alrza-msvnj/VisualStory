$(document).ready(function () {
    initClickEvents();
});


function initClickEvents() {
    // dark mode btn
    let darkModeBtn = $('#dark-btn');
    darkModeBtn.on('click', toggleDarkMode);

    if (localStorage.getItem('theme') === 'light') {
        darkModeBtn.removeClass('dark-btn-on');
        $('body').removeClass('dark-theme');
    } else if (localStorage.getItem('theme') === 'dark') {
        darkModeBtn.addClass('dark-btn-on');
        $('body').addClass('dark-theme');
    } else {
        localStorage.setItem('theme', 'light');
    }

    // settings menu
    let settingsMenu = $('.nav-user-icon.online');
    settingsMenu.on('click', settingsMenuToggle);
}

function settingsMenuToggle() {
    let settingsMenu = $('.settings-menu');
    settingsMenu.toggleClass('settings-menu-height');
}

function toggleDarkMode() {
    let darkModeBtn = $('#dark-btn');
    darkModeBtn.toggleClass('dark-btn-on');

    let body = $('body');
    body.toggleClass('dark-theme');

    if (localStorage.getItem('theme') === 'light') {
        localStorage.setItem('theme', 'dark');
    } else {
        localStorage.setItem('theme', 'light');
    }
}