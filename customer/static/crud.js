
// TODO: MODIFY Save customer form to support update customer
function saveCustomerForm() {
	const form = $("#customer-form")
	const url = form.attr("action")
	$.ajax({method: "POST", url, data: form.serialize()})
		.done(res => {
			const message = form.attr("data-action") == "create" ? "Added new customer!" : "Updated a customer!"
			alert(message)
			modal.hide()
			fetchAndRenderCustomer()
		})
		.fail(res => form.find("div.errors").html(res.responseJSON.errors))
	console.log("SAVE")
}






