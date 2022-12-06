const request = require('request')
// cj model ,old version 

// Request URL
var url = 'https://jsonplaceholder.typicode.com/todos/1';

request(url, (error, response, body)=>{
	
	// Printing the error if occurred
	if(error) console.log(error)

	// Printing status code
	console.log(response.statusCode);
	
	// Printing body
	console.log(body);
});
