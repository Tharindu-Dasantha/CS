// importing libraries
const fs = require("fs");

// read files
// fs.readFile('./docs/text.txt', (err, data) => {
//     // this is a callback function
//     if (err) {
//         console.log(err);
//     }
//     console.log(data.toString());
// });

// console.log('last line');

// write files
// fs.writeFile('./docs/text2.txt', "hello world", (err, data) => {
//     console.log("file is written");
// });

// directories
// if (!fs.existsSync("./assets")) {
//    fs.mkdir('./assets', (err) => {
//       if (err) {
//            console.log(err);
//        }
//        console.log('create');
//   })
// } else {
//     fs.rmdir('./assets', (err) => {
//         if (err) {
//             console.log(err);
//         }
//     });
// }

// deleting files
if (fs.existsSync("./docs/delete.txt")) {
    fs.unlink('./docs/delete.txt', (err) => {
        if (err) {
            console.log(err);
        }
        console.log('file deleted');
    });
}