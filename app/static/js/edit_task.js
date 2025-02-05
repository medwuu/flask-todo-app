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
            },
            error: function() {
                alert("Ошибка при добавлении задачи");
            }
        });
    }

    $(document).on("click", "input[type='checkbox']", editTask);
});