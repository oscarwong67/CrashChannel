var express = require('express');
var path = require('path');
module.exports = app;

var express = require('express'); 
var app = express(); 
  
app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 

app.get('/name', callName); 
  
function callName(req, res) { 
    console.log(req.query.url);
    var spawn = require("child_process").spawn; 
      
    var process = spawn('python',["../label_imagear.py", decodeURI(req.query.url)]); 
  
    process.stdout.on('data', function(data) { 
        res.send(data.toString()); 
    } ) 
} 
  