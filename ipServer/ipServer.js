const dgram = require("dgram")
const os = require("os")
const ip = require("ip")
const server = dgram.createSocket("udp4")

const SERVER_HOSTNAME = os.hostname()
const SERVER_IP = ip.address()
const SEND_PORT = 7001
const RECV_PORT = 7000
const IP_REQ = "IP_REQ"
const resData = `SERVER_IP: ${SERVER_IP}, SERVER_HOSTNAME: ${SERVER_HOSTNAME}`

server.on("error", (err) => {
    console.log("server error: ", err)
    server.close()
})
server.on("message", (message, rinfo) => {
    var CLIENT_IP = rinfo.address
    console.log(`server GOt ${message} from ${CLIENT_IP} ` )
    console.log(resData)
    // If there is a REQ from tablet then send a server ip and hostname back
    if(message == IP_REQ) {
        server.send(resData, 0, resData.length, SEND_PORT, CLIENT_IP)
    }
})
server.on("listening", () => {
    const address = server.address()
    console.log(`server listening ${address.address}:${address.port}`)
})

server.bind(RECV_PORT)
