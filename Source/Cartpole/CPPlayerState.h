// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerState.h"
#include "CPPlayerState.generated.h"

/**
 *
 */
UCLASS()
class CARTPOLE_API ACPPlayerState : public APlayerState
{
	GENERATED_BODY()

public:

	//! Expose SetScore to blueprint so we can implement a custom reward function
	UFUNCTION(BlueprintCallable, Category = Score)
	void K2_SetScore(const float value) {
		SetScore(value);
	}
};
