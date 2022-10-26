

var modal

$(document).ready(() => {
	console.log("Init")
	const csrftoken = Cookies.get('csrftoken');
	console.log("CSRF", csrftoken)
	$.ajaxSetup({
		headers: {'X-CSRFToken': csrftoken},
	});
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
				<td><div class="d-flex gap-2"><button class="btn btn-secondary" onclick="deleteMedicine(${m.pk})">Delete</button><button class="btn btn-secondary" onclick="openEditForm(${m.pk})">Edit</button></div></td>
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
			.attr("action", "/medicine/create")
			.html(data.form)
			.append($("<div>").attr("class", "errors") )
		console.log(form)
		modalBody.empty()
		modalBody.append(form)
	})
}

function openEditForm(id) {
	const modalBody = $("#medicine-form-modal-body")
	modalBody.text("Loading ...")
	modal.show()
	$.ajax({method: "GET", url: "/medicine/form/" + id}).done(data => {
		console.log("FINISHED FETCHING FORM")
		console.log(data)
		const form = $("<form>")
			.attr("id", "medicine-form")
			.attr("data-action", "update")
			.attr("action", "/medicine/update/" + id)
			.html(data.form)
			.append($("<div>").attr("class", "errors") )
		console.log(form)
		modalBody.empty()
		modalBody.append(form)
	})
}

// TODO: MODIFY Save medicine form to support update medicine
function saveMedicineForm() {
	const form = $("#medicine-form")
	const url = form.attr("action")
	$.ajax({method: "POST", url, data: form.serialize()})
		.done(res => {
			const message = form.attr("data-action") == "create" ? "Added new medicine!" : "Updated a medicine!"
			alert(message)
			modal.hide()
			fetchAndRenderMedicines()
		})
		.fail(res => form.find("div.errors").html(res.responseJSON.errors))
	console.log("SAVE")
}

function deleteMedicine(id) {
	$.ajax({method: "POST", url: "/medicine/delete/" + id})
		.done(() => {
			alert("Deleted one medicine!")
			fetchAndRenderMedicines()
		})
	console.log("DELETE ", id)
}