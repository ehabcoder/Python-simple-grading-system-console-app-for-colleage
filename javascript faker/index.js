const express = require('express')
const { faker } = require('@faker-js/faker');

const objectstocsv = require('objects-to-csv')

const fs = require("fs")

const app = express()

var data = [];
for (let i = 0; i < 100; i++) {
    data.push({
        id: i + 1,
        name: faker.name.findName(),
        midterm_grade: +Math.ceil(Math.random() * (22 - 1) + 1),
        classwok_grade: +Math.ceil(Math.random() * (100 - 1) + 1)
    })
}


const PORT = process.env.PORT || 5000

app.get('/', async(req, res) => {
    const csv = new objectstocsv(data);
    // Save to file:
    await csv.toDisk('./test.csv');


    res.download("./test.csv", () => {

        fs.unlinkSync("./test.csv")

    })
})


app.listen(PORT, () => {
    console.log("app is listening on port 5000")
})
