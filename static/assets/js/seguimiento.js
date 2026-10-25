document.addEventListener('DOMContentLoaded', () => {
    const btnOpenTrackingModal = document.getElementById('openTrackingModal');
    const modalTracking = document.getElementById('modalTracking');
    const btnCloseTrackingModal = document.getElementById('btnCloseTrackingModal');
    const btnCancelTrackingModal = document.getElementById('btnCancelTrackingModal');

    // Abrir modal
    const openModal = (e) => {
        if (e) e.preventDefault();
        if (modalTracking) {
            modalTracking.classList.add('modal__overlay--active');
            document.body.style.overflow = 'hidden';
        }
    };

    // Cerrar modal
    const closeModal = () => {
        if (modalTracking) {
            modalTracking.classList.remove('modal__overlay--active');
            document.body.style.overflow = '';
        }
    };

    // Eventos
    if (btnOpenTrackingModal) {
        btnOpenTrackingModal.addEventListener('click', openModal);
    }

    if (btnCloseTrackingModal) {
        btnCloseTrackingModal.addEventListener('click', closeModal);
    }

    if (btnCancelTrackingModal) {
        btnCancelTrackingModal.addEventListener('click', closeModal);
    }

    // Cierre al dar clic fuera del modal
    if (modalTracking) {
        modalTracking.addEventListener('click', (e) => {
            if (e.target === modalTracking) {
                closeModal();
            }
        });
    }
});