import DCaseMonitor as dcaseCom
import time

dcaseID = "ySxapgkpdt4SdS9hymt2cz4zzg46CPMpEtqloNd_SmE_"
partsID = "Parts_fassfcbj"
partsID2 = "Parts_nlyevduo"

dcase = dcaseCom.DCaseMonitor( dcaseID, partsID, sslIgnore=True )
dcase2 = dcaseCom.DCaseMonitor( dcaseID, partsID2, sslIgnore=True )
accuracy = 0.98
reliability = 0.999
while True:
	data = [
		{
			"Key": "Accuracy",
			"Value": accuracy,
        	"Color": "#FF0000",
			"Font":16,
			},
			]

	data2 = [
		{
		"Key": "Reliability",
		"Value": reliability,
        "Color": "#FF0000",
		"Font":16,
		},
		]


	if accuracy >= 0.95:
		ret = dcase.uploadNodeState( partsID, state=True, detail='Accuracy of Pattern Recognition', kind=dcase.Evidence )
		print("return", ret)
		ret = dcase.uploadData( data, partsID=ret["partsID"] )
		print("return", ret)
		accuracy -= 0.01
		time.sleep(5)
	else:
		ret = dcase.uploadNodeState( partsID, state=False, detail='Accuracy of Pattern Recognition', kind=dcase.Evidence )
		print("return", ret)
		if reliability >= 0.99:
			ret = dcase2.uploadNodeState( partsID2, state=True, detail='Reliability', kind=dcase.Evidence )
			print("return", ret)
			ret = dcase2.uploadData( data2, partsID=ret["partsID"] )
			print("return", ret)
			time.sleep(5)
			reliability -=0.001
		else:
			ret = dcase2.uploadNodeState( partsID2, state=False, detail='Reliability', kind=dcase.Evidence )
			print("return", ret)
