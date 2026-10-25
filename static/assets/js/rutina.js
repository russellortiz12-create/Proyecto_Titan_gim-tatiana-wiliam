document.addEventListener('DOMContentLoaded', () => {
    const btnOpenRoutineModal = document.getElementById('openRoutineModal');
    const modalCreateRoutine = document.getElementById('modalCreateRoutine');
    const btnCloseRoutineModal = document.getElementById('btnCloseRoutineModal');
    const btnCancelRoutineModal = document.getElementById('btnCancelRoutineModal');

    // Función para abrir el modal de rutina
    const openModal = (e) => {
        if (e) e.preventDefault();
        if (modalCreateRoutine) {
            modalCreateRoutine.classList.add('modal__overlay--active');
            document.body.style.overflow = 'hidden'; // Bloquea el scroll de fondo
        }
    };

    // Función para cerrar el modal de rutina
    const closeModal = () => {
        if (modalCreateRoutine) {
            modalCreateRoutine.classList.remove('modal__overlay--active');
            document.body.style.overflow = ''; // Restaura el scroll
        }
    };

    // Asignación de eventos
    if (btnOpenRoutineModal) {
        btnOpenRoutineModal.addEventListener('click', openModal);
    }

    if (btnCloseRoutineModal) {
        btnCloseRoutineModal.addEventListener('click', closeModal);
    }

    if (btnCancelRoutineModal) {
        btnCancelRoutineModal.addEventListener('click', closeModal);
    }

    // Cierre al hacer clic en el fondo (overlay)
    if (modalCreateRoutine) {
        modalCreateRoutine.addEventListener('click', (e) => {
            if (e.target === modalCreateRoutine) {
                closeModal();
            }
        });
    }
});