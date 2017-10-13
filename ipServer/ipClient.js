const dgram = require("dgram")
const client = dgram.createSocket("udp4")

const DES_IP = "192.168.1.255"
const SEND_PORT = 7000
const RECV_PORT = 7001
const sendData = "IP_REQ"

client.on("error", (err) => {
    console.log("client error: ", err)
    client.close()
})

//client.setBroadcast(true)
client.send(sendData, 0, sendData.length, SEND_PORT, DES_IP)

client.on("message", (msg, rinfo) => {
    console.log(`client GOt ${message} from ${rinfo.address}:${rinfo.port} ` )
})

// client.bind(RECV_PORT)
//client.close()
