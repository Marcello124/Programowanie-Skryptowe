const fs = require('fs');

const path = process.argv[2];

try {
    const stat = fs.statSync(path);

    if (stat.isFile()) {
        console.log(`"${path}" is a file:`)
        console.log(fs.readFileSync(path, 'utf8'))
    }
    else if (stat.isDirectory) {
        console.log(`"${path}" is a directory`)
    }
} catch (err) {
    console.error(`"${path}" does not exist`)
}