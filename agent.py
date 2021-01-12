from proxmoxer import ProxmoxAPI
import json

# IMPORTANT: Target Machine needs to have a package named qemu-guest-agent.
# After installing this package, Enable agent on web interface (Options > Qemu Guest Agent)

with open('config.json') as json_file:
    data = json.load(json_file)

# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: get_time(0, 111) for getting time of kvm node id 111 (192.168.1.11)
def get_time(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).agent.get('get-time')
    print(result)

# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: get_timezone(0, 111) for getting time zone of kvm node id 111 (192.168.1.11)
def get_timezone(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).agent.get('get-timezone')
    print(result)

# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: get_osinfo(0, 111) for getting os info of kvm node id 111 (192.168.1.11)
def get_osinfo(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).agent.get('get-osinfo')
    print(result)

# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: get_net_int(0, 111) for getting network info of kvm node id 111 (192.168.1.11)
def get_net_int(kvm, vid)
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).agent.get('network-get-interfaces')
    print(result)

# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: shutdown(0, 111) for shutting down of kvm node id 111 (192.168.1.11)
def shutdown(kvm, vid)
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).agent.post('shutdown')
    print(result)
