// Setup csrf token
const csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
	headers: {'X-CSRFToken': csrftoken},
});