const ip = require("ip")
const os = require("os")

const SERVER_HOSTNAME = os.hostname()
const SERVER_IP = ip.address()

console.log(SERVER_HOSTNAME)
console.log(SERVER_IP)