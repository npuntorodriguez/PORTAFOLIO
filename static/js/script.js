// ------------------------------
// script.js - Portafolio profesional
// ------------------------------

document.addEventListener("DOMContentLoaded", () => {

    // ------------------------------
    // Mensaje de bienvenida (solo en "/")
    // ------------------------------
    if (window.location.pathname === "/") {
        const saludoDiv = document.createElement("div");
        saludoDiv.className = "welcome-message fixed-top text-center py-3";
        saludoDiv.innerHTML = "✨ Bienvenida al portafolio de Natalia Rodríguez Escárate ✨";
        document.body.appendChild(saludoDiv);

        setTimeout(() => {
            saludoDiv.style.transition = "opacity 2s";
            saludoDiv.style.opacity = 0;
            setTimeout(() => saludoDiv.remove(), 2000);
        }, 3000);
    }

    // ------------------------------
    //  Navbar scroll
    // ------------------------------
    const navbar = document.querySelector(".navbar");
    if (navbar) {
        window.addEventListener("scroll", () => {
            if (window.scrollY > 10) {
                navbar.classList.add("navbar-scroll");
            } else {
                navbar.classList.remove("navbar-scroll");
            }
        });
    }

    // ------------------------------
    // Efecto visual botones submit
    // ------------------------------
    document.addEventListener("click", (e) => {
        if (e.target.tagName === "BUTTON" && e.target.type === "submit") {
            e.target.classList.add("btn-clicked");
            setTimeout(() => e.target.classList.remove("btn-clicked"), 500);
        }
    });

    // ------------------------------
    //  Mensajes de Django desaparecen después de 5 seg
    // ------------------------------
    const djangoAlerts = document.querySelectorAll(".django-alert");
    djangoAlerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = "opacity 1s";
            alert.style.opacity = 0;
            setTimeout(() => alert.remove(), 1000);
        }, 5000);
    });

    // ------------------------------
    // 5️⃣ Formulario de contacto con mensaje visual
    // ------------------------------
    const $form = $("#formContacto");
    if ($form.length) {

        // Crear contenedor de mensaje si no existe
        if ($("#mensajeForm").length === 0) {
            $form.prepend('<div id="mensajeForm" class="form-alert alert d-none"></div>');
        }
        const $mensajeDiv = $("#mensajeForm");

        $form.submit(function (e) {
            e.preventDefault();

            let nombre = $("input[name='nombre']").val().trim();
            let email = $("input[name='email']").val().trim();
            let mensaje = $("textarea[name='mensaje']").val().trim();

            if (!nombre || !email || !mensaje) {
                $mensajeDiv.removeClass("d-none alert-success")
                           .addClass("alert-danger")
                           .text("Por favor completa todos los campos.");
                return;
            }

            $mensajeDiv.removeClass("d-none alert-danger")
                       .addClass("alert-success")
                       .text("¡Gracias por tu mensaje, " + nombre + "! Me pondré en contacto contigo pronto.");

            $form[0].reset();

            // Ocultar mensaje después de 5 segundos
            setTimeout(() => {
                $mensajeDiv.addClass("d-none").removeClass("alert-success");
            }, 5000);
        });
    }

});