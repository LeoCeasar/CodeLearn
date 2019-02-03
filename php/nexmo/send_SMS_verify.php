<?php
$sendUrl = "https://api.nexmo.com/verify/json?";
$verifyUrl = "https://api.nexmo.com/verify/check/json?";
$Key_id = "";
$Secret = "";

/*
   curl -X POST  https://api.nexmo.com/verify/json \
   -d api_key=7da4832a \
   -d api_secret=ab7fK2b9 \
   -d number=8615210812468 \
   -d brand="NexmoVerifyTest"

  array(2) { ["request_id"]=> string(32) "502458f7bbeb46b2b724cb0549639ff9" ["status"]=> string(1) "0" }
 */
function sendVerifySms($to)
{
	global $sendUrl,$Key_id,$Secret;

	$body = iconv("gb2312", "utf-8//IGNORE", $body);
	$send_body="api_key=".$Key_id."&api_secret=".$Secret."&number=".$to."&brand=MITBBS";
	$curl=curl_init();
	curl_setopt($curl,CURLOPT_URL,$sendUrl);
	curl_setopt($curl,CURLOPT_HEADER,0);
	curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
	curl_setopt($curl,CURLOPT_POST,1);
	curl_setopt($curl,CURLOPT_POSTFIELDS,$send_body);

	$data=curl_exec($curl);
	$ret = array();
	if (empty($data))
	{
		$curl_error = curl_errno($curl);
		$ret['error'] = -98;
		$ret['msg'] = "curl error code:".$curl_error;
	}
	else
	{
		$json_data=json_decode($data,true);
		if ($json_data['status'] == 0)
		{
			$ret['error'] = 0;
		}
		else
		{
			$ret['error'] = -99;
			$ret['msg'] = $json_data['error_text'];
		}
		$ret['request_id'] = $json_data['request_id'];
	}


	//return $json_data;
	curl_close($curl);
	return $ret;
}
/*
   curl -X POST  https://api.nexmo.com/verify/check/json \
   -d api_key=7da4832a \
   -d api_secret=ab7fK2b9 \
   -d request_id="REQUEST_ID" \
   -d code=CODE

array(5) { ["request_id"]=> string(32) "502458f7bbeb46b2b724cb0549639ff9" ["status"]=> string(1) "0" ["event_id"]=> string(16) "1300000003ADE324" ["price"]=> string(10) "0.10000000" ["currency"]=> string(3) "EUR" } 
 */
function checkSms($request_id,$code)
{
	global $verifyUrl,$Key_id,$Secret;

	$body = iconv("gb2312", "utf-8//IGNORE", $body);
	$send_body="api_key=".$Key_id."&api_secret=".$Secret."&request_id=".$request_id."&code=".$code;
	$curl=curl_init();
	curl_setopt($curl,CURLOPT_URL,$verifyUrl);
	curl_setopt($curl,CURLOPT_HEADER,0);
	curl_setopt($curl,CURLOPT_RETURNTRANSFER,1);
	curl_setopt($curl,CURLOPT_POST,1);
	curl_setopt($curl,CURLOPT_POSTFIELDS,$send_body);

	$data=curl_exec($curl);
	$json_data=json_decode($data,true);
	$ret = array();
	if (empty($data))
	{
		$curl_error = curl_errno($curl);
		$ret['error'] = -98;
		$ret['msg'] = "curl error code :".$curl_error;
	}
	else
	{
		if ($json_data['status'] == 0)
		{
			$ret['error'] = true;
		}
		else
		{
			$ret['error'] = false;
			$ret['msg'] = $json_data['error_text'];
		}
		$ret['request_id'] = $json_data['request_id'];
	}

	curl_close($curl);
	//return $json_data;
	return $ret;
}

$type = $_POST['type'];

if(!strcasecmp($type, "send"))
{
	$tel = $_POST['tel'];
	$res = sendVerifySms($tel);
	
	echo json_encode($res);
}
else if (!strcasecmp($type, "check"))
{
	$request_id = $_POST['request_id'];
	$code = $_POST['code'];

	$res = checkSms($request_id,$code);

	echo json_encode($res);
}
?>
