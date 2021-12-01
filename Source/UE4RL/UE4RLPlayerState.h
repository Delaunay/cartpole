// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerState.h"
#include "UE4RLPlayerState.generated.h"

/**
 * 
 */
UCLASS()
class UE4RL_API AUE4RLPlayerState : public APlayerState
{
	GENERATED_BODY()

public:

	// use score as reward
	UFUNCTION(BlueprintCallable, Category = Score)
	void K2_SetScore(const float value) {
		SetScore(value);
	}
};
