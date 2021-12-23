
base = /media/setepenre/Games/
project = cartpole/Cartpole.uproject
engine = UnrealEngine/Engine/Binaries/Linux/UE4Editor
editor = $(base)/$(engine)

train:
	python cartpole/train.py --project $(base)/$(project) --exec $(editor)


cook:
	# https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Deployment/Cooking/
	# saved in <Game>/Saved/Sandboxes/Cooked-<Platform>
	$(editor) $(base)/$(project) -run=cook
