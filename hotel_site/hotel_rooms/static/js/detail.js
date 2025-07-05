const dateIn = sessionStorage.getItem("dateIn")
const dateOut = sessionStorage.getItem("dateOut")
const guests = sessionStorage.getItem("guests")

const dateInInput = document.getElementById("detail-input-in")
const dateOutInput = document.getElementById("detail-input-out")
const guestInput = document.getElementById("detail-guest")

dateInInput.value = dateIn
dateOutInput.value = dateOut
guestInput.value = guests
