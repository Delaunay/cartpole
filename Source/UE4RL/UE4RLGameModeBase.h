// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameModeBase.h"
#include "UE4RLGameModeBase.generated.h"

/**
 * 
 */
UCLASS()
class UE4RL_API AUE4RLGameModeBase : public AGameModeBase
{
	GENERATED_BODY()

public:
	AUE4RLGameModeBase();
	
	virtual void ResetLevel() override;

	/** Returns true if GameOver() has been called, false otherwise */
	virtual bool HasMatchEnded() const override;

	/** Called when the game is over 
	 * i.e. the player dies, the time runs out or the game is finished*/
	UFUNCTION(BlueprintCallable, Category = Game)
	virtual void GameOver();

protected:
	UFUNCTION(BlueprintImplementableEvent, Category = Game, meta = (DisplayName = "ResetLevel", ScriptName = "ResetLevel"))
	void K2_ResetLevel();

	UFUNCTION(BlueprintImplementableEvent, Category = Game, meta = (DisplayName = "OnGameOver", ScriptName = "OnGameOver"))
	void K2_OnGameOver();

	UPROPERTY(BlueprintReadOnly, Category = Game)
	uint32 bGameOver : 1;
};
