const csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
	headers: {'X-CSRFToken': csrftoken},
});

var modal

$(document).ready(() => {
	console.log("Init")
	modal = new bootstrap.Modal('#medicine-form-modal', {})
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

function openMedicineForm() {
	const modalBody = $("#medicine-form-modal-body")
	modalBody.text("Loading ...")
	modal.show()
	$.ajax({method: "GET", url: "/medicine/form"}).done(data => {
		console.log("FINISHED FETCHING FORM")
		console.log(data)
		const form = $("<form>")
			.attr("id", "medicine-form")
			.attr("data-action", "create")
			.html(data.form)
			.append($("<div>").attr("class", "errors") )
		console.log(form)
		modalBody.empty()
		modalBody.append(form)
	})
}

function saveMedicineForm() {
	const form = $("#medicine-form")
	$.ajax({method: "POST", url: "/medicine/" + form.attr("data-action"), data: form.serialize()})
		.done(res => {
			alert("A new medicine has been added!")
			modal.hide()
			fetchAndRenderMedicines()
		})
		.fail(res => form.find("div.errors").html(res.responseJSON.errors))
	console.log("SAVE")
}