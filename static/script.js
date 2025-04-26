// document -> representa toda la página web
// getElementById("formulario") -> busca un elemento que tenga el id="formulario"
// addEventListener("submit", ...) -> le dice al navegador: "cuando alguien envíe el formulario, ejecuta esta función"
document.getElementById("formulario").addEventListener("submit", async function(e) {

    // e.preventDefault() -> evita que el formulario se envíe de la forma tradicional (recargar la página)
    // Esto es útil si queremos enviar los datos con JavaScript sin que la página se recargue
    e.preventDefault();

    // document.getElementById("entradaUsuario") -> busca el elemento con id="entradaUsuario"
    // .value -> obtiene el texto que el usuario escribió en ese campo
    // Se guarda ese texto en una variable llamada "input"
    const input = document.getElementById("entradaUsuario").value;

    // fetch(...) -> se usa para enviar o pedir datos a un servidor (como si habláramos con otra computadora)
    // "/guardar" -> es la dirección en el servidor donde vamos a enviar los datos
    //   method: "POST" -> estamos diciendo que queremos ENVIAR datos (no solo pedirlos)
    //   headers: {"Content-Type": "application/json"} -> decimos que vamos a enviar los datos en formato JSON (un tipo de texto estructurado)
    //   body: JSON.stringify({ mensaje: input }) -> convertimos el mensaje a texto JSON antes de enviarlo
    await fetch("/guardar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ mensaje: input })
    });

    // Nota: usamos "await" porque fetch es una operación que toma tiempo, y queremos esperar a que termine antes de seguir
});
