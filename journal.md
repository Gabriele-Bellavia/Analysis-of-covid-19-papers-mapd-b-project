So Dask cast its shadows upon their new adventure...

# Journal


# 25/06/2025
* CloudVeneto initialization.
* Tried to setup SSHCluster


# 26/06/2025

## Gio
The clusters spins up if directly initialized on the vm (I used `dask ssh localhost` to test it out)...

BUT by forwarding the remote ports to the local (not so sure about the TeCHniCaL language) `ssh -L [local_port]:localhost:[vm_port] -L [local_port]:localhost:[vm_port] [Host (such as vm_master)]`, I was able to launch `client = Client(localhost:[local_port]`, and do stuff with the cluster.

Mesmerising truly.
