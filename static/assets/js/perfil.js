document.addEventListener('DOMContentLoaded', () => {
    // Definición de elementos
    const btnOpenModal   = document.getElementById('openEditProfileModal');
    const modalEdit      = document.getElementById('modalEditProfile');
    const btnCloseModal  = document.getElementById('btnCloseEditModal');
    const btnCancelModal = document.getElementById('btnCancelEditModal');
    const formEdit       = document.getElementById('formEditProfile');

    // Apertura del modal
    const openModal = (e) => {
        if (e) e.preventDefault();
        if (modalEdit) {
            modalEdit.classList.add('modal__overlay--active');
            document.body.style.overflow = 'hidden';
        }
    };

    // Cierre del modal
    const closeModal = () => {
        if (modalEdit) {
            modalEdit.classList.remove('modal__overlay--active');
            document.body.style.overflow = '';
        }
    };

    // Asignación de Listeners
    if (btnOpenModal)   btnOpenModal.addEventListener('click', openModal);
    if (btnCloseModal)  btnCloseModal.addEventListener('click', closeModal);
    if (btnCancelModal) btnCancelModal.addEventListener('click', closeModal);

    // Cierre al presionar fuera del contenedor modal
    if (modalEdit) {
        modalEdit.addEventListener('click', (e) => {
            if (e.target === modalEdit) closeModal();
        });
    }

    // Submit del formulario
    if (formEdit) {
        formEdit.addEventListener('submit', (e) => {
            e.preventDefault();
            closeModal();
        });
    }
});