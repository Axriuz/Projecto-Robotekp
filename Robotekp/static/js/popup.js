var btnAbrirPopup = document.getElementById("btn-abrir-popup"),
	overlay = document.getElementById("overlay"),
	popup = document.getElementById("popup"),
	btnCerrarPopup = document.getElementById("btn-cerrar-popup");

function AbrirPopUp(){
    overlay.setAttribute('active');
	overlay.setAttribute('overlay','active');
}
btnCerrarPopup.addEventListener("click", function(e){
	e.preventDefault();
	overlay.classList.remove("active");
	popup.classList.remove("active");
});