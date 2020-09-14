let buttonSearchModal = document.getElementById("search-modal");
let modal = document.getElementsByClassName("custom-modal")[0];
let closeModal = document.getElementById("close-modal");

buttonSearchModal.addEventListener("click",toggleModal);
closeModal.addEventListener("click",toggleModal);

function toggleModal() {
    modal.classList.toggle("custom-show-modal");
}
