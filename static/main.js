function getText() {
    // alert("hello");
    var user_text = document.getElementById("user_input").value;
    const formData = new FormData();
    formData.append("getText", user_text);
    fetch('/processdata', { method: 'POST', body: formData })
        .then(res => res.text())
        .then(text => outputText(text))


    const formData2 = new FormData();
    formData2.append("getSuggestions", user_text);
    fetch('/suggestionsdata', { method: 'POST', body: formData2 })
        .then(res => res.text())
        .then(text => outputSuggestions(text))
}

function outputText(text) {
    var str = text;
    console.log(str);
    var modified_text = document.getElementById("text_output")
    modified_text.value = str;
}

function outputSuggestions(text) {
    var str = text;
    console.log(str);
    var suggestions_field = document.getElementById("suggestionsBox")
    suggestions_field.value = str;
}
