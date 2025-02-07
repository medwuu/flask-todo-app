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

                    // progress-bar
                    completed_tasks = $('input:checkbox:checked').length;
                    var total_tasks = $('input:checkbox').length;
                    var complete_percent = (Math.round(completed_tasks / total_tasks * 100)) || 0;
                    $(".progress-bar").css("width", complete_percent+"%");
                    $(".progress-bar-inner").text(complete_percent+"%");
                    if (complete_percent > 48) {
                        $(".progress-bar-inner").css("color", "var(--white)");
                    } else {
                        $(".progress-bar-inner").css("color", "inherit");
                    }
                });
            },
            error: function() {
                alert("Ошибка при добавлении задачи");
            }
        });
    }

    $(document).on("click", ".trash-can", deleteTask);
});