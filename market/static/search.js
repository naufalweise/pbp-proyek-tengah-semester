const medicineCardTemplate = document.querySelector("[data-medicine-template]")
const medicineCardContainer = document.querySelector("[data-medicine-cards-container]")
const searchInput = document.querySelector("[data-search]")

let medicines = []

searchInput.addEventListener("input", e => {
  const value = e.target.value.toLowerCase()
  medicines.forEach(medicine => {
    const isVisible =
      medicine.name.toLowerCase().includes(value) ||
      medicine.pharmacy.toLowerCase().includes(value)
    medicine.element.classList.toggle("hide", !isVisible)
  })
})

fetch("/medicine/retrieve")
  .then(res => res.json())
  .then(data => {
    medicines = data.map(medicine => {
      const card = medicineCardTemplate.content.cloneNode(true).children[0]
      const name = card.querySelector("[data-name]")
      const stock = card.querySelector("[data-stock]")
      const pharmacy = card.querySelector("[data-pharmacy]")
      name.textContent = medicine.fields.name
      stock.textContent = "Stock: " + medicine.fields.stock
      pharmacy.textContent = "Pharmacy: " + medicine.fields.pharmacy
      medicineCardContainer.append(card)
      return { name: medicine.fields.name, stock: medicine.fields.stock, pharmacy: medicine.fields.pharmacy, element: card }
    })
  })

