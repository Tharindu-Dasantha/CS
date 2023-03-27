const people = ['yoshi', 'ryu', 'chun-li', 'mario'];
const ages = [28, 25, 30, 35];

console.log(people);

// Exporting file
module.exports = {
    people: people, // when both are the same name you can just type the name
    ages
};