// call the packages we need
var express = require('express'); // call express
var app = express(); // define our app using express
var bodyParser = require('body-parser');
var pyShell = require('python-shell');
var jsonfile = require('jsonfile')
var file = 'config.json'

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.use('/styles', express.static(__dirname + '/styles'));
app.set('view engine', 'pug');

var port = 9090; // set our port
var router = express.Router(); // get an instance of the express Router

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get('/config', function(req, res) {
    var fs = require('fs');
    var configString = fs.readFileSync('config.json', 'utf8');
    res.json(configString);
});

router.route('/order').post(function(req, res) {
    var fs = require('fs');
    var configJSON = JSON.parse(fs.readFileSync('config.json', 'utf8'));
    var product = req.body.product;

    var options = {
        mode: 'text',
        pythonPath: '/usr/bin/python3',
        scriptPath: './',
        args: [username, password, prodURL]
    };


    pyShell.run('run.py', options, function(err, results) {
        if (err) {
            //send BAD ORDER response
            res.json({
                'OrderStatus': '0'
            });
        } else {
            //send GOOD ORDER response
            res.json({
                'OrderStatus': '1'
            });
        }
    });
});

router.get('/', function(req, res) {
    jsonfile.readFile(file, function(err, obj) {
        res.render('index', {
            username: obj["amazon-username"],
            password: obj["amazon-password"],
            wifinetwork: obj["wifi-network"],
            wifipassword: obj["wifi-password"],
            name1: obj["1"]["name"],
            url1: obj["1"]["URL"],
            name2: obj["2"]["name"],
            url2: obj["2"]["URL"],
            name3: obj["3"]["name"],
            url3: obj["3"]["URL"],
            name4: obj["4"]["name"],
            url4: obj["4"]["URL"]
        });
    })
})

router.route('/submit').post((req, res) => {
  //console.log(req.body)
  var result = {}
  result["amazon-username"] = req.body["amazon-username"]
  result["amazon-password"] = req.body["amazon-password"]
  result["wifi-network"] = req.body["wifi-network"]
  result["wifi-password"] = req.body["wifi-password"]
  result["1"] = {"name": req.body.name1, "URL": req.body.url1}
  result["2"] = {"name": req.body.name2, "URL": req.body.url2}
  result["3"] = {"name": req.body.name3, "URL": req.body.url3}
  result["4"] = {"name": req.body.name4, "URL": req.body.url4}

  console.log(result)
  jsonfile.writeFile(file, result, function (err) {
    console.error(err)
  })
	res.render('result', {
		username: req.body["amazon-username"],
		name1: req.body["name1"],
            	url1: req.body["url1"],
            	name2: req.body["name2"],
            	url2: req.body["url2"],
            	name3: req.body["name3"],
            	url3: req.body["url3"],
            	name4: req.body["name4"],
            	url4: req.body["url4"]

	});
})

app.use('/pi-order', router);
app.listen(port);
console.log('Magic happens on port ' + port);
