var page = require('webpage').create();

//viewportSize 视区大小
//clipRect视区中裁剪的矩形的大小
page.viewportSize = {width:1024, height:768};
page.clipRect = {top:0, left:0, width:512, height:256};

page.open('http://www.cnblogs.com/qiyeboy/',
		function(status){
			console.log("status:" + status);
			if (status === "success"){
				page.render('qiyeE.png');
			}
			phantom.exit();
		});
