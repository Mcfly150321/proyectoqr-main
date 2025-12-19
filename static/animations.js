document.addEventListener('DOMContentLoaded', () => {
    const card = document.querySelector('.card');

    // Configuración inicial (invisible y un poco abajo)
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.8s ease-out';

    // Disparar la animación después de un pequeño retraso
    setTimeout(() => {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
    }, 100);
});