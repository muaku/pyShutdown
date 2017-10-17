const dgram = require("dgram")
const ip = require("ip")
const client = dgram.createSocket("udp4")

const SEND_PORT = 7000
const RECV_PORT = 7001
const sendData = "IP_REQ"

var getBroadcast_IP = (myIP) => {
    var ipArray = myIP.split(".")
    return ipArray[0] + "." + ipArray[1]+ "." + ipArray[2]+ "." +"255"
}
const BROADCAST_IP = getBroadcast_IP(ip.address())
console.log("BROADCAST_IP: ", BROADCAST_IP)

client.bind(SEND_PORT, () => {
    client.setBroadcast(true)   // Important, if not data will not be sent
})

client.on("error", (err) => {
    console.log("client error: ", err)
    client.close()
})

//client.setBroadcast(true)
client.send(sendData, 0, sendData.length, SEND_PORT, BROADCAST_IP)

client.on("message", (message, rinfo) => {
    console.log(`client GOt ${message} from ${rinfo.address}:${rinfo.port} ` )
    //client.close()
})



