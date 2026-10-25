document.addEventListener('DOMContentLoaded', () => {
    // Referencias a los elementos de Selección de Rol
    const btnAprendiz = document.getElementById('btn-rol-aprendiz');
    const btnFuncionario = document.getElementById('btn-rol-funcionario');
    const seccionAprendiz = document.getElementById('seccion-aprendiz');
    const seccionFuncionario = document.getElementById('seccion-funcionario');

    // Referencias a los elementos de Tipo de Funcionario
    const selectTipoFuncionario = document.getElementById('tipo_funcionario');
    const grupoContrato = document.getElementById('grupo-numero-contrato');
    const grupoFechaInicio = document.getElementById('grupo-fecha-inicio-contrato');
    const grupoFechaFin = document.getElementById('grupo-fecha-fin-contrato');

    // Cambiar entre Aprendiz y Funcionario
    if (btnAprendiz && btnFuncionario) {
        btnAprendiz.addEventListener('click', () => {
            btnAprendiz.classList.add('btn-role--active');
            btnFuncionario.classList.remove('btn-role--active');
            seccionAprendiz.classList.remove('is-hidden');
            seccionFuncionario.classList.add('is-hidden');
        });

        btnFuncionario.addEventListener('click', () => {
            btnFuncionario.classList.add('btn-role--active');
            btnAprendiz.classList.remove('btn-role--active');
            seccionFuncionario.classList.remove('is-hidden');
            seccionAprendiz.classList.add('is-hidden');
        });
    }

    // Mostrar/Ocultar campos según el Tipo de Funcionario
    if (selectTipoFuncionario) {
        selectTipoFuncionario.addEventListener('change', function () {
            if (this.value === 'PLANTA') {
                grupoContrato.classList.remove('is-hidden');
                grupoFechaInicio.classList.add('is-hidden');
                grupoFechaFin.classList.add('is-hidden');
            } else if (this.value === 'CONTRATISTA') {
                grupoContrato.classList.remove('is-hidden');
                grupoFechaInicio.classList.remove('is-hidden');
                grupoFechaFin.classList.remove('is-hidden');
            } else {
                grupoContrato.classList.add('is-hidden');
                grupoFechaInicio.classList.add('is-hidden');
                grupoFechaFin.classList.add('is-hidden');
            }
        });
    }
});