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
                    <div id="task-wrapper" class="task-wrapper" style="display: none;">
                        <div class="task-wrapper-left">
                            <input id="task${response.id}"
                                type="checkbox"
                                name="task"
                                value="${response.id}"
                                autocomplete="off">

                            <label for="task${response.id}">
                                <!--- FIXME: html инъекция --->
                                ${response.task}
                            </label>
                        </div>
                        <div id="trash-can-${response.id}" class="trash-can">
                            <img src="/static/images/trash-can.svg" alt="Delete">
                        </div>
                    </div>`;
                $("#taskList").append(newTask);
                $(".task-wrapper").last().fadeIn();
                $("#taskInput").val("");

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

    $("#addTaskBtn").click(addTask);
    $("#taskInput").keypress(function(event) {
        // Enter
        if (event.which === 13) addTask();
    });
});