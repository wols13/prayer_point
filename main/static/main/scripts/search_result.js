function updateResults() {
    var book = document.getElementById("query_book").value;
    var chapter = document.getElementById("query_chapter").value;
    var verse = document.getElementById("query_verse").value;
    $.ajax({
            type: "GET",
            url: window.location.protocol + "//" + window.location.hostname + "/prayer_point_by_scripture",
            data: {'book': book, 'chapter': chapter, 'verse': verse}
        })
        .done(function(response) {
            document.getElementById("prayer_point_results").innerHtml = response;
        });
}