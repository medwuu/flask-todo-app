$(document).ready(function() {
    function sortBy() {
        var sort_by = this.value;

        $.ajax({
            url: "/my",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ form_type: "sort", sort_by: sort_by }),
            success: function() {
                $("#taskList").toggleClass("flex-column");
                $("#taskList").toggleClass("flex-column-reverse");
            },
            error: function() {
                alert("Ошибка сортировки! Проверьте, не запрещены ли куки!");
            }
        });
    }

    $("#sortSelect").on('change', sortBy);
});