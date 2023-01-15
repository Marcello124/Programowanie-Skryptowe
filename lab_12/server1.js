const express = require('express');
const logger = require('morgan');
const bodyParser = require('body-parser');
const app = express();

// Configuring the application
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');
app.locals.pretty = app.get('env') === 'development';

// Determining the contents of the middleware stack
app.use(logger('dev'));

// Parse urlencoded form into json
app.use(bodyParser.urlencoded({ extended: true }));

// app.use(express.static(__dirname + '/public'));

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
    res.render('index');
});

// The second route
app.get('/submit', function (req, res) {

    var name = (typeof req.query.imie != "undefined") ? req.query.imie : "World";

    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            
            res.type('application/json');
            res.json({ welcome: `Hello ${name}` });  
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            
            res.type('application/xml');
            res.send(`<welcome>Hello ${name}</welcome>`);   
            console.log("The server sent an XML document to the browser");
            break;

        default:
        
            res.type('text/plain');
            res.send(`Hello ${name}`);        
            console.log("The server sent a plain text to the browser");
    }
});

app.post("/submit", function (req, res) {

    var name = (typeof req.body.imie != "undefined") ? req.body.imie : "World";


    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            
            res.type('application/json');
            res.json({ welcome: `Hello ${name}` });  
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            
            res.type('application/xml');
            res.send(`<welcome>Hello ${name}</welcome>`);  
            console.log("The server sent an XML document to the browser");
            break;

        default:
           
            res.type('text/plain');
            res.send(`Hello ${name}`);       
            console.log("The server sent a plain text to the browser");
    }
})



// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});