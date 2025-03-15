const xhttp = new XMLHttpRequest();
var showDate = function() {
	xhttp.open("GET", "https://worldtimeapi.org/api/timezone/Asia/Kolkata", false);
	xhttp.send();
	document.getElementById("xmlhttprequest").innerHTML = xhttp.responseText;
}
document.getElementById("dateButton").addEventListener("click", showDate);

/* 
 * xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
 *
 * xhttp.send("fname=Henry&lname=Ford");
 *
*/
