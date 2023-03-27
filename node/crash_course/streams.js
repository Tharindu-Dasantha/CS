const fs = require('fs');

 const readSteram = fs.createReadStream('./docs/text3.txt',{encoding: 'utf-8'});

//  readSteram.on('data', (chunk) => {
//      console.log('---- New Chunk ----');
//      console.log(chunk);
// });

const writeSteram = fs.createWriteStream('./docs/text4.txt');

// writeSteram.on('data', (chunk) => {
//     writeSteram.write('\nNew Chunk\n');
//     writeSteram.write(chunk);
// });

readSteram.pipe(writeSteram);