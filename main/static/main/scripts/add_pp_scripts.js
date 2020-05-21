//Scripts for the add prayer point UI component

function updateBibleRefCount() {
    var remaining_characters = 64 - document.getElementById("id_add_pp_bible_ref").value.length;
    document.getElementById("add_bible_ref_count").innerHTML = remaining_characters;
}

function updateContentCount() {
    var remaining_characters = 512 - document.getElementById("id_add_pp_content").value.length;
    document.getElementById("content_char_count").innerHTML = remaining_characters;
}