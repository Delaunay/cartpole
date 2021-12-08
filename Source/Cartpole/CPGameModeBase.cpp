// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.


#include "CPGameModeBase.h"


ACPGameModeBase::ACPGameModeBase() {
	bGameOver = false;
}

void ACPGameModeBase::ResetLevel()
{
	K2_ResetLevel();
}

bool ACPGameModeBase::HasMatchEnded() const
{
	return bGameOver;
}

void ACPGameModeBase::GameOver()
{
	if (bGameOver == false)
	{
		K2_OnGameOver();
		bGameOver = true;
	}
}
