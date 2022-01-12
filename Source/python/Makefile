
base = /media/setepenre/Games/
project = cartpole/Cartpole.uproject
engine = UnrealEngine/Engine/Binaries/Linux/UnrealEditor-Linux-Debug-Cmd
editor = $(base)/$(engine)
cooked = ""

train-editor-launch:
	# does not work anymore, the editor is launched but it does not play the game
	python cartpole/train.py --project $(base)/$(project) --exec $(editor) --launch

train-editor-attach:
	python cartpole/train.py --no-launch

train-cooked-launch:
	python cartpole/train.py --exec $(cooked) --launch

train-cooked-attach:
	python cartpole/train.py --no-launch

cook:
	# https://docs.unrealengine.com/4.27/en-US/SharingAndReleasing/Deployment/Cooking/
	# saved in <Game>/Saved/Sandboxes/Cooked-<Platform>
	$(editor) $(base)/$(project) -run=cook
