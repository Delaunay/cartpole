Cartpole
========

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/yQzQcLWakW4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


This project demonstrates how to use MLAdapter to create a reinforcement learning
environment for machine learning.

From `Wikipedia <https://en.wikipedia.org/wiki/Machine_learning>`_

   Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data.
   It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data,
   known as training data, in order to make predictions or decisions without being explicitly programmed to do so.

We will recreate the famous `Cartpole environment <https://gym.openai.com/envs/CartPole-v0/>`_,
which is a very simple environment that is straight forward to implement and yet will enable us
to focus on how to setup a project for machine learning, then we will train a neural network to play our game.

The notions seen in this project are applicable to any games made using UnrealEngine.


Why UnrealEngine
~~~~~~~~~~~~~~~~

* UnrealEngine is essentially open-source. The source is proprietary and technically private but you can get access by simply creating an Epic Account.
* The licencing is perfect for academia (See Creators LICENSE)
* All UnrealEngine technologies available to develop new cutting edge environments
* Easy to port research into the real world
* Easy to develop and redistribute environments


About MLAdapter
~~~~~~~~~~~

MLAdapter was made to be as unintrusive as possible, this means that
you will need to modify very little of your game (if anything) to turn it into
a reinforcement learning environment.

The main requirements that would need to be addressed are:

* Reward: a value that quantify how well your agent/neural network is doing (i.e a score)
* ResetLevel: the ability to restart a level when the agent dies

Because of it unintrusive design, ML-researchers will spend their time on the python side
focusing on the machine learning side while developers can focus on the environment itself.
While the cartpole environment is using a bit of C++ most of it was written to expose functionallity to
blueprint, as such very little C++ knownledge is necessary to build a custom environment.

Installation
~~~~~~~~~~~~

.. note::

   This tutorial use UnrealEngine 4.27.2, newer version should work as well


.. note::

   UE5 renamed UE4ML to MLAdapter



1. Install UnrealEngine
2. Create a new blank C++ project

   * Enable MLAdapter plugin (Setting > Plugins > UE4 support for ML)


.. toctree::
   :maxdepth: 2

   src/game
   src/launching
   src/training
   src/packaging
   src/issues


References
~~~~~~~~~~

* `UE4ML Documentation <https://docs.unrealengine.com/4.27/en-US/API/Plugins/UE4ML/>`_
* `ML Adapter Documentation <https://docs.unrealengine.com/5.0/en-US/5.0/en-US/5/en-US/API/Plugins/MLAdapter>`_
* `OpenAI Gym <https://gym.openai.com/>`_
* `PyTorch Documentation <https://pytorch.org/>`_


Code Documentation
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   api/cartpole
   python/index

