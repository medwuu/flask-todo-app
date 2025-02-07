$(document).ready(function() {
    function editTask() {
        var id = this.value;
        var completed = $(this).is(":checked");

        $.ajax({
            url: "/my",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                form_type: "edit",
                id: id,
                completed: completed
            }),
            success: function(response) {
                $("#task"+response.id).siblings("label").toggleClass("text-decoration-line-through text-success fw-light")

                // progress-bar
                completed_tasks = $('input:checkbox:checked').length;
                var total_tasks = $('input:checkbox').length;
                var complete_percent = Math.round(completed_tasks / total_tasks * 100);
                $(".progress-bar").css("width", complete_percent+"%");
                $(".progress-bar-inner").text(complete_percent+"%");
                if (complete_percent > 48) {
                    $(".progress-bar-inner").css("color", "var(--white)");
                } else {
                    $(".progress-bar-inner").css("color", "inherit");
                }
            },
            error: function() {
                alert("Ошибка при добавлении задачи");
            }
        });
    }

    $(document).on("click", "input[type='checkbox']", editTask);
});