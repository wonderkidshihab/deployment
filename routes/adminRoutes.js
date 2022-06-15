const Router = require('express').Router;
const router = new Router();
const expressSession = require('express-session');
const cookieParser = require('cookie-parser');


router.use(expressSession({
    secret: 'mySecret',
    resave: false,
    saveUninitialized: false,
    cookie: {
        maxAge: 1000 * 60 * 60 * 24 * 7 // 1 week
    }
}));

router.use(cookieParser());



router.get('/', (req, res) => {
    if (req.session.user) {
        res.render('admin/index');
    } else {
        res.render('../views/admin/loginPage');
    }
});

router.post('/login', (req, res) => {
    if (req.body.username === 'admin' && req.body.password === 'admin') {
        req.session.user = 'admin';
        res.redirect('/admin');
    } else {
        res.redirect('/admin');
    }

});

module.exports = router;