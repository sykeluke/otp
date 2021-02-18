from zeep import Client
from zeep import xsd
from zeep.plugins import HistoryPlugin
stationlist="For CRS codes look on this site and click on the letter http://www.railwaycodes.org.uk/crs/crs0.shtm"
print("Enter the train station CRS you would like to view the info for :")
print(stationlist)
crs = input("Enter a VALID CRS code here: ")
LDB_TOKEN='40bc85b4-bf40-4a97-82d5-a961c3d1fc15'
WSDL = 'http://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'



if LDB_TOKEN == '':
    raise Exeption("Please configure your token")

history = HistoryPlugin()

client = Client(wsdl=WSDL, plugins=[history])

header = xsd.Element(
 '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
 xsd.ComplexType([
     xsd.Element(
            '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}TokenValue',
            xsd.String()),
     ])
 )
header_value = header(TokenValue=LDB_TOKEN)

res = client.service.GetDepartureBoard(numRows=20, crs=crs, _soapheaders=[header_value])
print("Trains at " + res.locationName)
print("===============================================================================")

services = res.trainServices.service

i = 0
while i < len(services):
    t = services[i]
    print(t.std + " to " + t.destination.location[0].locationName + " - " + t.etd)
    i += 1
    from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
