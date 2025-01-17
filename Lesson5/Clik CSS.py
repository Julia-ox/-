// Находим кнопку по CSS-классу
const button = document.querySelector('.btn-primary');

// Проверяем, что кнопка найдена
if (button) {
    // Кликаем по кнопке
    button.click();
    console.log('Кликнут ' + button.innerText);
} else {
    console.log('Кнопка не найдена');
}