$(document).ready(function() {
    function deleteTask() {
        var id_splitted = this["id"].split("-");
        var id = id_splitted[id_splitted.length-1];

        $.ajax({
            url: "/my",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                form_type: "delete",
                id: id
            }),
            success: function(response) {
                $("#trash-can-"+response.id).parent().fadeOut( function() {
                    $("#trash-can-"+response.id).parent().remove();
                    if ($(".task-wrapper").length == 0) $(".no-tasks").removeClass("d-none")
                });
            },
            error: function() {
                alert("Ошибка при добавлении задачи");
            }
        });
    }

    $(document).on("click", ".trash-can", deleteTask);
});