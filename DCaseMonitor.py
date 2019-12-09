import json

import sys
import ssl


if sys.version_info[0] >= 3:
	import urllib.request as request
	import urllib.parse as parse
else:
	import urllib2 as request
	import urllib  as parse

class DCaseMonitor:
	Goal = "Goal"
	Plan = "Plan"
	Suppose = "Suppose"
	Evidence = "Evidence"
	Unachieved = "Unachieved"
	Monitor = "Monitor"
	Assumption = "Assumption"
	Justification = "Justification"
	External = "External"
	Pendding = "Pendding"

	def __init__(self, dcaseID=None, partsID=None, url=None, sslIgnore=False ):
		if url is None:
			self.baseURL = "https://mlab.ce.cst.nihon-u.ac.jp/dcase/api/"
		else:
			self.baseURL = url

		if dcaseID is None:
			self.dcaseID = None
		else:
			self.dcaseID = dcaseID

		if partsID is None:
			self.partsID = None
		else:
			self.partsID = partsID

		self.sslIgnore = sslIgnore

	def uploadData( self, obj, partsID=None, dcaseID=None ):
		url = self.baseURL + "/uploadTableValue.php"
		jsonStr = json.dumps(obj,separators=(',', ':'))

		if dcaseID is None:
			dcaseID = self.dcaseID

		if partsID is None:
			partsID = self.partsID

		if self.sslIgnore:
			ctx = ssl.create_default_context()
			ctx.check_hostname = False
			ctx.verify_mode = ssl.CERT_NONE
		if ( dcaseID is not None ) and ( partsID is not None ):
			data = {
				"dcaseID" : dcaseID,
				"partsID" : partsID,
				"data" : jsonStr
			}

			postData = parse.urlencode(data).encode('utf-8')
			headers = {
				'Content-Type': 'application/x-www-form-urlencoded',
			}
			print(url)
			req = request.Request(url, postData, headers)
			if self.sslIgnore:
				res = request.urlopen(req, context=ctx)
			else:
				res = request.urlopen(req)
			body = res.read().decode('utf-8')

			return( json.loads( body ) )

		return( None )

	def uploadNodeState( self, partsID, state=True, detail="", kind=None, dcaseID=None ):
		url = self.baseURL + "/uploadNodeState.php"

		if dcaseID is None:
			dcaseID = self.dcaseID

		if kind is None:
			kind = self.Pendding

		if self.sslIgnore:
			ctx = ssl.create_default_context()
			ctx.check_hostname = False
			ctx.verify_mode = ssl.CERT_NONE
		if ( dcaseID is not None ) and ( partsID is not None ):
			data = {
				"dcaseID" : dcaseID,
				"partsID" : partsID,
				"kind" : kind,
				"state" : state,
				"detail" : detail,
			}

			postData = parse.urlencode(data).encode('utf-8')
			headers = {
				'Content-Type': 'application/x-www-form-urlencoded',
			}
			print(url)
			req = request.Request(url, postData, headers)
			if self.sslIgnore:
				res = request.urlopen(req, context=ctx)
			else:
				res = request.urlopen(req)
			body = res.read().decode('utf-8')

			return( json.loads( body ) )

		return( None )
