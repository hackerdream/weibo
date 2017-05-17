var express = require('express');
var ejs = require('ejs');
var path = require('path');

var weibo = express();

<<<<<<< HEAD
weibo.use('/app/templates/views', express.static('views'));
weibo.use('/dist', express.static('dist'));
weibo.use('/app/templates/public', express.static('public'));
=======
weibo.use('/app/template/views', express.static('public'));
weibo.use('/dist', express.static('dist'));
weibo.use('/app/template/public', express.static('public'));
>>>>>>> 0188621859fd820ed90df2693b69cb9b402ae495

weibo.engine('html', ejs.__express);
weibo.set('view engine', 'html');
weibo.set('views', __dirname + '/templates/src/views');

weibo.get('/', function (req, res) {
  res.render('index.html');
});

weibo.get('/register',function (req, res) {
  res.render('register.html');
})

weibo.get('/u/:uid',function (req, res) {
  res.render('weibo.html')
})

weibo.get('/main/:uid',function (req, res) {
  res.render('main.html')
})

weibo.listen(8000, function (req, res) {
  console.log("http://localhost:8000");
})