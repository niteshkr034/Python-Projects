import speedtest

test = speedtest.Speedtest()
print("Loading available server...")
test.get_servers() #Featching server list

print("Selecting best server...")
best = test.get_best_server()

print(f"Selected: {best['host']} located in: {best['country']}")

print("Testing download speed...")
dlresult = str ("{:.2f}".format(test.download()/1024/1024)) + " Mb/s"
print(dlresult)
print("Testing upload speed... \n----------------------------")
upresult = str ("{:.2f}".format(test.upload()/1024/1024)) + " Mb/s"

presult = str(test.results.ping)+ " ms"
print("Download Speed: " + dlresult)
print("Upload Speed: "+ upresult)
print("Ping " + presult)
print("----------------------------")
