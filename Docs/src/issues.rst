Known Issues
============

Cartpole Bugs
~~~~~~~~~~~~~

* Pole Initial push is ineffective after a few level restarts, might be related to the PlayerController issue


UE4ML Bugs
~~~~~~~~~~

* PlayerController is not set upon level reset. The training script is sending actions but UE4ML agent does nothing
because his PlayerController reference is null.

* U4ML does not launch on standalone builds
