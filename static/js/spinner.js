const patience = document.getElementById('patience');
const patience2 = document.getElementById('patience2');
const spinnerBox = document.getElementById('spinner-box');
const kataCall = document.getElementById('kata-call');


patience.addEventListener('click', () => {
    spinnerBox.classList.remove('not-visible');
    kataCall.classList.add('not-visible');
});

patience2.addEventListener('click', () => {
    spinnerBox.classList.remove('not-visible');
    kataCall.classList.add('not-visible');
});
