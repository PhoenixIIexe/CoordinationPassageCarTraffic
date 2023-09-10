const form = document.querySelector('.upload-form');
const tilte = document.querySelector('.upload-form__title');
form.addEventListener('change', handleSubmit);

/** @param {Event} event */
function handleSubmit(event) {
    console.log(event)
    tilte.textContent = "Файл загружен"
}