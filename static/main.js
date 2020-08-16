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

    const formData3 = new FormData();
    formData3.append("getSentiments", user_text);
    fetch('/sentimentdata', { method: 'POST', body: formData3 })
        .then(res => res.text())
        .then(text => colorSentiment(text))
}

function outputText(text) {
    //document.getElementById("text_output").readOnly = false;
    var str = text;
    console.log(str);
    var modified_text = document.getElementById("text_output")
    modified_text.value = str;
    //document.getElementById("text_output").readOnly = true;
}

function outputSuggestions(text) {
    var str = text;
    console.log(str);
    var suggestions_field = document.getElementById("suggestionsBox")
    suggestions_field.value = str;
}

function colorSentiment(text) {
  //  document.getElementById("text_output").readOnly = false;
    var score = parseFloat(text);
    var t = document.getElementById("text_output");

    if (score <= -0.8) {
      t.style.backgroundColor='crimson';
    } else if (score > -0.8 && score <= -0.6) {
      t.style.backgroundColor='firebrick';
    } else  if (score > -0.6 && score <= -0.4) {
      t.style.backgroundColor='salmon';
    } else if (score > -0.4 && score <= -0.2) {
      t.style.backgroundColor='lightsalmon';
    } else if (score > -.02 && score <= 0){
      t.style.backgroundColor='orange';
    } else if (score > 0 && score <= 0.2){
      t.style.backgroundColor='khaki';
    } else if(score > 0.2 && score <= 0.4){
      t.style.backgroundColor='lightgoldenrod';
    } else if(score > 0.4 && score <= 0.6){
      t.style.backgroundColor='palegreen';
    } else if(score > 0.6 && score <= 0.8){
      t.style.backgroundColor='seagreen';
    } else {
      t.style.backgroundColor='springgreen';
    }
  //  document.getElementById("text_output").readOnly = true;
}
