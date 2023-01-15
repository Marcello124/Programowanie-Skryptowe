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

function readFile(p) {
    if (!isFile(p))
		return null;
	
    return fs.readFileSync(p, { encoding: 'utf8' })
}

app.use(logger('dev')); 
app.use(express.static(__dirname + 'public'));

app.get('', function (req, res) {
    res.send(sum(x, y)); 
});

app.get('/calculate/:operation/:x/:y', async function (req, res) {
    if (!["+", "-", "*", "/"].includes(req.params.operation)) {
        res.status(400).send("Invalid operation.");
		return;
    }
	
    let newOp = new Op({ x: req.params.x, y: req.params.y, op: req.params.operation });
    await newOp.save();
	
    res.send(req.params.x + ' ' + req.params.operation + ' ' + req.params.y + ' = ' + eval('' + req.params.x + req.params.operation + req.params.y));
});

app.get('/json/:name', async function (req, res) {
    let json = JSON.parse(readFile(req.params.name));

    res_str = '<table border="1"><tr><th>x</th><th>Operation</th><th>y</th><th>Result</th></tr>';

    for (var obj of json) {
        res_str += '<tr><td>' + obj.x + '</td><td>' + obj.op + '</td><td>' + obj.y + '</td><td>' + eval('' + obj.x + obj.op + obj.y) + '</td></tr>';
    }
	
    res_str += '</table>'
    res.send(res_str);
});


app.get('/results', async function (req, res) {
    let json = await Op.find();

    res_str = '<table border="1"><tr><th>x</th><th>Operation</th><th>y</th><th>Result</th></tr>';

    for (var obj of json) {
        res_str += '<tr><td>' + obj.x + '</td><td>' + obj.op + '</td><td>' + obj.y + '</td><td>' + eval('' + obj.x + obj.op + obj.y) + '</td></tr>';
    }
	
    res_str += '</table>'
    res.send(res_str);
});


app.listen(3000, function () {
    console.log('The application is available on port 3000');
});
});
