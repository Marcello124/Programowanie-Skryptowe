const express = require('express');
const logger = require('morgan');
const cors = require('cors')

const app1 = express();
app1.use(logger('dev'));
app1.use(express.static('public'));
app1.use(cors())

app1.listen(3000, function () {
    console.log('The application is available on port 3000');
});

app1.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

app1.get('/getData', function (req, res) {
    let area = req.query.area;
    let location = req.query.location;

    https.get(`https://worldtimeapi.org/api/timezone/${area}/${location}`, (remoteRes) => {
        let data = '';
        remoteRes.on('data', (chunk) => {
            data += chunk;
        });

        remoteRes.on('end', () => {
            if (remoteRes.statusCode === 200) {
                let jsonData = JSON.parse(data);
                let dateTime = jsonData.datetime;
                res.json({
                    status: 'success',
                    dateTime: dateTime
                });
            } else if (remoteRes.statusCode === 429) {
                res.json({
                    status: 'overload',
                    message: 'The server is overloaded'
                });
            }
        });
    }).on("error", (err) => {
        res.json({
            status: 'error',
            message: err.message
        });
    });
});

console.log("To stop the server, press 'CTRL + C'");
