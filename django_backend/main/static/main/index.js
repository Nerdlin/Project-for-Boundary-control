let arrowTimeout;

function showArrows() {
    document.body.classList.add('show-arrows');
    clearTimeout(arrowTimeout);
    arrowTimeout = setTimeout(() => {
        document.body.classList.remove('show-arrows');
    }, 3000);
}

document.addEventListener('mousemove', showArrows);

function navigateToPrevious() {
    window.location.href = '/';
}

function navigateToNext() {
    window.location.href = '/history/';
}

// Добавляем элементы в глобальную область видимости, чтобы они были доступны из HTML
window.navigateToNext = navigateToNext;
window.navigateToPrevious = navigateToPrevious;
