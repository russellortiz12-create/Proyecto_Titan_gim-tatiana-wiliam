// Lógica para el cambio automático y manual de imágenes promocionales (Carrusel)
document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.carousel__slide');
    const dots = document.querySelectorAll('.dot');
    
    // Validación previa para evitar errores si no existe el carrusel en la vista actual
    if (!slides.length) return;

    let currentIndex = 0;
    const intervalTime = 6000; // 6 segundos por diapositiva
    let slideInterval;

    // Función para activar la diapositiva según su índice
    function showSlide(index) {
        slides.forEach((slide, i) => {
            // Remueve clases activas (estándar y BEM para máxima compatibilidad)
            slide.classList.remove('active', 'carousel__slide--active');
            if (dots[i]) {
                dots[i].classList.remove('active', 'dot--active');
            }
        });

        // Activa el slide y punto actual
        slides[index].classList.add('carousel__slide--active', 'active');
        if (dots[index]) {
            dots[index].classList.add('dot--active', 'active');
        }
        
        currentIndex = index;
    }

    // Avanza a la siguiente diapositiva
    function nextSlide() {
        let index = (currentIndex + 1) % slides.length;
        showSlide(index);
    }

    // Inicia el temporizador
    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, intervalTime);
    }

    // Reinicia el temporizador al interactuar
    function resetAutoSlide() {
        clearInterval(slideInterval);
        startAutoSlide();
    }

    // Eventos de clic en los puntos indicadores (dots)
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
            resetAutoSlide();
        });
    });

    // Inicializar carrusel
    showSlide(0);
    startAutoSlide();
});