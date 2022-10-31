

var modal

$(document).ready(() => {
	console.log("Init")
	const csrftoken = Cookies.get('csrftoken');
	console.log("CSRF", csrftoken)
	$.ajaxSetup({
		headers: {'X-CSRFToken': csrftoken},
	});
	modal = new bootstrap.Modal('#pharmacy-form-modal', {})
	fetchAndRenderPharmacys()
})

function fetchAndRenderPharmacys() {
	$.ajax({type: "GET", url: "/pharmacy/retrieve"})
		.done(data => {
			console.log("DONE FETCHING MEDS")
			console.log(data)
			renderPharmacys(data)
		})
}

function renderPharmacys(pharmacys) {
	const tableBody = $("#pharmacy-table>tbody")
	tableBody.empty()
	pharmacys.forEach(m => {
		const row = `
			<tr>
				<td>${m.fields.name}</td>
				<td>${m.fields.address}</td>
				<td><div class="d-flex gap-2"><button class="btn btn-secondary" onclick="deletePharmacy(${m.pk})">Delete</button><button class="btn btn-secondary" onclick="openEditForm(${m.pk})">Edit</button></div></td>
			</tr>
		`
		tableBody.append(row)
	})
}

function openPharmacyForm() {
	const modalBody = $("#pharmacy-form-modal-body")
	modalBody.text("Loading ...")
	modal.show()
	$.ajax({method: "GET", url: "/pharmacy/form"}).done(data => {
		console.log("FINISHED FETCHING FORM")
		console.log(data)
		const form = $("<form>")
			.attr("id", "pharmacy-form")
			.attr("data-action", "create")
			.attr("action", "/pharmacy/create")
			.html(data.form)
			.append($("<div>").attr("class", "errors") )
		console.log(form)
		modalBody.empty()
		modalBody.append(form)
	})
}




function openEditForm(id) {
	const modalBody = $("#pharmacy-form-modal-body")
	modalBody.text("Loading ...")
	modal.show()
	$.ajax({method: "GET", url: "/pharmacy/form/" + id}).done(data => {
		console.log("FINISHED FETCHING FORM")
		console.log(data)
		const form = $("<form>")
			.attr("id", "pharmacy-form")
			.attr("data-action", "update")
			.attr("action", "/pharmacy/update/" + id)
			.html(data.form)
			.append($("<div>").attr("class", "errors") )
		console.log(form)
		modalBody.empty()
		modalBody.append(form)
	})
}


// TODO: MODIFY Save pharmacy form to support update pharmacy
function savePharmacyForm() {
	const form = $("#pharmacy-form")
	const url = form.attr("action")
	$.ajax({method: "POST", url, data: form.serialize()})
		.done(res => {
			const message = form.attr("data-action") == "create" ? "Added new pharmacy!" : "Updated a pharmacy!"
			alert(message)
			modal.hide()
			fetchAndRenderPharmacys()
		})
		.fail(res => form.find("div.errors").html(res.responseJSON.errors))
	console.log("SAVE")
}


function deletePharmacy(id) {
	$.ajax({method: "POST", url: "/pharmacy/delete/" + id})
		.done(() => {
			alert("Deleted one pharmacy!")
			fetchAndRenderPharmacys()
		})
	console.log("DELETE ", id)
}



