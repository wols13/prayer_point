//Scripts for the add prayer point UI component

function updateTitleCount() {
    var remaining_characters = 512 - document.getElementById("add_pp_title").value.length;
    document.getElementById("add_pp_title_count").innerHTML = remaining_characters;
}

function updateContentCount() {
    var remaining_characters = 512 - document.getElementById("add_pp_content").value.length;
    document.getElementById("content_char_count").innerHTML = remaining_characters;
}