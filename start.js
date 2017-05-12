var express = require('express');
var ejs = require('ejs');
var path = require('path');

var weibo = express();

weibo.use('/static', express.static('public'));
weibo.use('/views', express.static('public'));
weibo.use('/dist', express.static('dist'));
weibo.use('/public', express.static('public'));

weibo.engine('html', ejs.__express);
weibo.set('view engine', 'html');
weibo.set('views', __dirname + '/src/views');

weibo.get('/', function (req, res) {
  res.render('index.html');
});

weibo.get('/register',function (req, res) {
  res.render('register.html');
})

weibo.listen(8000, function (req, res) {
  console.log("http://localhost:8000");
})