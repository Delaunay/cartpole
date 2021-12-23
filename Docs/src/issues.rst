Known Issues
============

Cartpole Bugs
~~~~~~~~~~~~~

* Pole Initial push is in effective after a few level restart


UE4ML Bugs
~~~~~~~~~~

* PlayerController is not set upon level reset. The training script is sending actions but UE4ML agent does nothing
because his PlayerController reference is null.

