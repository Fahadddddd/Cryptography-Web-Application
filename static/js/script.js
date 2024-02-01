function copyfunction(){
    var copyText = document.getElementById("content").innerHTML;

    // copyText.select();
   // copytext.select();
    navigator.clipboard.writeText(copyText);

    alert("Copied the text: " + copyText);

}