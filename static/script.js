async function procesar() {
    const texto = document.getElementById('texto').value;
    const contenedor = document.getElementById('contenedor-emociones');
    
    if (!texto.trim()) {
        alert("Por favor, escribe algo.");
        return;
    }

    contenedor.innerHTML = "Analizando (la primera vez puede tardar)...";

    try {
        const resp = await fetch('/analizar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texto: texto })
        });

        // Verificamos si el servidor respondió bien
        if (!resp.ok) {
            throw new Error("Error en el servidor");
        }

        const emociones = await resp.json();
        contenedor.innerHTML = ""; 

        emociones.forEach(emo => {
            const div = document.createElement('div');
            div.className = "emocion-tag";
            div.style.backgroundColor = emo.color;
            div.innerHTML = `<strong>${emo.nombre}</strong> <span>${emo.fuerza}</span>`;
            contenedor.appendChild(div);
            const fuerzaNumero = parseInt(emo.fuerza); // Quita el % y lo hace número
div.style.transform = `scale(${0.8 + (fuerzaNumero / 100)})`; // Las más grandes brillan más
div.style.opacity = fuerzaNumero < 20 ? "0.7" : "1"; // Las pequeñas se ven más tenues
        });

        if (emociones.length > 0) {
            document.body.style.backgroundColor = emociones[0].color + "44";
        }
    } catch (error) {
        contenedor.innerHTML = "❌ Error al conectar con la IA.";
        console.error("Detalles del error:", error);
    }
}