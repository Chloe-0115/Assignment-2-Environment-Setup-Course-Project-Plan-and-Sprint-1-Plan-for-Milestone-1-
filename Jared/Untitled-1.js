// Japp.js
const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
let quotes = [];

// Load quotes from the file
fs.readFile(path.join(__dirname, 'quotes.txt'), 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading quotes file:', err);
        return;
    }
    quotes = data.split('\n').filter(quote => quote.trim() !== '');
});

// Endpoint to get a random quote
app.get('/quote', (req, res) => {
    if (quotes.length === 0) {
        return res.status(500).send('No quotes available');
    }
    const randomIndex = Math.floor(Math.random() * quotes.length);
    res.send(quotes[randomIndex]);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});