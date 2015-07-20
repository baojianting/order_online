$(document).ready(function(){
	
	$("#submit").click(function(){
		
		var phone = $("#phone").val();
		var product_name = $("#product-name").val();
		var username = $("#username").val();
		var province = $("#province").val();
		var city = $("#city").val();
		var county = $("#county").val();
		var extra = $("#extra").val();
		var detail_place = $("#detail-place").val();
		var phone_reg = /^0?1[3|4|5|8][0-9]\d{8}$/
		if (!phone_reg.test(phone)) {
			alert("手机号码有误");
			return;
		}
		if (username == "") {
			alert("收货人姓名不能为空");
			return;
		}
		if (detail_place == "") {
			alert("详细地址不能为空");
			return;
		}
		if (province == "省份" || city == "地级市") {
			alert("地区选择有误");
		}
		$.post("form", {"product":product_name, "username":username, "phone":phone, "place":province + city + county, "detail_place":detail_place, "extra":extra}, 
			function(result) {
				if (result == "ok") {
					alert("订单提交成功");
				} else {
					alert("订单提交失败");
				}
			});
		
		console.log("product-name:" + product_name + ";username:" + username + ";phone:" + phone + ";province:" + province + ";city:" + city + ";county:" 
		+ county + ";extra:" + extra + ";detail_place:" + detail_place);
		
	});
}); 