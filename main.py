import json
from proxmoxer import ProxmoxAPI
# import requests
# import argparse


with open('config.json') as json_file:
    data = json.load(json_file)



def list_vm():
    print("List of all VMs across all nodes:")
    for i in data['VM']:
        proxmox = ProxmoxAPI(i['ip'], user=i['user'], password=i['pass'], verify_ssl=False)
        for vm in proxmox.cluster.resources.get(type='vm'):
            print("{0}. {1} => {2}".format(vm['vmid'], vm['name'], vm['status']))


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: start_vm(0, 111) for starting kvm node id 111 (192.168.1.11)
def start_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).status.start.post()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: reboot_vm(0, 111) for stopping kvm node id 111 (192.168.1.11)
def stop_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).status.stop.post()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: reboot_vm(0, 111) for rebooting kvm node id 111 (192.168.1.11)
def reboot_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).status.reboot.post()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: shutdown_vm(0, 111) for shutting down kvm node id 111 (192.168.1.11)
def shutdown_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).status.shutdown.post()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: status_vm(0, 111) for rebooting kvm node id 111 (192.168.1.11)
def status_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).status.current.get()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: list_ss(0, 111) for listing snapshots of kvm node id 111 (192.168.1.11)
def list_ss(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).snapshot.get()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: roll_ss(0, 111, 'debian') for rolling back to a snapshot of a kvm node id 111 (192.168.1.11)
# Rollback to given snapshot, sname = snapshot name (e.g 'debian')
def roll_ss(kvm, vid, sname):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).snapshot(sname).rollback.post()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: del_ss(0, 111, 'debian') for deleting a snapshot of a kvm node id 111 (192.168.1.11)
def del_ss(kvm, vid, sname):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).snapshot(sname).delete()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: disk_info(0) for getting disk info of a kvm (192.168.1.x)
def disk_info(kvm):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).storage.get()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: net_info(0) for getting network info of a kvm (192.168.1.x)
def net_info(kvm):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).network.get()
    print('Result: ', result)


# Give kvm input 0 for first node, 1 for second node. Add new nodes to config file
# Example usage: del_vm(0, 111) for deleting kvm node id 111 (192.168.1.11)
def del_vm(kvm, vid):
    proxmox = ProxmoxAPI(data['VM'][kvm]['ip'], user=data['VM'][kvm]['user'], password=data['VM'][kvm]['pass'], verify_ssl=False)
    result = proxmox.nodes(data['VM'][kvm]['node']).qemu(vid).delete()
    print('Result: ', result)
