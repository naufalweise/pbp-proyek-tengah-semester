function login(e) {
	e.preventDefault()
	const form = $(e.target)
	const url = form.attr("action")
	$.ajax({method: "POST", url, data: form.serialize()})
		.done(data => {
			window.location.replace(data.homepage_url);
		})
		.fail(res => form.find("div.errors").html(res.responseJSON.errors))
}