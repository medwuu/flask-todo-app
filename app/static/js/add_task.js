$(document).ready(function() {
    function addTask() {
        var taskText = $("#taskInput").val().trim();
        if (taskText === "") {
            alert("Задача не может быть пустой!");
            return;
        }

        $.ajax({
            url: "/my",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ form_type: "add", task: taskText }),
            success: function(response) {
                if ($(".task-wrapper").length == 0) $(".no-tasks").addClass("d-none")
                var newTask = `
                    <div id="task-wrapper" class="task-wrapper">
                        <input id="task${response.id}"
                            type="checkbox"
                            name="task"
                            value="${response.id}"
                            autocomplete="off">

                        <label for="task${response.id}">
                            ${response.task}
                        </label>
                        <div id="trash-can-${response.id}" class="trash-can">
                            <img src="/static/images/trash-can.svg" alt="Delete">
                        </div>
                    </div>`;
                $("#taskList").append(newTask);
                $("#taskInput").val("");
            },
            error: function() {
                alert("Ошибка при добавлении задачи");
            }
        });
    }

    $("#addTaskBtn").click(addTask);
    $("#taskInput").keypress(function(event) {
        // Enter
        if (event.which === 13) addTask();
    });
});