var expect = chai.expect;
var suma = 0

function sum(x) {
    let number = ''
    for (let symbol of String(x)) {
        if (isNaN(symbol)) {
            break
        }
        number += symbol
    }
    suma += Number(number)
    return suma
}

function sum_of_digits(x) {
    let result = 0
    for (let symbol of String(x)) {
        if (isNaN(symbol)) {
            continue
        }
        result += Number(symbol)
    }
    return result
}

function char_count(string) {
    let count = 0
    for (let symbol of String(string)) {
        if (isNaN(symbol)) {
            count++
        }
    }
    return count
}

var x = window.prompt()
while (x != null) {
    document.write(`\t${sum(x)}\t${char_count(x)}\t${sum_of_digits(x)}<br>`)
    x = window.prompt()
    
}

describe('The sum() function', function() {
    it('Returns 4 for 2+2', function() {
        expect(sum(2)).to.equal(2);
    });
    it('Returns 0 for -2+2', function() {
        expect(sum('a2')).to.equal(2);
    });
    it('Returns 3 for 111', function() {
        expect(sum_of_digits(111)).to.equal(3);
    });
    it('Returns 2 for aa22', function() {
        expect(char_count('aaa22aa')).to.equal(5);
    });
})