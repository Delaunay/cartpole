// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.


#include "UE4RLGameModeBase.h"


AUE4RLGameModeBase::AUE4RLGameModeBase() {
	bGameOver = false;
}

void AUE4RLGameModeBase::ResetLevel()
{
	K2_ResetLevel();
}

bool AUE4RLGameModeBase::HasMatchEnded() const
{
	return bGameOver;
}

void AUE4RLGameModeBase::GameOver()
{
	if (bGameOver == false)
	{
		K2_OnGameOver();
		bGameOver = true;
	}
}
