function getText() {
    var user_text = document.getElementById("user_input").value;
    const formData = new FormData();
    formData.append("getText", user_text);
    fetch('/processdata', { method: 'POST', body: formData })
        .then(res => res.text())
}