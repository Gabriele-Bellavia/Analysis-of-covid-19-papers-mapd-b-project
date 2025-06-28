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


# 27/06/2025

Since we were using too many resources we shrank the VMs. They stopped working because of this, but now they seem fine. The bottom line is: never listen to GG.

## Gio

Set up a NFS. Now the cluster should be up perfectly up to use with no issue. I expect many problems to come.


# 28/06/2025

We can now sorta read files? Before delaying the functions the scheduler would have taken ages to compute, now it should be faster, maybe it's just all delayed...

## Gio

Found a list of stopwords, I didn't really checked it, a much dangerous behaviour. Seemed to work, now we should count the words, maybe a foldby?
