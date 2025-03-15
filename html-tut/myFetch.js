var showDitto = async function() {
	const response = await fetch("https://pokeapi.co/api/v2/pokemon/ditto");
	const jsonData = await response.json();
	document.getElementById("myDittoFetchBox").innerHTML = JSON.stringify(jsonData);
}
document.getElementById("dittoButton").addEventListener("click", showDitto);

var showMorpheus = async function() {
        const url = "https://reqres.in/api/users";
	const data = {"user": "morpheus", "job": "leader"};
        const response = await fetch(url, {
		method: "POST",
		mode: "cors",
		cache: "no-cache",
		credentials: "omit",
		headers : {
			"Content-Type": "application/json"
		},
		redirect: "follow",
		referrerPolicy: "no-referrer",
		body: JSON.stringify(data)

	});
        const jsonData = await response.json();
        document.getElementById("myMorpheusFetchBox").innerHTML = JSON.stringify(jsonData);
}

document.getElementById("morpheusButton").addEventListener("click", showMorpheus);
