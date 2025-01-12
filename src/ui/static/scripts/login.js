$(document).ready(function () {
    checkDarkMode();
});


function checkDarkMode() {
    let theme = localStorage.getItem('theme');
    if (theme === 'light') {
        $('body').removeClass('dark-theme');
    } else if (theme === 'dark') {
        $('body').addClass('dark-theme');
    }
}
