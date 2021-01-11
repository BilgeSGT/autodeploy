# Manage Proxmox Virtual Environments Easily

### You can do VM & Snapshot operations and get info about status
A config file named 'config.json' is needed for using this tool.
You can add as many VM as you want as long as you add them in config file properly.
An example config file is:

`{
    "VM": [
        {
            "ip": "192.168.1.1:8080",
            "user": "root@pam",
            "pass": "Password123",
            "node": "KVM"
        },
        {
            "ip": "192.168.1.1:8080",
            "user": "root@pam",
            "pass": "Password123",
            "node": "KVM2"
        }
    ]
}`

In this above example we have 2 nodes which are named KVM and KVM2.
KVM has an IP 192.168.15.1 and KVM2 has an IP which is 192.168.14.1.
There are several functions that has been implemented already.
There will be more functions to be added in this project.
Implemented functions can be found below with examples using above config.

## VM Operations
### List Virtual Machines

### Start a Virtual Machine
`start_vm(kvm, vid):`
Example usage: start_vm(0, 119) for starting kvm node id 119 (192.168.1.19)

### Stop a Virtual Machine
`stop_vm(kvm, vid):`
Example usage: reboot_vm(0, 119) for stopping kvm node id 119 (192.168.1.19)

### Reboot a Virtual Machine
`reboot_vm(kvm, vid):`
Example usage: reboot_vm(0, 119) for rebooting kvm node id 119 (192.168.1.19)

### Status of a Virtual Machine
`status_vm(kvm, vid):`
Example usage: status_vm(0, 119) for rebooting kvm node id 119 (192.168.1.19)

### Shutdown a Virtual Machine
`shutdown_vm(kvm, vid):`
Example usage: shutdown_vm(0, 119) for shutting down kvm node id 119 (192.168.1.19)

### Create a Virtual Machine
(Not yet completed) `cre_vm(kvm, vid, conf):` 
Example usage: del_vm(0, 119, {}) for deleting kvm node id 119 (192.168.1.19)

### Delete a Virtual Machine
`del_vm(kvm, vid):` function
Example usage: del_vm(0, 119) for deleting kvm node id 119 (192.168.1.19)

## Snapshot Operations
### Create Snapshot of a Virtual Machine
(Not yet completed) `cre_ss(kvm, vid, sname):`
Example usage: `cre_vm(0, 119, 'debian')` for creating snapshot of a VM id 119 (192.168.1.19)

### Delete a Snapshot of a Virtual Machine
`del_ss(kvm, vid, sname):`
Example usage: `del_ss(0, 119, 'debian')` for deleting a snapshot of a kvm node id 119 (192.168.1.19)

### Rollback to a Snapshot of a Virtual Machine
`roll_ss(kvm, vid, sname):` Rollback to given snapshot, sname = snapshot name (e.g 'debian')
Example usage: `roll_ss(0, 119, 'debian')` for rolling back to a snapshot of a kvm node id 119 (192.168.1.19)

### List Snapshot(s) of a Virtual Machine
`list_ss(kvm, vid):`
Example usage: `list_ss(0, 119)` for listing snapshots of kvm node id 119 (192.168.1.19)

## Disk Operations of Nodes
### Get Disk information of a Node 
Get disk info in detail for VMs.
`disk_info(kvm):`
Example usage: disk_info(0) for getting disk info of a kvm (192.168.1.x)

## Network Operations
### Get Network information of a Node
Functions for getting info about networks
`net_info(kvm):`
Example usage: net_info(0) for getting network info of a kvm (192.168.1.x)
