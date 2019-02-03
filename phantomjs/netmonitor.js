var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();

page.onREspirceRequested = function(request){
	console.log('Request ' + JSON.stringify(response,undefined, 4));
};

page.onResourceReceived = function(response){
	console.log('recieve ' + JSON.stringify(response, undefined, 4));
};

page.open(url);

//phantom.exit();
