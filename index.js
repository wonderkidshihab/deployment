const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');


app.use(bodyParser.json());
app.use(cors());

// static files
app.use(express.static('dist'));





app.get('/', (req, res) => {
    res.sendFile('./dist/index.html', { root: __dirname });
});



app.listen(process.env.PORT || 5000, () => {
    console.log('Server started on port 5000');
});


