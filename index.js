const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');
const adminRoutes = require('./routes/adminRoutes');


app.use(bodyParser.json());
app.use(cors());

app.set('view engine', 'ejs');

app.use(express.static('views'));




app.get('/', (req, res) => {
    res.render('index');
});

app.use('/admin', adminRoutes);



app.listen(process.env.PORT || 3000, () => {
    console.log('Server started on port 5000');
});


