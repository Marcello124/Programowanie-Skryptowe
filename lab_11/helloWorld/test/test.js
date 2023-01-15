var supertest = require("supertest");
var assert = require('assert');
var fs = require('fs');

var chai = require('chai');
var expect = chai.expect;
chai.use(require('chai-json'));

const mongoose = require('mongoose')
const { Schema } = mongoose;
mongoose.connect('mongodb://127.0.0.1:27017/skryptowe', { useNewUrlParser: true, useUnifiedTopology: true });
const opSchema = new Schema({
  x: Number,
  y: Number,
  op: String
})
const Op = mongoose.model('Op', opSchema);

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function () {
  it('Response validation', function (done) {
    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('Output validation', function (done) {
    function testValue(res) {
      if (res.text != 'Hello World<br>1 + 2 = 3')
        throw new Error('response doesn\'t match')
    }

    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect(testValue)
      .end(done)
  });
});

describe('Json check', function () {
	
  it('Output validation', function (done) {
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "+"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "+"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "-"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "-"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "*"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "*"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 4,
      "y": 2,
      "op": "/"
    })
    expect('./operations.json').to.be.a.jsonFile().and.contain.jsonWithProps({
      "x": 20,
      "y": 4,
      "op": "/"
    })
    done()
  })
})

describe('GET /json/:name', function () {
  it('respond with html', function (done) {
    server
      .get('/json/operations.json')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('Values validation', function (done) {
    server
      .get('/json/operations.json')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect((res) => {
        var match = res.text.match(/(?<=<tr>).*?(?=<\/tr>)/gm)
        for (line of match) {
          var lm = line.match(/(?<=<td>).*?(?=<\/td>)/gm)
          if (lm !== null) {
            assert.equal(eval(lm[0] + lm[1] + lm[2]), lm[3])
          }
        }

      })
      .end(done)
  })
})

describe('GET /calculate/:operation/:x/:y', function () {
  it('Response validation', function (done) {
    server
      .get('/calculate/+/1/1')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('Check response code', function (done) {
    server
      .get('/calculate/x/1/1')
      .expect('Content-Type', /html/)
      .expect(400)
      .end(done)
  })

  it('Database check', function (done) {
    var x = getRandomInt(65535)
    var y = getRandomInt(65535)
    server
      .get('/calculate/-/' + x + '/' + y)
      .expect('Content-Type', /html/)
      .expect(200)
      .expect(async (res) => {
        var json = await Op.find({ x: x, y: y, op: '-' });

        expect(json.length).to.be.greaterThanOrEqual(1)
      })
      .end(done)
  })
})

describe('GET /results', function () {
  it('Response validation', function (done) {
    server
      .get('/results')
      .expect('Content-Type', /html/)
      .expect(200, done);
  });

  it('Values validation', function (done) {
    server
      .get('/results')
      .expect('Content-Type', /html/)
      .expect(200)
      .expect(async (res) => {
        var match = res.text.match(/(?<=<tr>).*?(?=<\/tr>)/gm)
        for (line of match) {
          var lm = line.match(/(?<=<td>).*?(?=<\/td>)/gm)
          if (lm !== null) {
            assert.equal(eval(lm[0] + lm[1] + lm[2]), lm[3])
          }
        }
      })
      .end(done)
  })
})
