// Flipatron //
document.querySelectorAll('.card').forEach(function(card) {
    card.addEventListener('click', function() {
        this.classList.toggle('flipped');
    });
});

// Image //

let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

function showSlide(index) {
    const slider = document.querySelector('.slider');
    const offset = -index * (100 / 3); // Calculate the offset to show the correct slide for 3 images
    slider.style.transform = `translateX(${offset}%)`;
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(currentSlide);
}

// Automatically move to the next slide every 3 seconds
setInterval(nextSlide, 3000);

// Initialize ScrollReveal
ScrollReveal().reveal('.title', {
    origin: 'top',
    distance: '50px',
    duration: 1000,
    delay: 200,
    reset: true
});

ScrollReveal().reveal('.logo a', {
    origin: 'bottom',
    distance: '30px',
    duration: 1000,
    interval: 100,
    reset: true
});

ScrollReveal().reveal('.text', {
    origin: 'left',
    distance: '100px',
    duration: 1200,
    delay: 200,
    reset: true
});

ScrollReveal().reveal('.skills-div .card-container', {
    origin: 'bottom',
    distance: '50px',
    duration: 1000,
    interval: 200,
    reset: true
});

ScrollReveal().reveal('.educat', {
    origin: 'top',
    distance: '50px',
    duration: 1000,
    delay: 200,
    reset: true
});

ScrollReveal().reveal('.slider-container', {
    origin: 'left',
    distance: '100px',
    duration: 1200,
    delay: 300,
    reset: true
});

ScrollReveal().reveal('.schooldes', {
    origin: 'right',
    distance: '100px',
    duration: 1200,
    delay: 300,
    reset: true
});

ScrollReveal().reveal('.cont', {
    origin: 'top',
    distance: '50px',
    duration: 1000,
});
