const express = require('express');
const logger = require('morgan');
const bodyParser = require('body-parser')
const encoder = bodyParser.urlencoded();
/************* */
const app1 = express();
const app2 = express();
/************* */
app1.use(logger('dev'));
app2.use(logger('dev'));
/************* */
app1.listen(3000, function () {
	    console.log('The application is available on port 3000');
});
app2.listen(3001, function () {
	    console.log('The application is available on port 3001');
});
/************* */
app1.get('/', function (req, res) {
	    res.sendFile(__dirname + '/download.html');
});

app1.post('/', encoder, (req, res) => {
	var area = req.body.area;
	var location = req.body.location
	console.log(area, location)
	fetch("https://worldtimeapi.org/api/" + area + "/" + location)
	.then(res=>res.json())
	// .then(data=>console.log(data))
	.then(data=>res.send(data));
});

app2.get('/', function (req, res) {
	    res.send('Response from 3001');
});
/************* */
console.log("To stop the server, press 'CTRL + C'");