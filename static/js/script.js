function copyfunction(){
    var copyText = document.getElementById("content").innerHTML;

    // copyText.select();
   // copytext.select();
    navigator.clipboard.writeText(copyText);

    alert("Copied the text: " + copyText);

}


// document.getElementById('myForm').addEventListener('submit', function(event) {
//     // Prevent the default form submission behavior
//     event.preventDefault();
// })