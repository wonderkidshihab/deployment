const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');


app.use(bodyParser.json());
app.use(cors());




app.get('/', (req, res) => {
    res.sendFile('./index.html', { root: __dirname });
});



app.listen(process.env.PORT || 5000, () => {
    console.log('Server started on port 5000');
});


