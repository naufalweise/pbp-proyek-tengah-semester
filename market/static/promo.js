$(document).ready(function() {
        
    getForm();

    $(document).on('submit',"#add-promo-form",function (e) {
    e.preventDefault();

    var deal = $("#isi").val();
    console.log("deal", deal)

    $.ajax({
        type: "POST",
        url: "/market/add/",
        async:true,
        data: {
            deal: deal,
            csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            $("#add-promo").modal('hide');
            document.getElementById("add-promo-form").reset();
            $("#show-promo").empty();
            getForm();

        },
        error: function (error) {
            console.log(error);
        },

    });

  });
  
});

function getForm(){
    $("#show-promo").empty()
    $('#show-delete').empty()
    $.get("/market/json", function(data) {
        $.each(data, function(index, value) {
            $("#show-promo").append(
                "<div class='list-group w-100'>"+
                    "<div class='d-flex w-100 justify-content-between'>"+
                        "<h5 class='mb-1'>"+value.fields.promo+"</h5>"+
                    "</div>"+
                "</div>"
            );
            $("#show-delete").append(
                "<div class='tombol text-center mb-2'>" +
                    "<button class='btn btn-danger' onclick='deleteTask(" + value.pk + ")'>Delete</button>" +    
                "</div>"
            );
        });
    });
}

function deleteTask(id) {
    $.ajax({
        type: "POST",
        url:"delete/" + id,
        data: {csrfmiddlewaretoken:$('input[name = csrfmiddlewaretoken]').val(),},
        success: function (response) {
            $("#card-container").empty();
            getForm();
        },
    });
}