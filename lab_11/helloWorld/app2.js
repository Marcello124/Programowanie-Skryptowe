// Application using the 'Pug' template system
const express = require('express'),
    logger = require('morgan'),
	fs = require('fs'),
	mongoose = require('mongoose');
const app = express();
const x = 1;
const y = 2;

const { Schema } = mongoose;
mongoose.connect('mongodb://127.0.0.1:27017/skryptowe', { useNewUrlParser: true, useUnifiedTopology: true }).then(() => {
const opSchema = new Schema({
    x: Number,
    y: Number,
    op: String
})
const Op = mongoose.model('Op', opSchema);

function sum(x, y) {
    return x + ' + ' + y + ' = ' + (x + y);
}

function exists(p) {
    try {
        return fs.existsSync(p);
    }
    catch (err) {
        return false
    }
}

function isFile(p) {
    return exists(p) && fs.statSync(p).isFile();
}

function readFile(fpath) {
    if (!isFile(fpath))
		return null;
	
    return fs.readFileSync(fpath, { encoding: 'utf8' })
}

// Configuring the application
app.set('views', __dirname + '/views'); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');          // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {      // The first route
    res.render('index', { sum: sum(x, y) });
});

app.get('/json/:name', function (req, res) {
    let json = JSON.parse(readFile(req.params.name));

    res.render('json', { file: json });
});

app.get('/calculate/:operation/:x/:y', async function (req, res) {
    if (!["+", "-", "*", "/"].includes(req.params.operation)) {
        res.status(400).send("Invalid operation.");
		return;
    }
	
    let newOp = new Op({ x: req.params.x, y: req.params.y, op: req.params.operation });
    await newOp.save();

    res.render('index', { sum: req.params.x + ' ' + req.params.operation + ' ' + req.params.y + ' = ' + eval('' + req.params.x + req.params.operation + req.params.y) });
});

app.get('/results', async function (req, res) {
    let json = await Op.find();

    res.render('json', { file: json });
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});
});
