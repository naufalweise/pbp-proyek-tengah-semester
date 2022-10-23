$(document).ready(() => {
	console.log("Init")
	fetchAndRenderMedicines()
})
function fetchAndRenderMedicines() {
	$.ajax({type: "GET", url: "/medicine/retrieve"})
		.done(data => {
			console.log("DONE FETCHING MEDS")
			console.log(data)
			renderMedicines(data)
		})
}

function renderMedicines(medicines) {
	const tableBody = $("#medicine-table>tbody")
	tableBody.empty()
	medicines.forEach(m => {
		const row = `
			<tr>
				<td>${m.fields.name}</td>
				<td>${m.fields.stock}</td>
				<td>Pharmacy ${m.fields.pharmacy}</td>
			</tr>
		`
		tableBody.append(row)
	})
}